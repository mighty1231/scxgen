import sys
sys.path.append('..\\..') # It is used for only importing trggen2

from trggen2 import *

with MapFile("test_nombrftrig.scx", "result.scx") as mapfile:
	Trigger(
		players = [P1, P2],
		conditions = [HighestScore(Kills)],
		actions = [Wait(30)]
	)

with MapFile("result.scx", "result2.scx") as mapfile:
	pass
	