import sys
sys.path.append('..\\..') # It is used only for importing scxgen

from scxgen import *

with MapFile("test_nombrftrig.scx", "result.scx") as mapfile:
	Trigger(players = [P1],
		conditions = [
			Memory(0x58A340, Exactly, 34),
			Memory(0x58A368, AtLeast, 22),
			Memory().Address(0x58A340).AtLeast(30),
			Deaths().PU(100, 230).AtLeast(50),
			Deaths().PU(-34, 0).AtLeast(50),
			Deaths().PU(24, 54333).AtLeast(50),
			Deaths().PU(4, 4).AtLeast(50),

		],
		actions = [
			SetMemory(0x58A340, SetTo, 34),
			SetMemory(0x58A368, Add, 22),
			SetMemory().Address(0x58A340).Add(30),
			SetDeaths().PU(100, 230).Add(50),
			SetDeaths().PU(-34, 0).Add(50),
			SetDeaths().PU(24, 54333).Add(50),
			SetDeaths().PU(4, 4).Add(50),
		]
		)


with MapFile("result.scx", "result2.scx") as mapfile:
	pass
'''
Trigger.txt would be

Trigger(
	players = [P1],
	conditions = [
		Memory(0x0058A340, Exactly, 34),
		Deaths(P2, AtLeast, 22, 'Terran Marine'),
		Memory(0x0058A340, AtLeast, 30),
		Deaths(100, AtLeast, 50, '(men)'),
		Memory(0x0058A2DC, AtLeast, 50),
		Deaths(24, AtLeast, 50, 54333),
		Deaths(P5, AtLeast, 50, 'Goliath Turret'),
	],
	actions = [
		SetMemory(0x0058A340, SetTo, 34),
		SetDeaths(P2, Add, 22, 'Terran Marine'),
		SetMemory(0x0058A340, Add, 30),
		SetDeaths(100, Add, 50, '(men)'),
		SetMemory(0x0058A2DC, Add, 50),
		SetDeaths(24, Add, 50, 54333),
		SetDeaths(P5, Add, 50, 'Goliath Turret'),
	],
	flag = []
)


'''
