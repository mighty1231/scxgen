
from struct import pack, unpack
from inspect import currentframe

from .. import binio
from ..coder import Coder
from ..trgconst import *
from ..trgstrconst import *
from ..utils import FlattenList
from ..chktok import Section

__all__ = ['MBAction', 'MBTrigger', 'MBRFSection']


# code method should be one of the following strategies
_available_methods_ = [
	Coder.Default, Coder.AllyStatus, Coder.Comparison, Coder.Modifier,
	Coder.Order, Coder.Player, Coder.PropState, Coder.Resource,
	Coder.Score, Coder.SwitchAction, Coder.SwitchState,
	Coder.AIScript, Coder.Count, Coder.String, Coder.Location,
	Coder.Unit, Coder.Switch
]

'''
Mission Briefing Actions

                         +0x00   +0x04   +0x08   +0x0C   +0x10   +0x14   +0x18   +0x1A   +0x1B   +0x1C
                                  WORD    WORD   DWORD    BYTE   DWORD    WORD    BYTE    BYTE    BYTE
                                  strid  wavid    time    slot   vtime  unitid acttype     mod    flag
Wait                                              Time                               1
PlayWAV                                    Wav                                       2
TextMessage                       Text            Time                               3
MissionObjective                  Text                                               4
ShowPortrait                                              Slot            Unit       5
HidePortrait                                              Slot                       6
DisplaySpeakingPortrait                           Time    Slot                       7
Transmission                      Text     Wav    WTime   Slot   VTime               8 modifier
'''
class MBAction:
	# only defined on superior class
	_subclass_filter_ = {}   # {lambda s:s.acttype == 2 : PlayWav, ...}
	_orig_args_ = ['strid', 'wavid', 'time', 'slot', 'vtime',
					'unitid', 'acttype', 'mod', 'flag']

	# must specific for each subclasses
	_id_ = 0
	_args_ = [
		('strid', Coder.Default),
		('wavid', Coder.Default),
		('time', Coder.Default),
		('slot', Coder.Default),
		('vtime', Coder.Default),
		('unitid', Coder.Default),
		('acttype', Coder.Default),
		('mod', Coder.Default),
		('flag', Coder.Default),
	]
	_extra_args_ = {}
	_identity_ = None  # if it is None, automatically set to lambda p:p.acttype = cls._id_
	_args_base_ = _orig_args_ # thisis automatically evaluated for subclasses

	def __init__(self, *args):
		assert len(args) == len(self._args_) or len(args) == 0, "Check syntax, %s(%s)" \
				% (self.__class__.__name__, ','.join(map(lambda p:p[0], self._args_)))

		self._strid    = None if 'strid' in self._args_base_ else 0
		self._wavid    = None if 'wavid' in self._args_base_ else 0
		self._time     = None if 'time' in self._args_base_ else 0
		self._slot     = None if 'slot' in self._args_base_ else 0
		self._vtime    = None if 'vtime' in self._args_base_ else 0
		self._unitid   = None if 'unitid' in self._args_base_ else 0
		self._acttype  = None if 'acttype' in self._args_base_ else self._id_
		self._mod      = None if 'mod' in self._args_base_ else 0
		self._flag     = None if 'flag' in self._args_base_ else 0

		for i in range(len(args)):
			self.__setattr__(self._args_base_[i], args[i])

	@staticmethod
	def __getbase(cls, arg):
		temp = arg
		while temp not in MBAction._orig_args_:
			if temp in cls._extra_args_:
				temp = cls._extra_args_[temp]
			else:
				raise RuntimeError('Argument %s is not appropriate for %s' % (arg, cls))
		return temp

	# __init_subclass__ is availble for only python 3.6 or higher
	def __init_subclass__(cls, **kwargs):
		super().__init_subclass__(**kwargs)
		if cls._id_ == 0:
			raise RuntimeError("Subclass of MBAction should have positive _id_")
		if cls._identity_ == None:
			cls._identity_ = lambda act : act._acttype == cls._id_
		MBAction._subclass_filter_[cls._identity_] = cls
		cls._args_base_ = list(map(lambda arg:MBAction.__getbase(cls, arg[0]), cls._args_))


	def Encode(self, starcraftmap=None):
		if None in (self._strid, self._wavid, self._time, self._slot, self._vtime,
			self._unitid, self._acttype, self._mod, self._flag):
			raise RuntimeError('Undefined variable from encoding:\n\t%s' % self.Decode())

		# same order with self._orig_args_
		args = [self._strid, self._wavid, self._time, self._slot,
			self._vtime, self._unitid, self._acttype, self._mod, self._flag]

		for i in range(len(args)):
			if MBAction._orig_args_[i] in self._args_base_:
				args[i] = Coder.encode(
					starcraftmap,
					self._args_[self._args_base_.index(MBAction._orig_args_[i])][1],
					args[i])

		args = [0, ] + args + [0, 0, 0]
		return pack('<IIIIIIHBBBBBB', *args)

	def Decode(self, starcraftmap=None):
		cls = MBAction.GetType(self)

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
		for identity, c in MBAction._subclass_filter_.items():
			if identity(act):
				return c
		return MBAction

	def __getattr__(self, attr):
		while attr not in MBAction._orig_args_ and attr in self._extra_args_:
			attr = self._extra_args_[attr]

		if attr in MBAction._orig_args_:
			return lambda p:[self.__setattr__(attr, p), self][1]
		elif isinstance(attr, tuple):
			return lambda *p:[[self.__setattr__(attr[i], p[i])
				for i in range(len(p))], self][1]
		elif hasattr(attr, '__call__'):
			return lambda *args,**kwargs:[attr(self, *args, **kwargs), self][1]
		else:
			raise AttributeError

	def __setattr__(self, name, value):
		while name not in MBAction._orig_args_ and name in self._extra_args_:
			name = self._extra_args_[name]

		if name in self._args_base_:
			if '_'+name in self.__dict__ and self.__getattribute__('_'+name) != None:
				raise RuntimeError('Assigning twice for single attribute is prohibited')
			super().__setattr__('_'+name, value)
		elif name[0] == '_' and name[1:] in MBAction._orig_args_:
			assert type(value) == int or value == None
			if name in self.__dict__ and self.__getattribute__(name) != None:
				raise RuntimeError('Assigning twice for single attribute is prohibited')
			super().__setattr__(name, value)
		else:
			raise AttributeError

class MBTrigger:
	_sections_ = []
	def __init__(self, players, actions=[]):
		self.debuginfo = []
		f = currentframe().f_back
		while f != None:
			self.debuginfo.append((f.f_code.co_filename, f.f_lineno))
			f = f.f_back

		players = FlattenList(players)
		actions = FlattenList(actions)

		self.players = players
		self.actions = actions

		for section in MBTrigger._sections_:
			section.AddMBTrigger(self)

	def Encode(self, starcraftmap):
		log = ''
		try:
			log = 'The number of actions should be less than or equal to 64'
			assert len(self.actions) <= 64

			# Mission briefing trigger should have following bytes in 'condition area'
			b = [bytes(15), bytes([0xD, 0, 0, 0, 0]), bytes(20*15)]

			# same as Trigger
			for i in range(64):
				if i < len(self.actions):
					act = self.actions[i]
					log = 'Encoding action #%d, should be action type\n' \
						'Hint: actions for mission briefing have all MB-prefix' % (i+1)
					assert isinstance(act, MBAction)
					log = 'Encoding action #%d: %s' % (i+1, MBAction.GetType(act).__name__)
					b.append(act.Encode(starcraftmap))
				else:
					b.append(bytes(32))

			b.append(bytes(4))

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
			print('ENCODING ERROR during [%s] with mission briefing trigger defined at' % log)
			for i, (fname, lineno) in enumerate(self.debuginfo):
				print('>> %2d. Line %3d in File %s' % (i, lineno, fname))
			print('--------------------------------------------------')
			print("Following is the exception message from python")
			print('--------------------------------------------------')
			print(format_exc(), end='')
			print('--------------------------------------------------')

			sys.exit(-1)

	def Decode(self, starcraftmap):
		s = 'MBTrigger(\n'
		s += '\tplayers = [%s],\n' \
			% ', '.join(map(lambda p:Coder.decode(None, Coder.Player, p), self.players))
		if len(self.actions) == 0:
			s += '\tactions = []\n'
		elif len(self.actions) == 1:
			s += '\tactions = [%s]\n' % self.actions[0].Decode(starcraftmap)
		else:
			s += '\tactions = [\n'
			for a in self.actions:
				s += '\t\t%s,\n' % a.Decode(starcraftmap)
			s += '\t]\n'
		s += ')'

		return s

	@staticmethod
	def InitWithBinary(binary):
		assert len(binary) == 2400

		actions = []
		players = []

		for i in range(64):
			args = unpack('<IIIIIHBBB', binary[320+32*i+4:320+32*(i+1)-3])
			if args[6] == 0: # _acttype
				break
			actions.append(MBAction(*args))

		for i in range(28):
			if binary[16*20+64*32+4+i]:
				players.append(i)

		return MBTrigger(players, actions)

	@staticmethod
	def InstallSectionHook(mbrfsection):
		MBTrigger._sections_.append(mbrfsection)

	@staticmethod
	def UninstallSectionHook(mbrfsection):
		MBTrigger._sections_.remove(mbrfsection)

class MBRFSection(Section, Name='MBRF'):
	def __init__(self, content, starcraftmap):
		self.mbtriggers = []
		self.binaries = []
		self.starcraftmap = starcraftmap
		self.Load(content)

	def Load(self, content):
		for i in range(0, len(content), 2400):
			self.mbtriggers.append(MBTrigger.InitWithBinary(content[i:i+2400]))
			self.binaries.append(content[i:i+2400])

	def InstallMBTriggerHook(self):
		MBTrigger.InstallSectionHook(self)

	def UninstallMBTriggerHook(self):
		MBTrigger.UninstallSectionHook(self)

	def AddMBTrigger(self, mbtrigger):
		assert isinstance(mbtrigger, MBTrigger)
		self.mbtriggers.append(mbtrigger)
		self.binaries.append(mbtrigger.Encode(self.starcraftmap))

	def Save(self):
		return b''.join(self.binaries)

