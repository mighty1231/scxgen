import sys
sys.path.append('..\\..') # It is used only for importing scxgen

from scxgen import *

with MapFile("test_nombrftrig.scx", "result.scx") as mf:
	with OnCondition([Deaths(P7, 3, 1, 'Goliath Turret'),
			Deaths(P7, AtLeast, 5, 'Nuclear Missile')]):
		Trigger(
			players = [Force1],
			conditions = [
				Deaths(P7, AtMost, 30, 'Nuclear Missile'),
			],
			actions = [DisplayText('\n\n\n\n\x13\x08▷▷   \x0f크리스마스 트리 \x0e지키기   \x08◁◁\n\x13꿈을 빼앗아가려는 어른들을 막아라 !\n\n\n\x13Version 0.1 by Klassical\n\n\n\n')],
			flag = [preserved]
		)

		Trigger(
			players = [Force1],
			conditions = [
				Deaths(P7, AtMost, 68, 'Nuclear Missile'),
			],
			actions = [SetDeaths().Player(P7).Modifier(SetTo).Number(40).Unit('Nuclear Missile')],
			flag = [preserved]
		)

	Trigger(
		players = [Force1],
		conditions = [

			Deaths(P7, Exactly, 68, 'Nuclear Missile'),
		],
		actions = [SetDeaths().Player(P7).Modifier(SetTo).Number(0).Unit('Nuclear Missile')],
		flag = [preserved]
	)

