
from struct import pack, unpack
from inspect import currentframe

if __name__ == '__main__':
	import sys
	sys.path.append('..')
	from coder import Coder
	from trgconst import *
	from utils import FlattenList
	import binio
	from chktok import Section
else:
	from .. import binio
	from ..coder import Coder
	from ..trgconst import *
	from ..trgstrconst import *
	from ..utils import FlattenList
	from ..chktok import Section

__all__ = ['Condition', 'Action', 'Trigger']

#
# Command(P3, AtLeast, 4, "Terran Marine") should be same with
# Command().Player(P3).Count(4).Comparison(AtLeast).Unit("Terran Marine")
#


# code method should be one of the following strategies
_available_methods_ = [
	Coder.Default, Coder.AllyStatus, Coder.Comparison, Coder.Modifier,
	Coder.Order, Coder.Player, Coder.PropState, Coder.Resource,
	Coder.Score, Coder.SwitchAction, Coder.SwitchState,
	Coder.AIScript, Coder.Count, Coder.String, Coder.Location,
	Coder.Unit, Coder.Switch
]
class Condition:
	# only defined on superior class
	_subclass_filter_ = {}   # {lambda s:s.condtype == 2 : Command, ...}
	_orig_args_ = ['locid', 'player', 'amount', 'unitid',
		'comparison', 'condtype', 'restype', 'flag']

	# must specific for each subclasses
	_id_ = 0
	_args_ = [('locid', Coder.Default),   # arg_name and code_method
			  ('player', Coder.Default),
			  ('amount', Coder.Default),
			  ('unitid', Coder.Default),
			  ('comparison', Coder.Default),
			  ('condtype', Coder.Default),
			  ('restype', Coder.Default),
			  ('flag', Coder.Default)]
	_extra_args_ = {}
	_identity_ = None  # if it is None, automatically set to lambda p:p.condtype = cls._id_
	_args_base_ = _orig_args_ # this is automatically evaluated for subclasses

	def __init__(self, *args):
		assert len(args) == len(self._args_) or len(args) == 0, "Check syntax, %s(%s)" \
				% (self.__class__.__name__, ','.join(map(lambda p:p[0], self._args_)))

		self._locid      = None if 'locid' in self._args_base_ else 0
		self._player     = None if 'player' in self._args_base_ else 0
		self._amount     = None if 'amount' in self._args_base_ else 0
		self._unitid     = None if 'unitid' in self._args_base_ else 0
		self._comparison = None if 'comparison' in self._args_base_ else 0
		self._condtype   = None if 'condtype' in self._args_base_ else self._id_
		self._restype    = None if 'restype' in self._args_base_ else 0
		self._flag       = None if 'flag' in self._args_base_ else 0

		for i in range(len(args)):
			self.__setattr__(self._args_base_[i], args[i])

	@staticmethod
	def __getbase(cls, arg):
		temp = arg
		while temp not in Condition._orig_args_:
			if temp in cls._extra_args_:
				temp = cls._extra_args_[temp]
			else:
				raise RuntimeError('Argument %s is not appropriate for %s' % (arg, cls))
		return temp

	# __init_subclass__ is availble for only python 3.6 or higher
	def __init_subclass__(cls, **kwargs):
		super().__init_subclass__(**kwargs)
		if cls._id_ == 0:
			raise RuntimeError("Subclass of Condition should have positive _id_")
		if cls._identity_ == None:
			cls._identity_ = lambda cond : cond._condtype == cls._id_
		Condition._subclass_filter_[cls._identity_] = cls
		cls._args_base_ = list(map(lambda arg:Condition.__getbase(cls, arg[0]), cls._args_))

	def Encode(self, starcraftmap=None):
		if None in (self._locid, self._player, self._amount, self._unitid,
			self._comparison, self._condtype, self._restype, self._flag):
			raise RuntimeError('Undefined variable from encoding:\n\t%s' % self.Decode())

		# same order with self._orig_args_
		args = [self._locid, self._player, self._amount, self._unitid,
			self._comparison, self._condtype, self._restype, self._flag]

		for i in range(len(args)):
			if Condition._orig_args_[i] in self._args_base_:
				args[i] = Coder.encode(
					starcraftmap,
					self._args_[self._args_base_.index(Condition._orig_args_[i])][1],
					args[i])

		if args[1] < 0:
			arg[1] += 0x100000000 # EPD, player

		args += (0, 0)

		return pack('<IIIHBBBBBB', *args)

	def Decode(self, starcraftmap=None):
		cls = Condition.GetType(self)

		decoded_vars = []
		for i in range(len(cls._args_)):
			var = self.__getattribute__('_'+cls._args_base_[i])
			if var == None:
				decoded_vars.append('None')
			else:
				decoded_vars.append(
					Coder.decode(
						starcraftmap,
						cls._args_[i][1], # decoding strategy
						var))
		return '%s(%s)' % (cls.__name__, ', '.join(decoded_vars))

	@staticmethod
	def GetType(cond):
		for identity, c in Condition._subclass_filter_.items():
			if identity(cond):
				return c
		return Condition

	def __getattr__(self, attr):
		while attr not in Condition._orig_args_ and attr in self._extra_args_:
			attr = self._extra_args_[attr]

		if attr in Condition._orig_args_:
			return lambda p:[self.__setattr__(attr, p), self][1]
		elif isinstance(attr, tuple):
			return lambda *lp:(lambda p:[[self.__setattr__(attr[i], p[i])
				for i in range(len(p))], self][1])(FlattenList(lp))
		elif hasattr(attr, '__call__'):
			return lambda *args,**kwargs:[attr(self, *FlattenList(args), **kwargs), self][1]
		else:
			raise AttributeError

	def __setattr__(self, name, value):
		while name not in Condition._orig_args_ and name in self._extra_args_:
			name = self._extra_args_[name]

		if name in self._args_base_:
			if '_'+name in self.__dict__ and self.__getattribute__('_'+name) != None:
				raise RuntimeError('Assigning twice for single attribute is prohibited')
			super().__setattr__('_'+name, value)
		elif name[0] == '_' and name[1:] in Condition._orig_args_:
			assert type(value) == int or value == None
			if name in self.__dict__ and self.__getattribute__(name) != None:
				raise RuntimeError('Assigning twice for single attribute is prohibited')
			super().__setattr__(name, value)
		else:
			raise AttributeError



class Action:
	# only defined on superior class
	_subclass_filter_ = {}   # {lambda s:s.acttype == 2 : Defeat, ...}
	_orig_args_ = ['locid1', 'strid', 'wavid', 'time', 'player1',
					   'player2', 'unitid', 'acttype', 'amount', 'flag']

	# must specific for each subclasses
	_id_, _flag_ = 0, 0
	_args_ = [
		('locid1', Coder.Default),
		('strid', Coder.Default),
		('wavid', Coder.Default),
		('time', Coder.Default),
		('player1', Coder.Default),
		('player2', Coder.Default),
		('unitid', Coder.Default),
		('acttype', Coder.Default),
		('amount', Coder.Default),
		('flag', Coder.Default)
	]
	_extra_args_ = {}
	_identity_ = None  # if it is None, automatically set to lambda p:p.acttype = cls._id_
	_args_base_ = _orig_args_ # thisis automatically evaluated for subclasses

	def __init__(self, *args):
		assert len(args) == len(self._args_) or len(args) == 0, "Check syntax, %s(%s)" \
				% (self.__class__.__name__, ','.join(map(lambda p:p[0], self._args_)))

		self._locid1   = None if 'locid1' in self._args_base_ else 0
		self._strid    = None if 'strid' in self._args_base_ else 0
		self._wavid    = None if 'wavid' in self._args_base_ else 0
		self._time     = None if 'time' in self._args_base_ else 0
		self._player1  = None if 'player1' in self._args_base_ else 0
		self._player2  = None if 'player2' in self._args_base_ else 0
		self._unitid   = None if 'unitid' in self._args_base_ else 0
		self._acttype  = None if 'acttype' in self._args_base_ else self._id_
		self._amount   = None if 'amount' in self._args_base_ else 0
		self._flag     = None if 'flag' in self._args_base_ else self._flag_

		for i in range(len(args)):
			self.__setattr__(self._args_base_[i], args[i])

	@staticmethod
	def __getbase(cls, arg):
		temp = arg
		while temp not in Action._orig_args_:
			if temp in cls._extra_args_:
				temp = cls._extra_args_[temp]
			else:
				raise RuntimeError('Argument %s is not appropriate for %s' % (arg, cls))
		return temp

	# __init_subclass__ is availble for only python 3.6 or higher
	def __init_subclass__(cls, **kwargs):
		super().__init_subclass__(**kwargs)
		if cls._id_ == 0:
			raise RuntimeError("Subclass of Action should have positive _id_")
		if cls._identity_ == None:
			cls._identity_ = lambda act : act._acttype == cls._id_
		Action._subclass_filter_[cls._identity_] = cls
		cls._args_base_ = list(map(lambda arg:Action.__getbase(cls, arg[0]), cls._args_))


	def Encode(self, starcraftmap=None):
		if None in (self._locid1, self._strid, self._wavid,
			self._time, self._player1, self._player2, self._unitid,
			self._acttype, self._amount, self._flag):
			raise RuntimeError('Undefined variable from encoding:\n\t%s' % self.Decode())

		# same order with self._orig_args_
		args = [self._locid1, self._strid, self._wavid,
			self._time, self._player1, self._player2, self._unitid,
			self._acttype, self._amount, self._flag]

		for i in range(len(args)):
			if Action._orig_args_[i] in self._args_base_:
				args[i] = Coder.encode(
					starcraftmap,
					self._args_[self._args_base_.index(Action._orig_args_[i])][1],
					args[i])

		if args[4] < 0:
			args[4] += 0x100000000  # EPD, player1
		if args[5] < 0:
			args[5] += 0x100000000  # EPD, player2

		args += (0, 0, 0)

		return pack('<IIIIIIHBBBBBB', *args)

	def Decode(self, starcraftmap=None):
		cls = Action.GetType(self)

		decoded_vars = []
		for i in range(len(cls._args_)):
			var = self.__getattribute__('_'+cls._args_base_[i])
			if var == None:
				decoded_vars.append('None')
			else:
				decoded_vars.append(
					Coder.decode(
						starcraftmap,
						cls._args_[i][1], # decoding strategy
						var))
		return '%s(%s)' % (cls.__name__, ', '.join(decoded_vars))

	@staticmethod
	def GetType(act):
		for identity, c in Action._subclass_filter_.items():
			if identity(act):
				return c
		return Action

	def __getattr__(self, attr):
		while attr not in Action._orig_args_ and attr in self._extra_args_:
			attr = self._extra_args_[attr]

		if attr in Action._orig_args_:
			return lambda p:[self.__setattr__(attr, p), self][1]
		elif isinstance(attr, tuple):
			return lambda *lp:(lambda p:[[self.__setattr__(attr[i], p[i])
				for i in range(len(p))], self][1])(FlattenList(lp))
		elif hasattr(attr, '__call__'):
			return lambda *args,**kwargs:[attr(self, *FlattenList(args), **kwargs), self][1]
		else:
			raise AttributeError

	def __setattr__(self, name, value):
		while name not in Action._orig_args_ and name in self._extra_args_:
			name = self._extra_args_[name]

		if name in self._args_base_:
			if '_'+name in self.__dict__ and self.__getattribute__('_'+name) != None:
				raise RuntimeError('Assigning twice for single attribute is prohibited')
			super().__setattr__('_'+name, value)
		elif name[0] == '_' and name[1:] in Action._orig_args_:
			assert type(value) == int or value == None
			if name in self.__dict__ and self.__getattribute__(name) != None:
				raise RuntimeError('Assigning twice for single attribute is prohibited')
			super().__setattr__(name, value)
		else:
			raise AttributeError

class Trigger:
	_hooks_ = []
	_sections_ = []
	def __init__(self, players, conditions=[], actions=[], flag=[]):
		self.debuginfo = []
		f = currentframe().f_back
		while f != None:
			self.debuginfo.append((f.f_code.co_filename, f.f_lineno))
			f = f.f_back

		players = FlattenList(players)
		conditions = FlattenList(conditions)
		actions = FlattenList(actions)
		flag = FlattenList(flag)

		self.players = players
		self.conditions = conditions
		self.actions = actions
		self.flag = flag

		for hookfunc in Trigger._hooks_:
			hookfunc(self)

		self.players = FlattenList(self.players)
		self.conditions = FlattenList(self.conditions)
		self.actions = FlattenList(self.actions)
		self.flag = FlattenList(self.flag)
		
		for section in Trigger._sections_:
			section.AddTrigger(self)

	def Encode(self, starcraftmap):
		log = ''
		try:
			log = 'The number of conditions should be less than or equal to 16'
			assert len(self.conditions) <= 16

			log = 'The number of actions should be less than or equal to 64'
			assert len(self.actions) <= 64

			b = []
			for i in range(16):
				if i < len(self.conditions):
					cond = self.conditions[i]
					log = 'Encoding condition #%d, should be condition type' % (i+1)
					assert isinstance(cond, Condition)
					log = 'Encoding condition #%d: %s' % (i+1, Condition.GetType(cond).__name__)
					b.append(cond.Encode(starcraftmap))
				else:
					b.append(bytes(20))
			for i in range(64):
				if i < len(self.actions):
					act = self.actions[i]
					log = 'Encoding action #%d, should be action type' % (i+1)
					assert isinstance(act, Action)
					log = 'Encoding action #%d: %s' % (i+1, Action.GetType(act).__name__)
					b.append(act.Encode(starcraftmap))
				else:
					b.append(bytes(32))

			log = 'Encoding flags'
			trg_flag = 0
			if actexec in self.flag:
				trg_flag |= 1
			if preserved in self.flag:
				trg_flag |= 4
			if disabled in self.flag:
				trg_flag |= 8
			b.append(binio.i2b4(trg_flag))

			log = 'Encoding player'
			self.players = list(map(
				lambda p:Coder.encode(None, Coder.Player, p),
				self.players))
			b.append(bytes([1 if p in self.players else 0 for p in range(28)]))

			return b''.join(b)
		except Exception as err:
			from traceback import format_exc
			import sys
			print('--------------------------------------------------')
			print('ENCODING ERROR during [%s] with trigger defined at' % log)
			for i, (fname, lineno) in enumerate(self.debuginfo):
				print('>> %2d. Line %3d in File %s' % (i, lineno, fname))
			print('--------------------------------------------------')
			print("Following is the exception message from python")
			print('--------------------------------------------------')
			print(format_exc(), end='')
			print('--------------------------------------------------')

			sys.exit(-1)

	def Decode(self, starcraftmap):
		s = 'Trigger(\n'
		s += '\tplayers = [%s],\n' \
			% ', '.join(map(lambda p:Coder.decode(None, Coder.Player, p), self.players))
		if len(self.conditions) == 0:
			s += '\tconditions = [],\n'
		elif len(self.conditions) == 1:
			s += '\tconditions = [%s],\n' % self.conditions[0].Decode(starcraftmap)
		else:
			s += '\tconditions = [\n'
			for c in self.conditions:
				s += '\t\t%s,\n' % c.Decode(starcraftmap)
			s += '\t],\n'
		if len(self.actions) == 0:
			s += '\tactions = [],\n'
		elif len(self.actions) == 1:
			s += '\tactions = [%s],\n' % self.actions[0].Decode(starcraftmap)
		else:
			s += '\tactions = [\n'
			for a in self.actions:
				s += '\t\t%s,\n' % a.Decode(starcraftmap)
			s += '\t],\n'

		flagdict = {actexec:'actexec', preserved:'preserved', disabled:'disabled'}
		s += '\tflag = [%s]\n' % ', '.join(map(lambda t:flagdict.get(t, t), self.flag))
		s += ')'

		return s

	@staticmethod
	def InitWithBinary(binary):
		assert len(binary) == 2400

		conditions = []
		actions = []
		players = []
		flags = []
		for i in range(16):
			args = unpack('<IIIHBBBBBB'[:-2], binary[20*i:20*(i+1)-2])
			if args[5] == 0: # condtype
				break
			conditions.append(Condition(*args))

		for i in range(64):
			args = unpack('<IIIIIIHBBBBBB'[:-3], binary[320+32*i:320+32*(i+1)-3])
			if args[7] == 0: # _acttype
				break
			actions.append(Action(*args))

		_flag = binio.b2i4(binary, 16*20+64*32)
		if _flag & 1:
			flags.append(actexec)
		if _flag & 4:
			flags.append(preserved)
		if _flag & 8:
			flags.append(disabled)

		for i in range(28):
			if binary[16*20+64*32+4+i]:
				players.append(i)

		return Trigger(players, conditions, actions, flags)

	@staticmethod
	def InstallHook(func):
		Trigger._hooks_.append(func)

	@staticmethod
	def UninstallHook(func):
		Trigger._hooks_.remove(func)

	@staticmethod
	def InstallSectionHook(trigsection):
		Trigger._sections_.append(trigsection)

	@staticmethod
	def UninstallSectionHook(trigsection):
		Trigger._sections_.remove(trigsection)

class TRIGSection(Section, Name='TRIG'):
	def __init__(self, content, starcraftmap):
		self.triggers = []
		self.binaries = []
		self.starcraftmap = starcraftmap
		self.Load(content)

	def Load(self, content):
		for i in range(0, len(content), 2400):
			self.triggers.append(Trigger.InitWithBinary(content[i:i+2400]))
			self.binaries.append(content[i:i+2400])

	def InstallTriggerHook(self):
		Trigger.InstallSectionHook(self)

	def UninstallTriggerHook(self):
		Trigger.UninstallSectionHook(self)

	def AddTrigger(self, trigger):
		assert isinstance(trigger, Trigger)
		self.triggers.append(trigger)
		self.binaries.append(trigger.Encode(self.starcraftmap))

	def Save(self):
		return b''.join(self.binaries)


def test_cond():
	class Command(Condition):
		_id_ = 2
		_args_ = [
			('Player'     , Coder.Player),
			('Comparison' , Coder.Comparison),
			('Number'     , Coder.Default),
			('Unit'       , Coder.Unit)
		]
		_extra_args_ = {
			'Player'     : 'player',
			'Comparison' : 'comparison',
			'Number'     : 'amount',
			'Unit'       : 'unitid',
			'PUnit'      :  ('Player', 'Unit'),
			'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
			'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
			'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number)
		}
	c = Command(1, 3, 2, 4)
	print(c.Decode())
	print(unpack('<IIIHBBBBBB', c.Encode()))

	c = Command().Player(3535).Number(3).Comparison(AtLeast).Unit(4)
	print(c.Decode())
	print(unpack('<IIIHBBBBBB', c.Encode()))

	c = Command().Number(3).Comparison(10).PUnit(2222, 4444)
	print(c.Decode())
	print(unpack('<IIIHBBBBBB', c.Encode()))

	c = Command().AtLeast(30).PUnit(3, 'Terran')
	print(c.Decode())
	print(unpack('<IIIHBBBBBB', c.Encode()))

	c2 = Condition(0, 1, 2, 4, 3, 2, 0, 0)
	print(c2.Decode())

def test_act():
	class Transmission(Action):
		_id_, _flag_ = 7, 123
		_args_ = [
			('Unit'         , Coder.Unit),
			('Where'        , Coder.Location),
			('WAVName'      , Coder.String),
			('TimeModifier' , Coder.Modifier),
			('Time'         , Coder.Default),
			('Text'         , Coder.String),
		]
		_extra_args_ = {
			'Unit'         : 'unitid',
			'Where'        : 'locid1',
			'WAVName'      : 'wavid',
			'TimeModifier' : 'amount',
			'Time'         : 'time',
			'Text'         : 'strid',
		}

		def __init__(self, *args, AlwaysDisplay = 4):
			super().__init__(*args)
			self._flag = AlwaysDisplay

	t = Transmission('t', 3333, 55, 66, 77, 88)
	print(t.Decode())
	print(unpack('<IIIIIIHBBBBBB', t.Encode()))

	t = Transmission('t', 3333, 55, 66, 77, 88, AlwaysDisplay = 22)
	print(t.Decode())
	print(unpack('<IIIIIIHBBBBBB', t.Encode()))

	t = Action(666, 555, 555, 77, 0, 0, 3343, 7, 66, 4)
	print(t.Decode())
	print(unpack('<IIIIIIHBBBBBB', t.Encode()))

def test_trigger(): 
	class Command(Condition):
		_id_ = 2
		_args_ = [
			('Player'     , Coder.Player),
			('Comparison' , Coder.Comparison),
			('Number'     , Coder.Default),
			('Unit'       , Coder.Unit)
		]
		_extra_args_ = {
			'Player'     : 'player',
			'Comparison' : 'comparison',
			'Number'     : 'amount',
			'Unit'       : 'unitid',
			'PUnit'      :  ('Player', 'Unit'),
			'AtLeast'    : lambda cond, number: cond.Comparison(AtLeast).Number(number),
			'AtMost'     : lambda cond, number: cond.Comparison(AtMost).Number(number),
			'Exactly'    : lambda cond, number: cond.Comparison(Exactly).Number(number)
		}

	class Transmission(Action):
		_id_, _flag_ = 7, 123
		_args_ = [
			('Unit'         , Coder.Unit),
			('Where'        , Coder.Location),
			('WAVName'      , Coder.String),
			('TimeModifier' , Coder.Modifier),
			('Time'         , Coder.Default),
			('Text'         , Coder.String),
		]
		_extra_args_ = {
			'Unit'         : 'unitid',
			'Where'        : 'locid1',
			'WAVName'      : 'wavid',
			'TimeModifier' : 'amount',
			'Time'         : 'time',
			'Text'         : 'strid',
		}

		def __init__(self, *args, AlwaysDisplay = 4):
			super().__init__(*args)
			self._flag = AlwaysDisplay

	t = Trigger(
		players = [P1, P4],
		conditions = Command().Number(3).Comparison(10).PUnit(2222, 4444),
		actions = Transmission(1, 2, 3, 4, 5, 6),
		flag = [actexec]
	)
	print(t.Decode(None))

if __name__ == '__main__':
	# test_cond()
	# test_act()
	test_trigger()
	pass

