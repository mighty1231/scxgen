from .trgconst import *
from .trgstrconst import *
from . import binio
from .utils import mapstring2str

class _Unique2:
	pass


class Coder:
	Default       = _Unique2()
	AllyStatus    = _Unique2()
	Comparison    = _Unique2()
	Modifier      = _Unique2()
	Order         = _Unique2()
	Player        = _Unique2()
	PropState     = _Unique2()
	Resource      = _Unique2()
	Score         = _Unique2()
	SwitchAction  = _Unique2()
	SwitchState   = _Unique2()
	AIScript      = _Unique2()
	Count         = _Unique2()
	Property      = _Unique2()
	String        = _Unique2()
	Location      = _Unique2()
	Unit          = _Unique2()
	Switch        = _Unique2()

	AllyStatusMap = [(0, 1, 2), (Enemy, Ally, AlliedVictory)]
	ComparisonMap = [(0, 1, 10), (AtLeast, AtMost, Exactly)]
	ModifierMap = [(7, 8, 9), (SetTo, Add, Subtract)]
	OrderMap = [(0, 1, 2), (Move, Patrol, Attack)]
	PlayerMap = [(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 0, 1, 2, 3, 4, 5, 6, 7,
		8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19, 20, 21, 26),
		(P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12, 
		Player1, Player2, Player3, Player4, Player5, Player6, Player7, 
		Player8, Player9, Player10, Player11, Player12, CurrentPlayer, 
		Foes, Allies, NeutralPlayers, AllPlayers, Force1, Force2, Force3, Force4, 
		NonAlliedVictoryPlayers)]
	PropStateMap = [(4, 5, 6), (Enable, Disable, Toggle)]
	ResourceMap = [(0, 1, 2), (Ore, Gas, OreAndGas)]
	ScoreMap = [(0, 1, 2, 3, 4, 5, 6, 7),
		(Total, Units, Buildings, UnitsAndBuildings,
		None, # Kills should be here
		Razings, KillsAndRazings, Custom)]
	SwitchActionMap = [(4, 5, 6, 11), (Set, Clear, Toggle, Random)]
	SwitchStateMap = [(2, 3), (Set, Cleared)]

	@staticmethod
	def _dec(_map, _int):
		if _int in _map[0]:
			return _map[1][_map[0].index(_int)].GetConstName()
		elif isinstance(_int, Enemy.__class__):
			return _int.GetConstName()
		return mapstring2str(_int)

	@staticmethod
	def decode(starcraftmap, methodtype, value):
		if methodtype == Coder.Default:
			return mapstring2str(value)
		elif methodtype == Coder.AllyStatus:
			return Coder._dec(Coder.AllyStatusMap, value)
		elif methodtype == Coder.Comparison:
			return Coder._dec(Coder.ComparisonMap, value)
		elif methodtype == Coder.Modifier:
			return Coder._dec(Coder.ModifierMap, value)
		elif methodtype == Coder.Order:
			return Coder._dec(Coder.OrderMap, value)
		elif methodtype == Coder.Player:
			return Coder._dec(Coder.PlayerMap, value)
		elif methodtype == Coder.PropState:
			return Coder._dec(Coder.PropStateMap, value)
		elif methodtype == Coder.Resource:
			return Coder._dec(Coder.ResourceMap, value)
		elif methodtype == Coder.Score:
			return Coder._dec(Coder.ScoreMap, value)
		elif methodtype == Coder.SwitchAction:
			return Coder._dec(Coder.SwitchActionMap, value)
		elif methodtype == Coder.SwitchState:
			return Coder._dec(Coder.SwitchStateMap, value)
		elif methodtype == Coder.AIScript:
			_byte = binio.i2b4(value)
			for string, compressed in AIScriptDict.items():
				if compressed == _byte:
					return "'%s'" % string
			return mapstring2str(value) if value >= 0 else mapstring2str(value+0x100000000)
		elif methodtype == Coder.Count:
			return 'All' if value == 0 else mapstring2str(value)
		elif methodtype == Coder.Property:
			if type(value) is int and starcraftmap:
				res = starcraftmap.DecodeUnitProperty(value)
				if res == None:
					return mapstring2str(value)
				value = res
			return mapstring2str(value, stringize = False)
		elif methodtype == Coder.String:
			if type(value) is int and starcraftmap:
				res = starcraftmap.DecodeString(value)
				if res == None:
					return mapstring2str(value)
				value = res
			return mapstring2str(value)
		elif methodtype == Coder.Location:
			if type(value) is int and starcraftmap:
				res = starcraftmap.DecodeLocation(value)
				if res == None:
					return mapstring2str(value)
				value = res
			return mapstring2str(value)
		elif methodtype == Coder.Unit:
			if type(value) is int and starcraftmap:
				res = starcraftmap.DecodeUnit(value)
				if res == None:
					for unitname, unitid in UnitNameDict.items():
						if unitid == value:
							return mapstring2str(unitname)
				value = res
			return mapstring2str(value)
		elif methodtype == Coder.Switch:
			if type(value) is int and starcraftmap:
				res = starcraftmap.DecodeSwitch(value)
				if res == None:
					return mapstring2str(value)
				value = res
			return mapstring2str(value)
		else:
			raise RuntimeError('Coder : Unknown type on decode')

	@staticmethod
	def _enc(_map, _var):
		if _var in _map[1]:
			return _map[0][_map[1].index(_var)]
		else:
			raise RuntimeError("Coder : Encoding error")

	@staticmethod
	def encode(starcraftmap, methodtype, value):
		if type(value) is int:
			return value
		if methodtype == Coder.Default:
			raise RuntimeError("Coder : Encoding error")
		elif methodtype == Coder.AllyStatus:
			return Coder._enc(Coder.AllyStatusMap, value)
		elif methodtype == Coder.Comparison:
			return Coder._enc(Coder.ComparisonMap, value)
		elif methodtype == Coder.Modifier:
			return Coder._enc(Coder.ModifierMap, value)
		elif methodtype == Coder.Order:
			return Coder._enc(Coder.OrderMap, value)
		elif methodtype == Coder.Player:
			return Coder._enc(Coder.PlayerMap, value)
		elif methodtype == Coder.PropState:
			return Coder._enc(Coder.PropStateMap, value)
		elif methodtype == Coder.Resource:
			return Coder._enc(Coder.ResourceMap, value)
		elif methodtype == Coder.Score:
			return Coder._enc(Coder.ScoreMap, value)
		elif methodtype == Coder.SwitchAction:
			return Coder._enc(Coder.SwitchActionMap, value)
		elif methodtype == Coder.SwitchState:
			return Coder._enc(Coder.SwitchStateMap, value)
		elif methodtype == Coder.AIScript:
			return binio.b2i4(AIScriptDict.get(value, value), 0)
		elif methodtype == Coder.Count:
			if value is All:
				return 0
			else:
				raise RuntimeError("Coder : Encoding error")
		elif methodtype == Coder.Property:
			return starcraftmap.EncodeUnitProperty(value) if starcraftmap else value
		elif methodtype == Coder.String:
			return starcraftmap.EncodeString(value) if starcraftmap else value
		elif methodtype == Coder.Location:
			return starcraftmap.EncodeLocation(value) if starcraftmap else value
		elif methodtype == Coder.Unit:
			if starcraftmap:
				res = starcraftmap.EncodeUnit(value)
				if res == None and value in UnitNameDict:
					return UnitNameDict[value]
				elif type(res) is int:
					return res
			else:
				raise RuntimeError("Coder : Encoding error")
		elif methodtype == Coder.Switch:
			return starcraftmap.EncodeSwitch(value) if starcraftmap else value
		else:
			raise RuntimeError('Coder: Unknown type on encode')


