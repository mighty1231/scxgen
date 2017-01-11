from struct import pack, unpack
from collections import namedtuple

if __name__ == '__main__':
	import sys
	sys.path.append('..')
	from chktok import Section
else:
	from ..chktok import Section



class UPRPSection(Section, Name='UPRP'):
	def __init__(self, content, starcraftmap):
		self.uprps = []
		self.hookfunc = lambda t:self.AddUnitProperty(t)
		self.starcraftmap = starcraftmap
		self.Load(content)

	def Load(self, content):
		for i in range(0, len(content), 20):
			self.uprps.append(UnitProperty.InitWithBinary(content[i:i+20]))

	def Clear(self):
		self.uprps.clear()

	def InstallUnitPropertyHook(self):
		if self.starcraftmap:
			UnitProperty.InstallHook(self.hookfunc)

	def UninstallUnitPropertyHook(self):
		if self.starcraftmap:
			UnitProperty.UninstallHook(self.hookfunc)

	def AddUnitProperty(self, uprp):
		assert isinstance(uprp, UnitProperty)
		if not uprp in self.uprps:
			assert len(self.uprps) < 64, 'Unit property table overflow'
			self.uprps.append(uprp)

	def EncodeUnitProperty(self, uprp):
		assert uprp in self.uprps
		return self.uprps.index(uprp) + 1

	def DecodeUnitProperty(self, uprpid):
		assert 0 < uprpid <= len(self.uprps)
		return self.uprps[uprpid - 1].Decode()

	def Save(self):
		return b''.join(map(UnitProperty.Encode, self.uprps)) + bytes(20 * (64 - len(self.uprps)))

class UnitProperty:
	_hooks_ = []
	def __init__(self,
				 hitpoint=None, shield=None, energy=None, resource=None,
				 hanger=None, clocked=None, burrowed=None, intransit=None,
				 hallucinated=None, invincible=None
				 ):
		'''
		Properties : Value/None (Don't care)
		 hitpoint : 0~100(%)  cf) When unit's hitpoint is greater than 167772,
		 shield   : 0~100(%)    you should give hitpoint None to make 100%% HP.
		 energy   : 0~100(%)
		 resource : 0~4294967295
		 hanger   : 0~65536 (Count)

		Special properties : True(Enabled)/False(Disabled)/None(Don't care)
		 clocked      : Unit is clocked.
		 burrowed     : Unit is burrowed.
		 intransit    : Unit is lifted. (In transit)
		 hallucinated : Unit is hallucination.
		 invincible   : Unit is invincible.

		ex) UnitProperty(hitpoint = 50, burrowed = True)
		'''
		assert hitpoint is None or 0 <= hitpoint <= 100
		assert shield is None or 0 <= shield <= 100
		assert energy is None or 0 <= energy <= 100
		assert resource is None or 0 <= resource
		assert hanger is None or 0 <= hanger <= 255

		assert clocked in [None, True, False]
		assert burrowed in [None, True, False]
		assert intransit in [None, True, False]
		assert hallucinated in [None, True, False]
		assert invincible in [None, True, False]

		def prop2int(p):
			if p is None:
				return 0
			else:
				return p

		def prop2valid(p, v):
			if p is None:
				return 0
			else:
				return v

		def prop2flag(p, v):
			if p:
				return v
			else:
				return 0

		self.player = 0

		# Set properties
		self.hitpoint = prop2int(hitpoint)
		self.shield = prop2int(shield)
		self.energy = prop2int(energy)
		self.resource = prop2int(resource)
		self.hanger = prop2int(hanger)

		self.prpvalid = (
			prop2valid(hitpoint, 1 << 1) |
			prop2valid(shield,   1 << 2) |
			prop2valid(energy,   1 << 3) |
			prop2valid(resource, 1 << 4) |
			prop2valid(hanger,   1 << 5)
		)

		# Set special properties
		self.sprpvalid = (
			prop2valid(clocked,      1 << 0) |
			prop2valid(burrowed,     1 << 1) |
			prop2valid(intransit,    1 << 2) |
			prop2valid(hallucinated, 1 << 3) |
			prop2valid(invincible,   1 << 4)
		)

		self.sprpflag = (
			prop2flag(clocked,      1 << 0) |
			prop2flag(burrowed,     1 << 1) |
			prop2flag(intransit,    1 << 2) |
			prop2flag(hallucinated, 1 << 3) |
			prop2flag(invincible,   1 << 4)
		)
		self.unused = 0

		for hookfunc in UnitProperty._hooks_:
			hookfunc(self)

	@staticmethod
	def InstallHook(hookfunc):
		UnitProperty._hooks_.append(hookfunc)

	@staticmethod
	def UninstallHook(hookfunc):
		UnitProperty._hooks_.remove(hookfunc)

	def Encode(self):
		return pack('<HHBBBBIHHI', self.sprpvalid, self.prpvalid,
			self.player, self.hitpoint, self.shield, self.energy,
			self.resource, self.hanger, self.sprpflag, self.unused)

	@staticmethod
	def InitWithBinary(b):
		args = unpack('<HHBBBBIHHI', b)
		res = UnitProperty()
		res.sprpvalid = args[0]
		res.prpvalid  = args[1]
		res.player    = args[2]
		res.hitpoint  = args[3]
		res.shield    = args[4]
		res.energy    = args[5]
		res.resource  = args[6]
		res.hanger    = args[7]
		res.sprpflag  = args[8]
		res.unused    = args[9]
		return res

	def __eq__(self, other):
		if isinstance(other, UnitProperty):
			return all([
				self.sprpvalid  == other.sprpvalid, 
				self.prpvalid   == other.prpvalid, 
				self.player     == other.player, 
				self.hitpoint   == other.hitpoint, 
				self.shield     == other.shield, 
				self.energy     == other.energy, 
				self.resource   == other.resource, 
				self.hanger     == other.hanger, 
				self.sprpflag   == other.sprpflag, 
				# self.unused     == other.unused, 
			])
		return super().__eq__(other)

	def Decode(self):
		args = [
			('hitpoint'    , self.hitpoint if self.prpvalid & (1 << 1) else None),
			('shield'      , self.shield   if self.prpvalid & (1 << 2) else None),
			('energy'      , self.energy   if self.prpvalid & (1 << 3) else None),
			('resource'    , self.resource if self.prpvalid & (1 << 4) else None),
			('hanger'      , self.hanger   if self.prpvalid & (1 << 5) else None),
			('clocked'     , bool(self.sprpflag & (1 << 0)) if self.sprpvalid & (1 << 0) else None),
			('burrowed'    , bool(self.sprpflag & (1 << 1)) if self.sprpvalid & (1 << 1) else None),
			('intransit'   , bool(self.sprpflag & (1 << 2)) if self.sprpvalid & (1 << 2) else None),
			('hallucinated', bool(self.sprpflag & (1 << 3)) if self.sprpvalid & (1 << 3) else None),
			('invincible'  , bool(self.sprpflag & (1 << 4)) if self.sprpvalid & (1 << 4) else None),
		]
		return 'UnitProperty(%s)' % ', '.join(['%s=%s' % (n, v) for n, v in args if v is not None])

if __name__ == '__main__':
	b = b'\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'
	up = UnitProperty.InitWithBinary(b)
	print(up.Decode())
