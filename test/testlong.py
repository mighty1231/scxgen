import sys
sys.path.append('..\\..') # It is used for only importing scxgen

from scxgen import *

mf = MapFile("test_nombrftrig.scx", "result.scx")
mf.LoadMap()

Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, AtLeast, 5, 'Nuclear Missile'),
		Deaths(P7, AtMost, 30, 'Nuclear Missile'),
	],
	actions = [DisplayText('\n\n\n\n\x13\x08▷▷   \x0f크리스마스 트리 \x0e지키기   \x08◁◁\n\x13꿈을 빼앗아가려는 어른들을 막아라 !\n\n\n\x13Version 0.7 by Klassical\n\n\n\n')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 30, 'Nuclear Missile'),
	],
	actions = [RunAIScript('Turn ON Shared Vision for Player 7')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 30, 'Nuclear Missile'),
	],
	actions = [
		CreateUnit(6, 'Terran SCV', 'itembox_a1', P7),
		CreateUnit(3, 'Terran Marine', 'itembox_a2', P7),
		CreateUnit(1, 'Terran Vulture', 'itembox_a3', P7),
		CreateUnit(8, 'Protoss Probe', 'itembox_a4', P7),
		CreateUnit(2, 'Protoss Zealot', 'itembox_a5', P7),
		CreateUnit(7, 'Zerg Drone', 'itembox_a6', P7),
		CreateUnit(5, 'Zerg Zergling', 'itembox_a7', P7),
		CreateUnit(3, 'Zerg Hydralisk', 'itembox_a8', P7),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 50, 'Nuclear Missile'),
	],
	actions = [
		CreateUnit(6, 'Terran Marine', 'itembox_b1', P7),
		CreateUnit(2, 'Terran Medic', 'itembox_b1', P7),
		CreateUnit(3, 'Terran Vulture', 'itembox_b2', P7),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'itembox_b2', P7),
		CreateUnit(4, 'Protoss Zealot', 'itembox_b3', P7),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'itembox_b3', P7),
		CreateUnit(2, 'Protoss Dragoon', 'itembox_b4', P7),
		CreateUnit(1, 'Protoss Archon', 'itembox_b4', P7),
		CreateUnit(10, 'Zerg Zergling', 'itembox_b5', P7),
		CreateUnit(1, 'Zerg Ultralisk', 'itembox_b5', P7),
		CreateUnit(6, 'Zerg Hydralisk', 'itembox_b6', P7),
		CreateUnit(2, 'Zerg Lurker', 'itembox_b6', P7),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 70, 'Nuclear Missile'),
	],
	actions = [
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'itembox_c1', P7),
		CreateUnit(4, 'Terran Goliath', 'itembox_c1', P7),
		CreateUnit(1, 'Terran Battlecruiser', 'itembox_c2', P7),
		CreateUnit(5, 'Terran Wraith', 'itembox_c2', P7),
		CreateUnit(3, 'Protoss Archon', 'itembox_c3', P7),
		CreateUnit(1, 'Protoss Reaver', 'itembox_c3', P7),
		CreateUnit(1, 'Protoss Carrier', 'itembox_c4', P7),
		CreateUnit(4, 'Protoss Scout', 'itembox_c4', P7),
		CreateUnit(3, 'Zerg Ultralisk', 'itembox_c5', P7),
		CreateUnit(5, 'Zerg Hydralisk', 'itembox_c5', P7),
		CreateUnit(3, 'Zerg Guardian', 'itembox_c6', P7),
		CreateUnit(5, 'Zerg Mutalisk', 'itembox_c6', P7),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 40, 'Nuclear Missile'),
	],
	actions = [
		DisplayText('\x0f산타로부터 받은 \x08선물 상자\x0f로 트리를 지키세요!'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 100, 'Nuclear Missile'),
	],
	actions = [
		DisplayText('밸런스 조정중인 맵이어요. 참고 ^.~)찡긋'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall4', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall4', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 140, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_centerwall4', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtMost, 51130563, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 51130564, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 102261126, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 102261127, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 153391689, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 153391690, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 204522252, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 204522253, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 255652815, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 255652816, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 306783378, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 306783379, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 357913941, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 357913942, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 409044504, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 409044505, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 460175067, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 460175068, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 511305630, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 511305631, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 562436193, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 562436194, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 613566756, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 613566757, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 664697319, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 664697320, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 766958445, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 766958446, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 818089008, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 818089009, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 869219571, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 869219572, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 920350134, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 920350135, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 971480697, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 971480698, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1022611260, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1022611261, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1124872387, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1124872388, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1176002950, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1176002951, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1227133513, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1227133514, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1278264076, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1278264077, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1329394639, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1329394640, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1380525202, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1380525203, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1482786328, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1482786329, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1533916891, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1533916892, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1585047454, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1585047455, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1636178017, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1636178018, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1687308580, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1687308581, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1738439143, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1738439144, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1789569706, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1789569707, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1840700269, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1840700270, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1891830832, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1891830833, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1942961395, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1942961396, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1994091958, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall2', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 1994091959, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2045222521, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2045222522, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2096353084, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2096353085, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2198614211, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2198614212, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2249744774, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2249744775, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2300875337, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2300875338, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2352005900, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2352005901, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2403136463, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2403136464, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2454267026, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2454267027, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2505397589, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2505397590, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2556528152, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2556528153, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2607658715, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2607658716, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2658789278, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2658789279, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2709919841, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2709919842, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2761050404, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2761050405, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2812180967, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2812180968, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2914442093, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2914442094, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2965572656, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2965572657, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3016703219, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3016703220, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3067833782, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3067833783, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3118964345, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3118964346, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3170094908, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3170094909, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3272356035, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3272356036, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3323486598, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3323486599, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3374617161, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall4', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3374617162, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3425747724, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3425747725, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3476878287, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3476878288, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3528008850, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3528008851, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3630269976, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3630269977, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3681400539, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3681400540, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3732531102, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3732531103, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3783661665, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3783661666, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3834792228, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3834792229, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3885922791, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3885922792, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3937053354, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3937053355, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3988183917, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 3988183918, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4039314480, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 4039314481, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4090445043, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 4090445044, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4141575606, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall6', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 4141575607, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4192706169, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall1', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 4192706170, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4243836732, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall3', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 150, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 4243836733, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', 'item_wall7', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall8', P12),
		KillUnitAt(1, 'Terran Control Tower', 'item_wall5', P12),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 0, 'Goliath Turret'),
		Deaths(P7, Exactly, 160, 'Nuclear Missile'),
	],
	actions = [
		SetDeaths(P7, SetTo, 1, 'Goliath Turret'),
		SetDeaths(P7, SetTo, 0, 'Nuclear Missile'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f1\n\x0f>>> \x0eZerg Zergling \x1030마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [CreateUnit(5, 'Zerg Zergling', 'monstergen1', P8)],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [CreateUnit(5, 'Zerg Zergling', 'monstergen2', P8)],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [CreateUnit(5, 'Zerg Zergling', 'monstergen3', P8)],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [CreateUnit(5, 'Zerg Zergling', 'monstergen4', P8)],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [CreateUnit(5, 'Zerg Zergling', 'monstergen5', P8)],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [CreateUnit(5, 'Zerg Zergling', 'monstergen6', P8)],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f2\n\x0f>>> \x0eZerg Zergling \x1080마리\n\x0f>>> \x0eZerg Hydralisk \x1020마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(13, 'Zerg Zergling', 'monstergen1', P8),
		CreateUnit(3, 'Zerg Hydralisk', 'monstergen1', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(13, 'Zerg Zergling', 'monstergen2', P8),
		CreateUnit(3, 'Zerg Hydralisk', 'monstergen2', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(14, 'Zerg Zergling', 'monstergen3', P8),
		CreateUnit(4, 'Zerg Hydralisk', 'monstergen3', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(13, 'Zerg Zergling', 'monstergen4', P8),
		CreateUnit(3, 'Zerg Hydralisk', 'monstergen4', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(13, 'Zerg Zergling', 'monstergen5', P8),
		CreateUnit(3, 'Zerg Hydralisk', 'monstergen5', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(14, 'Zerg Zergling', 'monstergen6', P8),
		CreateUnit(4, 'Zerg Hydralisk', 'monstergen6', P8),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f3\n\x0f>>> \x0eZerg Zergling \x10150마리\n\x0f>>> \x0eZerg Hydralisk \x1040마리\n\x0f>>> \x0eZerg Mutalisk \x1040마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(25, 'Zerg Zergling', 'monstergen1', P8),
		CreateUnit(6, 'Zerg Hydralisk', 'monstergen1', P8),
		CreateUnit(6, 'Zerg Mutalisk', 'monstergen1', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(25, 'Zerg Zergling', 'monstergen2', P8),
		CreateUnit(7, 'Zerg Hydralisk', 'monstergen2', P8),
		CreateUnit(7, 'Zerg Mutalisk', 'monstergen2', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(25, 'Zerg Zergling', 'monstergen3', P8),
		CreateUnit(7, 'Zerg Hydralisk', 'monstergen3', P8),
		CreateUnit(7, 'Zerg Mutalisk', 'monstergen3', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(25, 'Zerg Zergling', 'monstergen4', P8),
		CreateUnit(6, 'Zerg Hydralisk', 'monstergen4', P8),
		CreateUnit(6, 'Zerg Mutalisk', 'monstergen4', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(25, 'Zerg Zergling', 'monstergen5', P8),
		CreateUnit(7, 'Zerg Hydralisk', 'monstergen5', P8),
		CreateUnit(7, 'Zerg Mutalisk', 'monstergen5', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(25, 'Zerg Zergling', 'monstergen6', P8),
		CreateUnit(7, 'Zerg Hydralisk', 'monstergen6', P8),
		CreateUnit(7, 'Zerg Mutalisk', 'monstergen6', P8),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f4\n\x0f>>> \x0eProtoss Zealot \x10100마리\n\x0f>>> \x0eProtoss Dragoon \x1030마리\n\x0f>>> \x0eProtoss Archon \x1015마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(16, 'Protoss Zealot', 'monstergen1', P8),
		CreateUnit(5, 'Protoss Dragoon', 'monstergen1', P8),
		CreateUnit(2, 'Protoss Archon', 'monstergen1', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(17, 'Protoss Zealot', 'monstergen2', P8),
		CreateUnit(5, 'Protoss Dragoon', 'monstergen2', P8),
		CreateUnit(3, 'Protoss Archon', 'monstergen2', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(17, 'Protoss Zealot', 'monstergen3', P8),
		CreateUnit(5, 'Protoss Dragoon', 'monstergen3', P8),
		CreateUnit(2, 'Protoss Archon', 'monstergen3', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(16, 'Protoss Zealot', 'monstergen4', P8),
		CreateUnit(5, 'Protoss Dragoon', 'monstergen4', P8),
		CreateUnit(3, 'Protoss Archon', 'monstergen4', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(17, 'Protoss Zealot', 'monstergen5', P8),
		CreateUnit(5, 'Protoss Dragoon', 'monstergen5', P8),
		CreateUnit(2, 'Protoss Archon', 'monstergen5', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(17, 'Protoss Zealot', 'monstergen6', P8),
		CreateUnit(5, 'Protoss Dragoon', 'monstergen6', P8),
		CreateUnit(3, 'Protoss Archon', 'monstergen6', P8),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f5\n\x0f>>> \x0eFenix (Zealot) \x1030마리\n\x0f>>> \x0eProtoss Archon \x1030마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(5, 'Fenix (Zealot)', 'monstergen1', P8),
		CreateUnit(5, 'Protoss Archon', 'monstergen1', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(5, 'Fenix (Zealot)', 'monstergen2', P8),
		CreateUnit(5, 'Protoss Archon', 'monstergen2', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(5, 'Fenix (Zealot)', 'monstergen3', P8),
		CreateUnit(5, 'Protoss Archon', 'monstergen3', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(5, 'Fenix (Zealot)', 'monstergen4', P8),
		CreateUnit(5, 'Protoss Archon', 'monstergen4', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(5, 'Fenix (Zealot)', 'monstergen5', P8),
		CreateUnit(5, 'Protoss Archon', 'monstergen5', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(5, 'Fenix (Zealot)', 'monstergen6', P8),
		CreateUnit(5, 'Protoss Archon', 'monstergen6', P8),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Final Round\n\x0f>>> \x0eFenix (Zealot) \x1050마리\n\x0f>>> \x0eTassadar/Zeratul (Archon) \x1015마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(8, 'Fenix (Zealot)', 'monstergen1', P8),
		CreateUnit(2, 'Tassadar/Zeratul (Archon)', 'monstergen1', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(8, 'Fenix (Zealot)', 'monstergen2', P8),
		CreateUnit(3, 'Tassadar/Zeratul (Archon)', 'monstergen2', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(9, 'Fenix (Zealot)', 'monstergen3', P8),
		CreateUnit(2, 'Tassadar/Zeratul (Archon)', 'monstergen3', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(8, 'Fenix (Zealot)', 'monstergen4', P8),
		CreateUnit(3, 'Tassadar/Zeratul (Archon)', 'monstergen4', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(8, 'Fenix (Zealot)', 'monstergen5', P8),
		CreateUnit(2, 'Tassadar/Zeratul (Archon)', 'monstergen5', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		CreateUnit(9, 'Fenix (Zealot)', 'monstergen6', P8),
		CreateUnit(3, 'Tassadar/Zeratul (Archon)', 'monstergen6', P8),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(32, Random),
		SetSwitch(33, Random),
		SetSwitch(34, Random),
		SetSwitch(35, Random),
		SetSwitch(36, Random),
		SetDeaths(P7, SetTo, 0, 'Siege Tank Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Cleared),
		Switch(34, Cleared),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa1-1', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Cleared),
		Switch(34, Cleared),
	],
	actions = [
		CenterView('santa1-1'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Cleared),
		Switch(34, Set),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa1-2', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Cleared),
		Switch(34, Set),
	],
	actions = [
		CenterView('santa1-2'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Set),
		Switch(34, Cleared),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa1-3', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Set),
		Switch(34, Cleared),
	],
	actions = [
		CenterView('santa1-3'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Set),
		Switch(34, Set),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa1-4', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(33, Set),
		Switch(34, Set),
	],
	actions = [
		CenterView('santa1-4'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Cleared),
		Switch(34, Cleared),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa2-1', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Cleared),
		Switch(34, Cleared),
	],
	actions = [
		CenterView('santa2-1'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Cleared),
		Switch(34, Set),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa2-2', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Cleared),
		Switch(34, Set),
	],
	actions = [
		CenterView('santa2-2'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Set),
		Switch(34, Cleared),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa2-3', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Set),
		Switch(34, Cleared),
	],
	actions = [
		CenterView('santa2-3'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Set),
		Switch(34, Set),
	],
	actions = [CreateUnit(1, 'Terran Dropship', 'santa2-4', P7)],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(33, Set),
		Switch(34, Set),
	],
	actions = [
		CenterView('santa2-4'),
		PlayWAV('staredit\wav\jinglebell.wav'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(35, Cleared),
		Switch(36, Cleared),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa2-1')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(35, Cleared),
		Switch(36, Set),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa2-2')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(35, Set),
		Switch(36, Cleared),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa2-3')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Cleared),
		Switch(35, Set),
		Switch(36, Set),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa2-4')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(35, Cleared),
		Switch(36, Cleared),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa1-1')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(35, Cleared),
		Switch(36, Set),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa1-2')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(35, Set),
		Switch(36, Cleared),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa1-3')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(32, Set),
		Switch(35, Set),
		Switch(36, Set),
	],
	actions = [Order('Terran Dropship', P7, 'Anywhere', Move, 'santa1-4')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_w1'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_w1'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 15, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_w1'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_n1'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_n1'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 23, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_n1'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_e1'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_e1'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 31, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_e1'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_s1'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_s1'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 39, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_s1'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 47, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Valkyrie', '2by2', P7),
		Order('Terran Valkyrie', P7, 'itemfield', Move, 'item_nw'),
		Wait(0),
		GiveUnits(1, 'Terran Valkyrie', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_w2'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_w2'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 55, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_w2'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_n2'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_n2'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 63, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_n2'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_e2'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_e2'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 71, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_e2'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_s2'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_s2'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 79, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_s2'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 87, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Valkyrie', '2by2', P7),
		Order('Terran Valkyrie', P7, 'itemfield', Move, 'item_ne'),
		Wait(0),
		GiveUnits(1, 'Terran Valkyrie', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_w3'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_w3'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 95, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_w3'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_n3'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_n3'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 103, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_n3'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_e3'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_e3'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 111, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_e3'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_s3'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_s3'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 119, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_s3'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 127, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Valkyrie', '2by2', P7),
		Order('Terran Valkyrie', P7, 'itemfield', Move, 'item_se'),
		Wait(0),
		GiveUnits(1, 'Terran Valkyrie', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_w4'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_w4'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 135, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_w4'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_n4'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_n4'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 143, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_n4'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_e4'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_e4'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 151, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_e4'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Protoss Scout', '2by2', P7),
		Order('Protoss Scout', P7, 'itemfield', Move, 'item_s4'),
		Wait(0),
		GiveUnits(1, 'Protoss Scout', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Zerg Scourge', '2by2', P7),
		Order('Zerg Scourge', P7, 'itemfield', Move, 'item_s4'),
		Wait(0),
		GiveUnits(1, 'Zerg Scourge', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 159, 'Nuclear Missile'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, Exactly, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Science Vessel', '2by2', P7),
		Order('Terran Science Vessel', P7, 'itemfield', Move, 'item_s4'),
		Wait(0),
		GiveUnits(1, 'Terran Science Vessel', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 167, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Dropship', P7, 'itemfield'),
		CreateUnit(1, 'Terran Valkyrie', '2by2', P7),
		Order('Terran Valkyrie', P7, 'itemfield', Move, 'item_sw'),
		Wait(0),
		GiveUnits(1, 'Terran Valkyrie', P7, 'itemfield', P9),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, '(men)', 'item_w1'),
		Bring(P9, Exactly, 1, '(men)', 'item_w2'),
		Bring(P9, Exactly, 1, '(men)', 'item_w3'),
		Bring(P9, Exactly, 1, '(men)', 'item_w4'),
		Bring(P9, Exactly, 1, '(men)', 'item_n1'),
		Bring(P9, Exactly, 1, '(men)', 'item_n2'),
		Bring(P9, Exactly, 1, '(men)', 'item_n3'),
		Bring(P9, Exactly, 1, '(men)', 'item_n4'),
		Bring(P9, Exactly, 1, '(men)', 'item_nw'),
		Bring(P9, Exactly, 1, '(men)', 'item_ne'),
		Bring(P9, Exactly, 1, '(men)', 'item_se'),
		Bring(P9, Exactly, 1, '(men)', 'item_sw'),
	],
	actions = [SetDeaths(P7, SetTo, 1, 'Siege Tank Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, '(men)', 'item_e1'),
		Bring(P9, Exactly, 1, '(men)', 'item_e2'),
		Bring(P9, Exactly, 1, '(men)', 'item_e3'),
		Bring(P9, Exactly, 1, '(men)', 'item_e4'),
		Bring(P9, Exactly, 1, '(men)', 'item_s1'),
		Bring(P9, Exactly, 1, '(men)', 'item_s2'),
		Bring(P9, Exactly, 1, '(men)', 'item_s3'),
		Bring(P9, Exactly, 1, '(men)', 'item_s4'),
	],
	actions = [SetDeaths(P7, SetTo, 2, 'Siege Tank Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 2, 'Siege Tank Turret (Siege Mode)'),
	],
	actions = [SetDeaths(P7, Add, 1, 'Siege Tank Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtMost, 1, 'Siege Tank Turret (Siege Mode)'),
	],
	actions = [SetDeaths(P7, SetTo, 0, 'Siege Tank Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, Exactly, 40, 'Siege Tank Turret (Siege Mode)'),
	],
	actions = [
		KillUnit('Terran Dropship', P7),
		MoveUnit(1, '(men)', P9, 'item_w1', 'item_w1'),
		MoveUnit(1, '(men)', P9, 'item_w2', 'item_w2'),
		MoveUnit(1, '(men)', P9, 'item_w3', 'item_w3'),
		MoveUnit(1, '(men)', P9, 'item_w4', 'item_w4'),
		MoveUnit(1, '(men)', P9, 'item_n1', 'item_n1'),
		MoveUnit(1, '(men)', P9, 'item_n2', 'item_n2'),
		MoveUnit(1, '(men)', P9, 'item_n3', 'item_n3'),
		MoveUnit(1, '(men)', P9, 'item_n4', 'item_n4'),
		MoveUnit(1, '(men)', P9, 'item_e1', 'item_e1'),
		MoveUnit(1, '(men)', P9, 'item_e2', 'item_e2'),
		MoveUnit(1, '(men)', P9, 'item_e3', 'item_e3'),
		MoveUnit(1, '(men)', P9, 'item_e4', 'item_e4'),
		MoveUnit(1, '(men)', P9, 'item_s1', 'item_s1'),
		MoveUnit(1, '(men)', P9, 'item_s2', 'item_s2'),
		MoveUnit(1, '(men)', P9, 'item_s3', 'item_s3'),
		MoveUnit(1, '(men)', P9, 'item_s4', 'item_s4'),
		MoveUnit(1, '(men)', P9, 'item_nw', 'item_nw'),
		MoveUnit(1, '(men)', P9, 'item_ne', 'item_ne'),
		MoveUnit(1, '(men)', P9, 'item_se', 'item_se'),
		MoveUnit(1, '(men)', P9, 'item_sw', 'item_sw'),
		CreateUnit(3, '상급상자', 'item_nn', P7),
		CreateUnit(3, '상급상자', 'item_ss', P7),
		CreateUnit(3, '상급상자', 'item_ee', P7),
		CreateUnit(3, '상급상자', 'item_ww', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Command(P9, AtLeast, 1, '(men)'),
	],
	actions = [MoveLocation('2by2', '(men)', P9, 'itemfield')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Zerg Scourge', '2by2'),
	],
	actions = [
		RemoveUnitAt(1, 'Zerg Scourge', '2by2', P9),
		CreateUnit(1, '하급상자', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Protoss Scout', '2by2'),
	],
	actions = [
		RemoveUnitAt(1, 'Protoss Scout', '2by2', P9),
		CreateUnit(1, '중급상자', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Science Vessel', '2by2'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Science Vessel', '2by2', P9),
		CreateUnit(1, '상급상자', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtMost, 330382099, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Magellan (Science Vessel)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 330382100, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 660764199, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Tassadar/Zeratul (Archon)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 660764200, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 991146299, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Tassadar (Templar)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 991146300, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1321528398, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Infested Kerrigan (Infested Terran)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 1321528399, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1651910498, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Unclean One (Defiler)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 1651910499, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1982292598, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Gantrithor (Carrier)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 1982292599, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2312674697, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Infested Duran (Infested Terran)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 2312674698, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2643056797, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Gui Montag (Firebat)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 2643056798, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2973438897, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Alan Schezar (Goliath)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 2973438898, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3303820996, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Torrasque (Ultralisk)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 3303820997, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3634203096, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Protoss Dark Archon', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 3634203097, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3964585196, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Fenix (Zealot)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Bring(P9, Exactly, 1, 'Terran Valkyrie', '2by2'),
		Deaths(P7, AtLeast, 3964585197, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Valkyrie', '2by2', P9),
		CreateUnit(1, 'Fenix (Dragoon)', '2by2', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 1, 'Goliath Turret'),
		Deaths(P7, AtLeast, 40, 'Siege Tank Turret (Siege Mode)'),
		Command(P9, Exactly, 0, '(men)'),
	],
	actions = [
		SetDeaths(P7, SetTo, 2, 'Goliath Turret'),
		SetDeaths(P7, SetTo, 0, 'Nuclear Missile'),
		SetDeaths(P7, SetTo, 0, 'Scanner Sweep'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, Exactly, 1, 'Goliath Turret'),
	],
	actions = [
		DisplayText('\n\n\x13\x03가방 수용량 현재 \x08(1/3)\n\x13\x04중앙지점으로 돌아가야 상자를 뜯을 수 있습니다.\n\n'),
		PlayWAV('sound\Bullet\ZLrkFir2.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, Exactly, 2, 'Goliath Turret'),
	],
	actions = [
		DisplayText('\n\n\x13\x03가방 수용량 현재 \x08(2/3)\n\x13\x03더이상 중급 이상의 상자를 획득할 수 없습니다\n\x13\x04중앙지점으로 돌아가야 상자를 뜯을 수 있습니다.\n\n'),
		PlayWAV('sound\Bullet\ZLrkFir2.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, Exactly, 3, 'Goliath Turret'),
	],
	actions = [
		DisplayText('\n\n\x13\x03가방 수용량 현재 \x08(3/3)\n\x13\x03더이상 상자를 획득할 수 없습니다\n\x13\x04중앙지점으로 돌아가야 상자를 뜯을 수 있습니다.\n\n'),
		PlayWAV('sound\Misc\PError.WAV'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 10),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\n\n\x13\x11시간이 얼마 남지 않았습니다.\n\x13\x07중앙지점으로 돌아오세요!\n\n'),
		PlayWAV('sound\Misc\Door\Door2Opn.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 10),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\n\n\x13\x11시간이 얼마 남지 않았습니다.\n\x13\x07중앙지점으로 돌아오세요!\n\n'),
		PlayWAV('sound\Misc\Door\Door2Opn.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 10),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\n\n\x13\x11시간이 얼마 남지 않았습니다.\n\x13\x07중앙지점으로 돌아오세요!\n\n'),
		PlayWAV('sound\Misc\Door\Door2Opn.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 10),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\n\n\x13\x11시간이 얼마 남지 않았습니다.\n\x13\x07중앙지점으로 돌아오세요!\n\n'),
		PlayWAV('sound\Misc\Door\Door2Opn.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 10),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\n\n\x13\x11시간이 얼마 남지 않았습니다.\n\x13\x07중앙지점으로 돌아오세요!\n\n'),
		PlayWAV('sound\Misc\Door\Door2Opn.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 10),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\n\n\x13\x11시간이 얼마 남지 않았습니다.\n\x13\x07중앙지점으로 돌아오세요!\n\n'),
		PlayWAV('sound\Misc\Door\Door2Opn.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Terran Civilian', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 35),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Terran Civilian', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 50),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Terran Civilian', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 65),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Terran Civilian', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 80),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Terran Civilian', CurrentPlayer, 'itemfield'),
		Order('Protoss Observer', CurrentPlayer, 'Anywhere', Move, '2by2'),
		MoveUnit(1, 'Magellan (Science Vessel)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Tassadar/Zeratul (Archon)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Tassadar (Templar)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Infested Kerrigan (Infested Terran)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Unclean One (Defiler)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Gantrithor (Carrier)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Infested Duran (Infested Terran)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Gui Montag (Firebat)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Alan Schezar (Goliath)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Torrasque (Ultralisk)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Protoss Dark Archon', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Fenix (Zealot)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Fenix (Dragoon)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Zerg Hydralisk', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 35),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Zerg Hydralisk', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 50),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Zerg Hydralisk', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 65),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Zerg Hydralisk', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 80),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Zerg Hydralisk', CurrentPlayer, 'itemfield'),
		Order('Protoss Observer', CurrentPlayer, 'Anywhere', Move, '2by2'),
		MoveUnit(1, 'Magellan (Science Vessel)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Tassadar/Zeratul (Archon)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Tassadar (Templar)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Infested Kerrigan (Infested Terran)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Unclean One (Defiler)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Gantrithor (Carrier)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Infested Duran (Infested Terran)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Gui Montag (Firebat)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Alan Schezar (Goliath)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Torrasque (Ultralisk)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Protoss Dark Archon', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Fenix (Zealot)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Fenix (Dragoon)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Devouring One (Zergling)', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 35),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Devouring One (Zergling)', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 50),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Devouring One (Zergling)', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 65),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Alan Schezar Turret'),
	],
	actions = [
		CreateUnit(1, 'Devouring One (Zergling)', 'item_center', CurrentPlayer),
		CenterView('item_center'),
		DisplayText('\n\x13\x10달리세요!\n\x13\x03산타의 선물 상자가 기다리고있습니다!\n'),
		PlayWAV('sound\Bullet\TNsFir00.wav'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		SetCountdownTimer(SetTo, 80),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
	],
	actions = [
		MoveLocation('2by2', 'Devouring One (Zergling)', CurrentPlayer, 'itemfield'),
		Order('Protoss Observer', CurrentPlayer, 'Anywhere', Move, '2by2'),
		MoveUnit(1, 'Magellan (Science Vessel)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Tassadar/Zeratul (Archon)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Tassadar (Templar)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Infested Kerrigan (Infested Terran)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Unclean One (Defiler)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Gantrithor (Carrier)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Infested Duran (Infested Terran)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Gui Montag (Firebat)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Alan Schezar (Goliath)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Torrasque (Ultralisk)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Protoss Dark Archon', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Fenix (Zealot)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
		MoveUnit(1, 'Fenix (Dragoon)', CurrentPlayer, 'itemfield', 'unitwarp_base'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '하급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 2, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', '2by2', P7),
		CreateUnit(1, '하급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 1, 'Goliath Turret'),
		CreateUnit(1, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '중급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 1, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', '2by2', P7),
		CreateUnit(1, '중급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 2, 'Goliath Turret'),
		CreateUnit(2, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '상급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 0, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', '2by2', P7),
		CreateUnit(1, '상급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '(men)', '2by2'),
		Deaths(CurrentPlayer, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 0, 'Goliath Turret'),
	],
	actions = [
		GiveUnits(1, '(men)', P7, '2by2', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '하급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 3, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', '2by2', P7),
		CreateUnit(1, '하급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 1, 'Goliath Turret'),
		CreateUnit(1, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '중급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 2, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', '2by2', P7),
		CreateUnit(1, '중급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 2, 'Goliath Turret'),
		CreateUnit(2, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '상급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 1, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', '2by2', P7),
		CreateUnit(1, '상급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '(men)', '2by2'),
		Deaths(CurrentPlayer, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 1, 'Goliath Turret'),
	],
	actions = [
		GiveUnits(1, '(men)', P7, '2by2', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '하급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 4, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', '2by2', P7),
		CreateUnit(1, '하급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 1, 'Goliath Turret'),
		CreateUnit(1, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '중급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 3, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', '2by2', P7),
		CreateUnit(1, '중급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 2, 'Goliath Turret'),
		CreateUnit(2, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '상급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 2, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', '2by2', P7),
		CreateUnit(1, '상급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '(men)', '2by2'),
		Deaths(CurrentPlayer, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 2, 'Goliath Turret'),
	],
	actions = [
		GiveUnits(1, '(men)', P7, '2by2', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '하급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 5, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', '2by2', P7),
		CreateUnit(1, '하급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 1, 'Goliath Turret'),
		CreateUnit(1, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '중급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 4, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', '2by2', P7),
		CreateUnit(1, '중급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 2, 'Goliath Turret'),
		CreateUnit(2, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '상급상자', '2by2'),
		Deaths(CurrentPlayer, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 3, 'Goliath Turret'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', '2by2', P7),
		CreateUnit(1, '상급상자', 'unitwarp_base', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P7, AtLeast, 1, '(men)', '2by2'),
		Deaths(CurrentPlayer, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
		Deaths(CurrentPlayer, AtMost, 3, 'Goliath Turret'),
	],
	actions = [
		GiveUnits(1, '(men)', P7, '2by2', CurrentPlayer),
		SetDeaths(CurrentPlayer, Add, 3, 'Goliath Turret'),
		CreateUnit(3, 'Protoss Observer', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
	],
	actions = [
		SetDeaths(P7, SetTo, 1, 'Scanner Sweep'),
		DisplayText('\x13\x04파밍 종료!'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtMost, 53024287, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Marine', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Marine'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 53024288, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 106048575, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Ghost', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Ghost'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 106048576, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 159072862, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Vulture', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Vulture'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 159072863, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 212097150, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Goliath', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Goliath'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 212097151, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 265121438, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Siege Tank'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 265121439, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 318145725, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran SCV', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran SCV'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 318145726, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 371170013, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Wraith', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Wraith'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 371170014, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 424194300, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Science Vessel', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Science Vessel'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 424194301, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 477218588, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Gui Montag (Firebat)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cGui Montag'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 477218589, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 530242876, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Dropship', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Dropship'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 530242877, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 583267163, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Battlecruiser'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 583267164, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 636291451, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Civilian', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Civilian'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 636291452, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 689315738, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Sarah Kerrigan (Ghost)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cSarah Kerrigan'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 689315739, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 742340026, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Alan Schezar (Goliath)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cAlan Schezar'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 742340027, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 795364314, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Jim Raynor (Vulture)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cJim Raynor'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 795364315, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 848388601, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Jim Raynor (Marine)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cJim Raynor'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 848388602, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 901412889, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Tom Kazansky (Wraith)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTom Kazansky'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 901412890, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 954437176, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Magellan (Science Vessel)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cMagellan'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 954437177, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1007461464, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Edmund Duke (Tank Mode)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cEdmund Duke'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1007461465, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1060485752, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Hyperion (Battlecruiser)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cHyperion'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1060485753, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1113510039, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Norad II (Battlecruiser)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cNorad II'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1113510040, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1166534327, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Firebat', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Firebat'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1166534328, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1219558614, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Medic', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Medic'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1219558615, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1272582902, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Zergling', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Zergling'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1272582903, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1325607190, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Hydralisk', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Hydralisk'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1325607191, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1378631477, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Ultralisk'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1378631478, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Broodling', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Broodling'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1484680052, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Drone', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Drone'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1484680053, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1537704340, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Overlord', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Overlord'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1537704341, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1590728628, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Mutalisk', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Mutalisk'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1590728629, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1643752915, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Guardian', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Guardian'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1643752916, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1696777203, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Queen', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Queen'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1696777204, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1749801490, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Defiler', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Defiler'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1749801491, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1802825778, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Scourge', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Scourge'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1802825779, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1855850066, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Torrasque (Ultralisk)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTorrasque'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1855850067, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1908874353, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Matriarch (Queen)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cMatriarch'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1908874354, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1961898641, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Infested Terran', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cInfested Terran'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 1961898642, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2014922928, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Infested Kerrigan (Infested Terran)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cInfested Kerrigan'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2014922929, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2067947216, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Unclean One (Defiler)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cUnclean One'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2067947217, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2120971504, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Hunter Killer (Hydralisk)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cHunter Killer'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2120971505, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2173995791, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Devouring One (Zergling)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cDevouring One'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2173995792, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2227020079, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Kukulza (Mutalisk)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cKukulza'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2227020080, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2280044367, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Kukulza (Guardian)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cKukulza'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2280044368, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2333068654, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Yggdrasill (Overlord)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cYggdrasill'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2333068655, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2386092942, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Terran Valkyrie', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTerran Valkyrie'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2386092943, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2439117229, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Corsair', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Corsair'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2439117230, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2492141517, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Dark Templar (Unit)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Dark Templar'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2492141518, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2545165805, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Devourer', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Devourer'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2545165806, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2598190092, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Dark Archon', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Dark Archon'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2598190093, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2651214380, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Probe', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Probe'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2651214381, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2704238667, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Zealot', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Zealot'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2704238668, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2757262955, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Dragoon', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Dragoon'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2757262956, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2810287243, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss High Templar', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss High Templar'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2810287244, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Archon', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Archon'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2916335818, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Shuttle', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Shuttle'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2916335819, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2969360105, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Scout', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Scout'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 2969360106, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3022384393, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Arbiter', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Arbiter'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3022384394, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3075408681, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Carrier'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3075408682, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3128432968, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Dark Templar (Hero)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Dark Templar'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3128432969, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3181457256, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zeratul (Dark Templar)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZeratul'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3181457257, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3234481543, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Tassadar/Zeratul (Archon)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTassadar/Zeratul'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3234481544, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3287505831, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Fenix (Zealot)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cFenix'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3287505832, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3340530119, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Fenix (Dragoon)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cFenix'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3340530120, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3393554406, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Tassadar (Templar)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cTassadar'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3393554407, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3446578694, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Mojo (Scout)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cMojo'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3446578695, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3499602981, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Warbringer (Reaver)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cWarbringer'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3499602982, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3552627269, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Gantrithor (Carrier)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cGantrithor'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3552627270, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3605651557, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Reaver'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3605651558, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3658675844, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Protoss Observer', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cProtoss Observer'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3658675845, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3711700132, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Danimoth (Arbiter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cDanimoth'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3711700133, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3764724419, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Artanis (Scout)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cArtanis'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3764724420, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3817748707, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Rhynadon (Badlands Critter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cRhynadon'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3817748708, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3870772995, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Bengalaas (Jungle Critter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cBengalaas'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3870772996, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3923797282, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Scantid (Desert Critter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cScantid'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3923797283, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3976821570, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Kakaru (Twilight Critter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cKakaru'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 3976821571, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4029845857, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Ragnasaur (Ashworld Critter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cRagnasaur'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 4029845858, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4082870145, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Ursadon (Ice World Critter)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cUrsadon'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 4082870146, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4135894433, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Samir Duran (Ghost)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cSamir Duran'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 4135894434, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4188918720, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Alexei Stukov (Ghost)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cAlexei Stukov'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 4188918721, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 4241943008, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Zerg Lurker', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cZerg Lurker'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
		Bring(CurrentPlayer, AtLeast, 1, '(men)', 'item_center'),
		Deaths(P7, AtLeast, 4241943009, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		CreateUnit(1, 'Infested Duran (Infested Terran)', 'unitwarp_base', CurrentPlayer),
		DisplayText('\x13\x03원점 복귀 \x07보너스 유닛 \x03획득!'),
		DisplayText('\x13\x1cInfested Duran'),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Bring(P1, Exactly, 1, 'Terran Civilian', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P1, 'unitwarp_base', 'unitwarp_p1'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Bring(P1, Exactly, 1, 'Zerg Hydralisk', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P1, 'unitwarp_base', 'unitwarp_p1'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Bring(P1, Exactly, 1, 'Devouring One (Zergling)', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P1, 'unitwarp_base', 'unitwarp_p1'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtMost, 536870912, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(6, 'Terran SCV', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 536870913, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Terran Marine', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1610612736, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(1, 'Terran Vulture', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 1610612737, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(8, 'Protoss Probe', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2684354560, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(2, 'Protoss Zealot', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 2684354561, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(7, 'Zerg Drone', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3758096384, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(5, 'Zerg Zergling', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '하급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 3758096385, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Zerg Hydralisk', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p1', P1),
		CreateUnit(6, 'Terran Marine', 'unitwarp_p1', P1),
		CreateUnit(2, 'Terran Medic', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Terran Vulture', 'unitwarp_p1', P1),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p1', P1),
		CreateUnit(4, 'Protoss Zealot', 'unitwarp_p1', P1),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p1', P1),
		CreateUnit(2, 'Protoss Dragoon', 'unitwarp_p1', P1),
		CreateUnit(1, 'Protoss Archon', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p1', P1),
		CreateUnit(10, 'Zerg Zergling', 'unitwarp_p1', P1),
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '중급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p1', P1),
		CreateUnit(6, 'Zerg Hydralisk', 'unitwarp_p1', P1),
		CreateUnit(2, 'Zerg Lurker', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p1', P1),
		CreateUnit(4, 'Terran Goliath', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p1', P1),
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_p1', P1),
		CreateUnit(5, 'Terran Wraith', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Protoss Archon', 'unitwarp_p1', P1),
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p1', P1),
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_p1', P1),
		CreateUnit(4, 'Protoss Scout', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Zerg Ultralisk', 'unitwarp_p1', P1),
		CreateUnit(5, 'Zerg Hydralisk', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P1, AtLeast, 1, '상급상자', 'unitwarp_p1'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p1', P1),
		CreateUnit(3, 'Zerg Guardian', 'unitwarp_p1', P1),
		CreateUnit(5, 'Zerg Mutalisk', 'unitwarp_p1', P1),
	],
	flag = [preserved]
)
Trigger(
	players = [P1],
	conditions = [Always()],
	actions = [
		ModifyUnitEnergy(All, '(men)', P1, 'unitwarp_p1', 100),
		MoveUnit(All, '(men)', P1, 'unitwarp_p1', 'unitgen_p1'),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Bring(P2, Exactly, 1, 'Terran Civilian', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P2, 'unitwarp_base', 'unitwarp_p2'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Bring(P2, Exactly, 1, 'Zerg Hydralisk', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P2, 'unitwarp_base', 'unitwarp_p2'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Bring(P2, Exactly, 1, 'Devouring One (Zergling)', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P2, 'unitwarp_base', 'unitwarp_p2'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtMost, 536870912, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(6, 'Terran SCV', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 536870913, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Terran Marine', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1610612736, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(1, 'Terran Vulture', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 1610612737, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(8, 'Protoss Probe', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2684354560, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(2, 'Protoss Zealot', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 2684354561, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(7, 'Zerg Drone', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3758096384, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(5, 'Zerg Zergling', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '하급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 3758096385, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Zerg Hydralisk', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p2', P2),
		CreateUnit(6, 'Terran Marine', 'unitwarp_p2', P2),
		CreateUnit(2, 'Terran Medic', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Terran Vulture', 'unitwarp_p2', P2),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p2', P2),
		CreateUnit(4, 'Protoss Zealot', 'unitwarp_p2', P2),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p2', P2),
		CreateUnit(2, 'Protoss Dragoon', 'unitwarp_p2', P2),
		CreateUnit(1, 'Protoss Archon', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p2', P2),
		CreateUnit(10, 'Zerg Zergling', 'unitwarp_p2', P2),
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '중급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p2', P2),
		CreateUnit(6, 'Zerg Hydralisk', 'unitwarp_p2', P2),
		CreateUnit(2, 'Zerg Lurker', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p2', P2),
		CreateUnit(4, 'Terran Goliath', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p2', P2),
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_p2', P2),
		CreateUnit(5, 'Terran Wraith', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Protoss Archon', 'unitwarp_p2', P2),
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p2', P2),
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_p2', P2),
		CreateUnit(4, 'Protoss Scout', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Zerg Ultralisk', 'unitwarp_p2', P2),
		CreateUnit(5, 'Zerg Hydralisk', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P2, AtLeast, 1, '상급상자', 'unitwarp_p2'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p2', P2),
		CreateUnit(3, 'Zerg Guardian', 'unitwarp_p2', P2),
		CreateUnit(5, 'Zerg Mutalisk', 'unitwarp_p2', P2),
	],
	flag = [preserved]
)
Trigger(
	players = [P2],
	conditions = [Always()],
	actions = [
		ModifyUnitEnergy(All, '(men)', P2, 'unitwarp_p2', 100),
		MoveUnit(All, '(men)', P2, 'unitwarp_p2', 'unitgen_p2'),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Bring(P3, Exactly, 1, 'Terran Civilian', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P3, 'unitwarp_base', 'unitwarp_p3'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Bring(P3, Exactly, 1, 'Zerg Hydralisk', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P3, 'unitwarp_base', 'unitwarp_p3'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Bring(P3, Exactly, 1, 'Devouring One (Zergling)', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P3, 'unitwarp_base', 'unitwarp_p3'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtMost, 536870912, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(6, 'Terran SCV', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 536870913, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Terran Marine', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1610612736, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(1, 'Terran Vulture', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 1610612737, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(8, 'Protoss Probe', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2684354560, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(2, 'Protoss Zealot', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 2684354561, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(7, 'Zerg Drone', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3758096384, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(5, 'Zerg Zergling', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '하급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 3758096385, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Zerg Hydralisk', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p3', P3),
		CreateUnit(6, 'Terran Marine', 'unitwarp_p3', P3),
		CreateUnit(2, 'Terran Medic', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Terran Vulture', 'unitwarp_p3', P3),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p3', P3),
		CreateUnit(4, 'Protoss Zealot', 'unitwarp_p3', P3),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p3', P3),
		CreateUnit(2, 'Protoss Dragoon', 'unitwarp_p3', P3),
		CreateUnit(1, 'Protoss Archon', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p3', P3),
		CreateUnit(10, 'Zerg Zergling', 'unitwarp_p3', P3),
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '중급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p3', P3),
		CreateUnit(6, 'Zerg Hydralisk', 'unitwarp_p3', P3),
		CreateUnit(2, 'Zerg Lurker', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p3', P3),
		CreateUnit(4, 'Terran Goliath', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p3', P3),
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_p3', P3),
		CreateUnit(5, 'Terran Wraith', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Protoss Archon', 'unitwarp_p3', P3),
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p3', P3),
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_p3', P3),
		CreateUnit(4, 'Protoss Scout', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Zerg Ultralisk', 'unitwarp_p3', P3),
		CreateUnit(5, 'Zerg Hydralisk', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P3, AtLeast, 1, '상급상자', 'unitwarp_p3'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p3', P3),
		CreateUnit(3, 'Zerg Guardian', 'unitwarp_p3', P3),
		CreateUnit(5, 'Zerg Mutalisk', 'unitwarp_p3', P3),
	],
	flag = [preserved]
)
Trigger(
	players = [P3],
	conditions = [Always()],
	actions = [
		ModifyUnitEnergy(All, '(men)', P3, 'unitwarp_p3', 100),
		MoveUnit(All, '(men)', P3, 'unitwarp_p3', 'unitgen_p3'),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Bring(P4, Exactly, 1, 'Terran Civilian', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P4, 'unitwarp_base', 'unitwarp_p4'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Bring(P4, Exactly, 1, 'Zerg Hydralisk', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P4, 'unitwarp_base', 'unitwarp_p4'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Bring(P4, Exactly, 1, 'Devouring One (Zergling)', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P4, 'unitwarp_base', 'unitwarp_p4'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtMost, 536870912, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(6, 'Terran SCV', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 536870913, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Terran Marine', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1610612736, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(1, 'Terran Vulture', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 1610612737, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(8, 'Protoss Probe', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2684354560, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(2, 'Protoss Zealot', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 2684354561, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(7, 'Zerg Drone', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3758096384, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(5, 'Zerg Zergling', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '하급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 3758096385, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Zerg Hydralisk', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p4', P4),
		CreateUnit(6, 'Terran Marine', 'unitwarp_p4', P4),
		CreateUnit(2, 'Terran Medic', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Terran Vulture', 'unitwarp_p4', P4),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p4', P4),
		CreateUnit(4, 'Protoss Zealot', 'unitwarp_p4', P4),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p4', P4),
		CreateUnit(2, 'Protoss Dragoon', 'unitwarp_p4', P4),
		CreateUnit(1, 'Protoss Archon', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p4', P4),
		CreateUnit(10, 'Zerg Zergling', 'unitwarp_p4', P4),
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '중급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p4', P4),
		CreateUnit(6, 'Zerg Hydralisk', 'unitwarp_p4', P4),
		CreateUnit(2, 'Zerg Lurker', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p4', P4),
		CreateUnit(4, 'Terran Goliath', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p4', P4),
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_p4', P4),
		CreateUnit(5, 'Terran Wraith', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Protoss Archon', 'unitwarp_p4', P4),
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p4', P4),
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_p4', P4),
		CreateUnit(4, 'Protoss Scout', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Zerg Ultralisk', 'unitwarp_p4', P4),
		CreateUnit(5, 'Zerg Hydralisk', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P4, AtLeast, 1, '상급상자', 'unitwarp_p4'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p4', P4),
		CreateUnit(3, 'Zerg Guardian', 'unitwarp_p4', P4),
		CreateUnit(5, 'Zerg Mutalisk', 'unitwarp_p4', P4),
	],
	flag = [preserved]
)
Trigger(
	players = [P4],
	conditions = [Always()],
	actions = [
		ModifyUnitEnergy(All, '(men)', P4, 'unitwarp_p4', 100),
		MoveUnit(All, '(men)', P4, 'unitwarp_p4', 'unitgen_p4'),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Bring(P5, Exactly, 1, 'Terran Civilian', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P5, 'unitwarp_base', 'unitwarp_p5'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Bring(P5, Exactly, 1, 'Zerg Hydralisk', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P5, 'unitwarp_base', 'unitwarp_p5'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Bring(P5, Exactly, 1, 'Devouring One (Zergling)', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P5, 'unitwarp_base', 'unitwarp_p5'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtMost, 536870912, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(6, 'Terran SCV', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 536870913, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Terran Marine', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1610612736, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(1, 'Terran Vulture', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 1610612737, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(8, 'Protoss Probe', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2684354560, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(2, 'Protoss Zealot', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 2684354561, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(7, 'Zerg Drone', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3758096384, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(5, 'Zerg Zergling', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '하급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 3758096385, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Zerg Hydralisk', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p5', P5),
		CreateUnit(6, 'Terran Marine', 'unitwarp_p5', P5),
		CreateUnit(2, 'Terran Medic', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Terran Vulture', 'unitwarp_p5', P5),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p5', P5),
		CreateUnit(4, 'Protoss Zealot', 'unitwarp_p5', P5),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p5', P5),
		CreateUnit(2, 'Protoss Dragoon', 'unitwarp_p5', P5),
		CreateUnit(1, 'Protoss Archon', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p5', P5),
		CreateUnit(10, 'Zerg Zergling', 'unitwarp_p5', P5),
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '중급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p5', P5),
		CreateUnit(6, 'Zerg Hydralisk', 'unitwarp_p5', P5),
		CreateUnit(2, 'Zerg Lurker', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p5', P5),
		CreateUnit(4, 'Terran Goliath', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p5', P5),
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_p5', P5),
		CreateUnit(5, 'Terran Wraith', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Protoss Archon', 'unitwarp_p5', P5),
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p5', P5),
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_p5', P5),
		CreateUnit(4, 'Protoss Scout', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Zerg Ultralisk', 'unitwarp_p5', P5),
		CreateUnit(5, 'Zerg Hydralisk', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P5, AtLeast, 1, '상급상자', 'unitwarp_p5'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p5', P5),
		CreateUnit(3, 'Zerg Guardian', 'unitwarp_p5', P5),
		CreateUnit(5, 'Zerg Mutalisk', 'unitwarp_p5', P5),
	],
	flag = [preserved]
)
Trigger(
	players = [P5],
	conditions = [Always()],
	actions = [
		ModifyUnitEnergy(All, '(men)', P5, 'unitwarp_p5', 100),
		MoveUnit(All, '(men)', P5, 'unitwarp_p5', 'unitgen_p5'),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 0, 'Nuclear Missile'),
		Bring(P6, Exactly, 1, 'Terran Civilian', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P6, 'unitwarp_base', 'unitwarp_p6'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 1, 'Nuclear Missile'),
		Bring(P6, Exactly, 1, 'Zerg Hydralisk', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P6, 'unitwarp_base', 'unitwarp_p6'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(CurrentPlayer, Exactly, 2, 'Nuclear Missile'),
		Bring(P6, Exactly, 1, 'Devouring One (Zergling)', 'item_center'),
	],
	actions = [
		MoveUnit(All, '(any unit)', P6, 'unitwarp_base', 'unitwarp_p6'),
		SetDeaths(CurrentPlayer, SetTo, 0, 'Goliath Turret'),
		KillUnit('Protoss Observer', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtMost, 536870912, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(6, 'Terran SCV', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 536870913, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1073741824, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Terran Marine', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 1073741825, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1610612736, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(1, 'Terran Vulture', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 1610612737, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(8, 'Protoss Probe', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2684354560, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(2, 'Protoss Zealot', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 2684354561, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3221225472, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(7, 'Zerg Drone', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 3221225473, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3758096384, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(5, 'Zerg Zergling', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '하급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 3758096385, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '하급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Zerg Hydralisk', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p6', P6),
		CreateUnit(6, 'Terran Marine', 'unitwarp_p6', P6),
		CreateUnit(2, 'Terran Medic', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Terran Vulture', 'unitwarp_p6', P6),
		CreateUnit(1, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p6', P6),
		CreateUnit(4, 'Protoss Zealot', 'unitwarp_p6', P6),
		CreateUnit(2, 'Protoss Dark Templar (Unit)', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p6', P6),
		CreateUnit(2, 'Protoss Dragoon', 'unitwarp_p6', P6),
		CreateUnit(1, 'Protoss Archon', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p6', P6),
		CreateUnit(10, 'Zerg Zergling', 'unitwarp_p6', P6),
		CreateUnit(1, 'Zerg Ultralisk', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '중급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '중급상자', 'unitwarp_p6', P6),
		CreateUnit(6, 'Zerg Hydralisk', 'unitwarp_p6', P6),
		CreateUnit(2, 'Zerg Lurker', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
	],
	actions = [
		SetSwitch(0, Random),
		SetSwitch(1, Random),
		SetSwitch(2, Random),
		SetSwitch(3, Random),
		SetSwitch(4, Random),
		SetSwitch(5, Random),
		SetSwitch(6, Random),
		SetSwitch(7, Random),
		SetSwitch(8, Random),
		SetSwitch(9, Random),
		SetSwitch(10, Random),
		SetSwitch(11, Random),
		SetSwitch(12, Random),
		SetSwitch(13, Random),
		SetSwitch(14, Random),
		SetSwitch(15, Random),
		SetSwitch(16, Random),
		SetSwitch(17, Random),
		SetSwitch(18, Random),
		SetSwitch(19, Random),
		SetSwitch(20, Random),
		SetSwitch(21, Random),
		SetSwitch(22, Random),
		SetSwitch(23, Random),
		SetSwitch(24, Random),
		SetSwitch(25, Random),
		SetSwitch(26, Random),
		SetSwitch(27, Random),
		SetSwitch(28, Random),
		SetSwitch(29, Random),
		SetSwitch(30, Random),
		SetSwitch(31, Random),
		SetDeaths(P7, SetTo, 0, 'Edmund Duke Turret (Siege Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(0, Set),
	],
	actions = [SetDeaths(P7, Add, 1, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(1, Set),
	],
	actions = [SetDeaths(P7, Add, 2, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(2, Set),
	],
	actions = [SetDeaths(P7, Add, 4, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(3, Set),
	],
	actions = [SetDeaths(P7, Add, 8, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(4, Set),
	],
	actions = [SetDeaths(P7, Add, 16, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(5, Set),
	],
	actions = [SetDeaths(P7, Add, 32, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(6, Set),
	],
	actions = [SetDeaths(P7, Add, 64, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(7, Set),
	],
	actions = [SetDeaths(P7, Add, 128, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(8, Set),
	],
	actions = [SetDeaths(P7, Add, 256, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(9, Set),
	],
	actions = [SetDeaths(P7, Add, 512, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(10, Set),
	],
	actions = [SetDeaths(P7, Add, 1024, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(11, Set),
	],
	actions = [SetDeaths(P7, Add, 2048, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(12, Set),
	],
	actions = [SetDeaths(P7, Add, 4096, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(13, Set),
	],
	actions = [SetDeaths(P7, Add, 8192, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(14, Set),
	],
	actions = [SetDeaths(P7, Add, 16384, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(15, Set),
	],
	actions = [SetDeaths(P7, Add, 32768, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(16, Set),
	],
	actions = [SetDeaths(P7, Add, 65536, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(17, Set),
	],
	actions = [SetDeaths(P7, Add, 131072, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(18, Set),
	],
	actions = [SetDeaths(P7, Add, 262144, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(19, Set),
	],
	actions = [SetDeaths(P7, Add, 524288, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(20, Set),
	],
	actions = [SetDeaths(P7, Add, 1048576, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(21, Set),
	],
	actions = [SetDeaths(P7, Add, 2097152, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(22, Set),
	],
	actions = [SetDeaths(P7, Add, 4194304, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(23, Set),
	],
	actions = [SetDeaths(P7, Add, 8388608, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(24, Set),
	],
	actions = [SetDeaths(P7, Add, 16777216, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(25, Set),
	],
	actions = [SetDeaths(P7, Add, 33554432, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(26, Set),
	],
	actions = [SetDeaths(P7, Add, 67108864, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(27, Set),
	],
	actions = [SetDeaths(P7, Add, 134217728, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(28, Set),
	],
	actions = [SetDeaths(P7, Add, 268435456, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(29, Set),
	],
	actions = [SetDeaths(P7, Add, 536870912, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(30, Set),
	],
	actions = [SetDeaths(P7, Add, 1073741824, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Switch(31, Set),
	],
	actions = [SetDeaths(P7, Add, 2147483648, 'Edmund Duke Turret (Siege Mode)')],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Deaths(P7, AtMost, 715827882, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Terran Siege Tank (Tank Mode)', 'unitwarp_p6', P6),
		CreateUnit(4, 'Terran Goliath', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 715827883, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 1431655765, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p6', P6),
		CreateUnit(1, 'Terran Battlecruiser', 'unitwarp_p6', P6),
		CreateUnit(5, 'Terran Wraith', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 1431655766, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2147483648, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Protoss Archon', 'unitwarp_p6', P6),
		CreateUnit(1, 'Protoss Reaver', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 2147483649, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 2863311530, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p6', P6),
		CreateUnit(1, 'Protoss Carrier', 'unitwarp_p6', P6),
		CreateUnit(4, 'Protoss Scout', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 2863311531, 'Edmund Duke Turret (Siege Mode)'),
		Deaths(P7, AtMost, 3579139413, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Zerg Ultralisk', 'unitwarp_p6', P6),
		CreateUnit(5, 'Zerg Hydralisk', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Bring(P6, AtLeast, 1, '상급상자', 'unitwarp_p6'),
		Deaths(P7, AtLeast, 3579139414, 'Edmund Duke Turret (Siege Mode)'),
	],
	actions = [
		RemoveUnitAt(1, '상급상자', 'unitwarp_p6', P6),
		CreateUnit(3, 'Zerg Guardian', 'unitwarp_p6', P6),
		CreateUnit(5, 'Zerg Mutalisk', 'unitwarp_p6', P6),
	],
	flag = [preserved]
)
Trigger(
	players = [P6],
	conditions = [Always()],
	actions = [
		ModifyUnitEnergy(All, '(men)', P6, 'unitwarp_p6', 100),
		MoveUnit(All, '(men)', P6, 'unitwarp_p6', 'unitgen_p6'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		CountdownTimer(Exactly, 0),
	],
	actions = [RemoveUnitAt(All, '(men)', 'itemfield', CurrentPlayer)],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 2, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Scanner Sweep'),
	],
	actions = [
		SetDeaths(P7, SetTo, 3, 'Goliath Turret'),
		SetDeaths(P7, SetTo, 0, 'Nuclear Missile'),
		RemoveUnitAt(All, '(any unit)', 'unitwarp_base', Force1),
		RemoveUnitAt(All, '(men)', 'itemfield', Force1),
		RemoveUnitAt(All, '(any unit)', 'itemfield', P7),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 0, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f1\n\x0f>>> \x0eZerg Zergling \x1030마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 1, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f2\n\x0f>>> \x0eZerg Zergling \x1080마리\n\x0f>>> \x0eZerg Hydralisk \x1020마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f3\n\x0f>>> \x0eZerg Zergling \x10150마리\n\x0f>>> \x0eZerg Hydralisk \x1040마리\n\x0f>>> \x0eZerg Mutalisk \x1040마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 3, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f4\n\x0f>>> \x0eProtoss Zealot \x10100마리\n\x0f>>> \x0eProtoss Dragoon \x1030마리\n\x0f>>> \x0eProtoss Archon \x1015마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Round \x1f5\n\x0f>>> \x0eFenix (Zealot) \x1030마리\n\x0f>>> \x0eProtoss Archon \x1030마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		DisplayText('\x0f>>  \x08Final Round\n\x0f>>> \x0eFenix (Zealot) \x1050마리\n\x0f>>> \x0eTassadar/Zeratul (Archon) \x1015마리'),
		PlayWAV('sound\Bullet\LaserHit.wav'),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Deaths(P7, Exactly, 60, 'Nuclear Missile'),
	],
	actions = [
		Order('(men)', P8, 'battleground', Patrol, 'attackaim'),
		SetDeaths(P7, SetTo, 0, 'Nuclear Missile'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [Deaths(P7, Exactly, 3, 'Goliath Turret')],
	actions = [SetInvincibility(Disable, '(men)', P8, 'battleground')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Bring(P7, Exactly, 0, '(buildings)', 'battleground'),
	],
	actions = [
		DisplayText('\n\x13\x08우리는 결국 굴복하고말았다\n'),
		Defeat(),
	],
	flag = []
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Bring(P8, Exactly, 0, '(men)', 'battleground'),
		Deaths(P7, AtMost, 4, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		KillUnitAt(All, '(any unit)', 'battleground', Force1),
		SetDeaths(P7, Add, 1, 'Siege Tank Turret (Tank Mode)'),
		SetDeaths(P7, SetTo, 4, 'Goliath Turret'),
		SetDeaths(P7, SetTo, 0, 'Nuclear Missile'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 3, 'Goliath Turret'),
		Bring(P8, Exactly, 0, '(men)', 'battleground'),
		Deaths(P7, Exactly, 5, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		SetDeaths(P7, SetTo, 100, 'Goliath Turret'),
		DisplayText('\n\x13\x1f우리는 결국 트리를 무사히 사수했다\n'),
		Wait(3000),
		Victory(),
	],
	flag = []
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Deaths(P7, Exactly, 1, 'Nuclear Missile'),
	],
	actions = [
		CreateUnitWithProperties(1, 'Terran SCV', 'upgrade_center', CurrentPlayer, UnitProperty(invincible=True)),
		DisplayText('\n\x1e업그레이드를 할 수 있습니다!\n\x0830초 \x1e안에 결정하세요'),
		CenterView('upgrade_center'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Bring(CurrentPlayer, AtLeast, 1, 'Terran SCV', 'upgrade_size'),
		Deaths(CurrentPlayer, AtMost, 2, 'Siege Tank Turret (Tank Mode)'),
	],
	actions = [
		KillUnitAt(1, 'Terran SCV', 'upgrade_size', CurrentPlayer),
		CreateUnitWithProperties(1, 'Zerg Zergling', 'upview_size', CurrentPlayer, UnitProperty(invincible=True)),
		SetDeaths(CurrentPlayer, Add, 1, 'Siege Tank Turret (Tank Mode)'),
		Wait(0),
		GiveUnits(All, 'Zerg Zergling', CurrentPlayer, 'upview_size', P10),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Bring(CurrentPlayer, AtLeast, 1, 'Terran SCV', 'upgrade_speed'),
		Deaths(CurrentPlayer, AtMost, 1, 'Nuclear Missile'),
	],
	actions = [
		KillUnitAt(1, 'Terran SCV', 'upgrade_speed', CurrentPlayer),
		CreateUnitWithProperties(1, 'Zerg Zergling', 'upview_speed', CurrentPlayer, UnitProperty(invincible=True)),
		SetDeaths(CurrentPlayer, Add, 1, 'Nuclear Missile'),
		Wait(0),
		GiveUnits(All, 'Zerg Zergling', CurrentPlayer, 'upview_speed', P10),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Bring(CurrentPlayer, AtLeast, 1, 'Terran SCV', 'upgrade_wall'),
	],
	actions = [
		KillUnitAt(1, 'Terran SCV', 'upgrade_wall', CurrentPlayer),
		CreateUnitWithProperties(1, 'Zerg Zergling', 'upview_wall', CurrentPlayer, UnitProperty(invincible=True)),
		CreateUnitWithProperties(1, 'Terran Siege Tank (Tank Mode)', 'item_center', CurrentPlayer, UnitProperty(invincible=True)),
		DisplayText('\x11부수고싶은 벽에 붙어 시즈모드하세요'),
		Wait(0),
		GiveUnits(All, 'Zerg Zergling', CurrentPlayer, 'upview_wall', P10),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [Bring(CurrentPlayer, AtLeast, 1, 'Terran Siege Tank (Siege Mode)', 'itemfield')],
	actions = [MoveLocation('2by2', 'Terran Siege Tank (Siege Mode)', CurrentPlayer, 'itemfield')],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Bring(CurrentPlayer, AtLeast, 1, 'Terran Siege Tank (Siege Mode)', 'itemfield'),
		Bring(P12, AtLeast, 1, 'Terran Control Tower', '2by2'),
	],
	actions = [
		KillUnitAt(1, 'Terran Control Tower', '2by2', P12),
		KillUnitAt(1, 'Terran Siege Tank (Siege Mode)', '2by2', CurrentPlayer),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [
		Bring(CurrentPlayer, AtLeast, 1, 'Terran Siege Tank (Siege Mode)', 'itemfield'),
		Bring(P12, Exactly, 0, 'Terran Control Tower', '2by2'),
	],
	actions = [
		RemoveUnitAt(1, 'Terran Siege Tank (Siege Mode)', '2by2', CurrentPlayer),
		CreateUnitWithProperties(1, 'Terran Siege Tank (Tank Mode)', '2by2', CurrentPlayer, UnitProperty(invincible=True)),
		DisplayText('\x11더 가까이 붙어서 시즈모드하세요'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Bring(Force1, AtLeast, 2, 'Terran SCV', 'upgrade_collecttime'),
		Deaths(P7, AtMost, 2, 'Alan Schezar Turret'),
	],
	actions = [
		MoveUnit(2, 'Terran SCV', Force1, 'upgrade_collecttime', 'upview_collecttime'),
		SetDeaths(P7, Add, 1, 'Alan Schezar Turret'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Bring(Force1, AtLeast, 2, 'Terran SCV', 'upgrade_quality'),
		Deaths(P7, Exactly, 0, 'Edmund Duke Turret (Tank Mode)'),
	],
	actions = [
		MoveUnit(2, 'Terran SCV', Force1, 'upgrade_quality', 'upview_quality'),
		SetDeaths(P7, SetTo, 1, 'Edmund Duke Turret (Tank Mode)'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [Bring(CurrentPlayer, AtLeast, 1, 'Terran SCV', 'upview_collecttime')],
	actions = [
		RemoveUnitAt(1, 'Terran SCV', 'upview_collecttime', CurrentPlayer),
		CreateUnitWithProperties(1, 'Zerg Zergling', 'upview_collecttime', CurrentPlayer, UnitProperty(invincible=True)),
		Wait(0),
		GiveUnits(All, 'Zerg Zergling', CurrentPlayer, 'upview_collecttime', P10),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [Bring(CurrentPlayer, AtLeast, 1, 'Terran SCV', 'upview_quality')],
	actions = [
		RemoveUnitAt(1, 'Terran SCV', 'upview_quality', CurrentPlayer),
		CreateUnitWithProperties(1, 'Zerg Zergling', 'upview_quality', CurrentPlayer, UnitProperty(invincible=True)),
		Wait(0),
		GiveUnits(All, 'Zerg Zergling', CurrentPlayer, 'upview_quality', P10),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Bring(Force1, Exactly, 0, '(men)', 'upgrade_center'),
		Deaths(P7, AtLeast, 1, 'Nuclear Missile'),
		Deaths(P7, AtMost, 300, 'Nuclear Missile'),
	],
	actions = [SetDeaths(P7, SetTo, 324, 'Nuclear Missile')],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [
		Deaths(P7, Exactly, 4, 'Goliath Turret'),
		Deaths(P7, Exactly, 360, 'Nuclear Missile'),
	],
	actions = [
		KillUnitAt(All, '(men)', 'upgrade_center', Force1),
		SetDeaths(P7, SetTo, 1, 'Goliath Turret'),
		SetDeaths(P7, SetTo, 0, 'Nuclear Missile'),
	],
	flag = [preserved]
)
Trigger(
	players = [P7],
	conditions = [Always()],
	actions = [
		SetDeaths(P7, Add, 1, 'Nuclear Missile'),
		MoveUnit(All, '(men)', Force1, 'battlelimit', 'battleground'),
	],
	flag = [preserved]
)
Trigger(
	players = [Force1],
	conditions = [Always()],
	actions = [
		SetAllianceStatus(Force1, Ally),
		SetAllianceStatus(P9, Ally),
		SetAllianceStatus(P10, Ally),
		RunAIScript('Turn ON Shared Vision for Player 1'),
		RunAIScript('Turn ON Shared Vision for Player 2'),
		RunAIScript('Turn ON Shared Vision for Player 3'),
		RunAIScript('Turn ON Shared Vision for Player 4'),
		RunAIScript('Turn ON Shared Vision for Player 5'),
		RunAIScript('Turn ON Shared Vision for Player 6'),
	],
	flag = [preserved]
)
Trigger(
	players = [P8],
	conditions = [Always()],
	actions = [
		RunAIScript('Turn ON Shared Vision for Player 1'),
		RunAIScript('Turn ON Shared Vision for Player 2'),
		RunAIScript('Turn ON Shared Vision for Player 3'),
		RunAIScript('Turn ON Shared Vision for Player 4'),
		RunAIScript('Turn ON Shared Vision for Player 5'),
		RunAIScript('Turn ON Shared Vision for Player 6'),
		SetAllianceStatus(P7, Enemy),
	],
	flag = [preserved]
)
Trigger(
	players = [AllPlayers],
	conditions = [Always()],
	actions = [
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
	],
	flag = [preserved]
)
Trigger(
	players = [AllPlayers],
	conditions = [Always()],
	actions = [
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
	],
	flag = [preserved]
)
Trigger(
	players = [AllPlayers],
	conditions = [Always()],
	actions = [
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
		Wait(0),
	],
	flag = [preserved]
)


mf.SaveMap()