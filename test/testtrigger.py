import sys
sys.path.append('..\\..') # It is used for only importing scxgen

from scxgen import *

with MapFile("test_nombrftrig.scx", "result.scx") as mapfile:
	Trigger(
		players = [P1], 
		conditions = [
			Command().PU((P1, 'Terran Marine')).AtLeast(30), # The module would flattening argument
			ElapsedTime(AtMost, 40),
			ElapsedTime().AtLeast(20)
		],
		actions = [
			Order().PU(P1, 'Terran Marine').Move('item_s1', 'item_wall1'),
			SetInvincibility().PU(P1, 'Terran Marine').At('item_s1').Enable()
		])