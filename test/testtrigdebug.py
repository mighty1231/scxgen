import sys
sys.path.append('..\\..') # It is used for only importing scxgen

from scxgen import *

def f():
	Trigger(
		players = [Force1],
		conditions = [
			Deaths(P7, 3, 1, 'Goliath Turret'),
			Deaths(P7, AtLeast, 5, 'Nuclear Missile').Number(5), # raise error
			Deaths(P7, AtMost, 30, 'Nuclear Missile'),
		],
		actions = [DisplayText('\n\n\n\n\x13\x08▷▷   \x0f크리스마스 트리 \x0e지키기   \x08◁◁\n\x13꿈을 빼앗아가려는 어른들을 막아라 !\n\n\n\x13Version 0.1 by Klassical\n\n\n\n')],
		flag = [preserved]
	)
def g():
	f()
mf = MapFile("test_nombrftrig.scx", "result.scx")
mf.LoadMap()
g()
mf.SaveMap()
