import sys
sys.path.append('..\\..') # It is used for only importing scxgen

from scxgen import *

with MapFile("test_nombrftrig.scx", "result.scx") as mapfile:
	Trigger(
		players = [P1, P2],
		conditions = [HighestScore(Kills)],
		actions = [Wait(30)]
	)

with MapFile("result.scx", "result2.scx") as mapfile:
	pass
	