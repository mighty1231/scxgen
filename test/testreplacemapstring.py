import sys
sys.path.append('..\\..') # It is used for only importing scxgen

from scxgen import *

with MapFile("test_nombrftrig.scx", "result.scx") as mapfile:
	mapfile.SetScenarioName('\x08New ScenarioName한글')
	mapfile.SetForce1Name('VERSION 0.05')