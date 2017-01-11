from struct import pack, unpack
from collections import namedtuple
from ..chktok import Section

LocationData = namedtuple('LocationData', ['x1', 'y1', 'x2', 'y2', 'stringid', 'flag'])

class MRGNSection(Section, Name='MRGN'):
	def __init__(self, content, starcraftmap):
		self._data = []

		if content:
			self.Load(content)

	def Load(self, content):
		for i in range(0, 5100, 20):
			# x1, y1, x2, y2, stringid, flag
			self._data.append(LocationData(*unpack('<IIIIHH', content[i:i+20])))

	def Save(self):
		res = []
		for i in range(255):
			res.append(pack('<IIIIHH', *self._data[i]))
		return b''.join(res)

	def Iterate(self, f):
		return [f(i, t) for i, t in enumerate(self._data)]

if __name__ == "__main__":
	b = pack("<IIIIHH", 1, 2, 3, 4, 5, 6)

	m = MRGNSection(b*255)

	print(m.Iterate(lambda i, p:p.stringid))

	m.__bytes__()
