import sys
sys.path.append('..\\..') # It is used for only importing scxgen

from scxgen import *

with MapFile("test_nombrftrig.scx", "intermediate1.scx"):
	pass

with MapFile("test_nombrftrig.scx", "intermediate2.scx"):
	pass

with MapFile("intermediate1.scx", "res1.scx") as mf1:
	MBTrigger(
		players = [Force1],
		actions = [
			MBTextMessage('wef', 4),
			MBTransmission('rtttttttt', 2, 10000, Subtract, 'sound\\Bullet\\TNsFir00.wav', 13131),
			MBWait(341)
		]
	)

	with MapFile("intermediate2.scx", "res2.scx") as mf2:
		Trigger(
			players = [Force1],
			conditions = [
				Deaths(P7, Exactly, 0, 'Goliath Turret'),
				Deaths(P7, AtLeast, 5, 'Nuclear Missile'),
				Deaths(P7, AtMost, 30, 'Nuclear Missile'),
			],
			actions = [DisplayText('hihi hoho')],
			flag = [preserved]
		)
