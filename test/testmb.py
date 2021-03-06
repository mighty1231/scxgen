import sys
sys.path.append('..\\..') # It is used only for importing scxgen

from scxgen import *

mf = MapFile("test_nombrftrig.scx", "result.scx")
mf.LoadMap()

MBTrigger(
	players = [Force1],
	actions = [
		MBTextMessage('wef', 4),
		MBTransmission('rtttttttt', 2, 10000, Subtract, 'sound\\Bullet\\TNsFir00.wav', 13131),
		Wait(341) # raise error
	]
)
mf.SaveMap()
