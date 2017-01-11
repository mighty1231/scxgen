
class _Unique:
	def __init__(self, name):
		self.name = name

	def GetConstName(self):
		return self.name

	def __str__(self):
		return self.name

All                      = _Unique('All')
Enemy                    = _Unique('Enemy')
Ally                     = _Unique('Ally')
AlliedVictory            = _Unique('AlliedVictory')
AtLeast                  = _Unique('AtLeast')
AtMost                   = _Unique('AtMost')
Exactly                  = _Unique('Exactly')
SetTo                    = _Unique('SetTo')
Add                      = _Unique('Add')
Subtract                 = _Unique('Subtract')
Move                     = _Unique('Move')
Patrol                   = _Unique('Patrol')
Attack                   = _Unique('Attack')
P1                       = _Unique('P1')
P2                       = _Unique('P2')
P3                       = _Unique('P3')
P4                       = _Unique('P4')
P5                       = _Unique('P5')
P6                       = _Unique('P6')
P7                       = _Unique('P7')
P8                       = _Unique('P8')
P9                       = _Unique('P9')
P10                      = _Unique('P10')
P11                      = _Unique('P11')
P12                      = _Unique('P12')
Player1                  = _Unique('Player1')
Player2                  = _Unique('Player2')
Player3                  = _Unique('Player3')
Player4                  = _Unique('Player4')
Player5                  = _Unique('Player5')
Player6                  = _Unique('Player6')
Player7                  = _Unique('Player7')
Player8                  = _Unique('Player8')
Player9                  = _Unique('Player9')
Player10                 = _Unique('Player10')
Player11                 = _Unique('Player11')
Player12                 = _Unique('Player12')
CurrentPlayer            = _Unique('CurrentPlayer')
Foes                     = _Unique('Foes')
Allies                   = _Unique('Allies')
NeutralPlayers           = _Unique('NeutralPlayers')
AllPlayers               = _Unique('AllPlayers')
Force1                   = _Unique('Force1')
Force2                   = _Unique('Force2')
Force3                   = _Unique('Force3')
Force4                   = _Unique('Force4')
NonAlliedVictoryPlayers  = _Unique('NonAlliedVictoryPlayers')
Enable                   = _Unique('Enable')
Disable                  = _Unique('Disable')
Toggle                   = _Unique('Toggle')
Ore                      = _Unique('Ore')
Gas                      = _Unique('Gas')
OreAndGas                = _Unique('OreAndGas')
Total                    = _Unique('Total')
Units                    = _Unique('Units')
Buildings                = _Unique('Buildings')
UnitsAndBuildings        = _Unique('UnitsAndBuildings')
# Kills                  = _Unique('# Kills')
Razings                  = _Unique('Razings')
KillsAndRazings          = _Unique('KillsAndRazings')
Custom                   = _Unique('Custom')
Set                      = _Unique('Set')
Clear                    = _Unique('Clear')
Random                   = _Unique('Random')
Cleared                  = _Unique('Cleared')

actexec                  = _Unique('actexec')
preserved                = _Unique('preserved')
disabled                 = _Unique('disabled')

AnyUnit = 229
Men = 230
Buildings = 231
Factories = 232

