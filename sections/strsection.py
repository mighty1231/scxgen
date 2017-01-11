'''
Similar with TBL from original trggen
'''

if __name__ == "__main__":
	import sys
	sys.path.append('..')
	import binio, ubconv, chktok
	from chktok import Section
else:
	from .. import binio, ubconv
	from ..chktok import Section

class STRSection(Section, Name='STR'):
	def __init__(self, content, starcraftmap):
        #
        # datatb : list of strings                : string data table
        # stringmap : string -> string id         : hashing
        # refcount : string id -> reference count
        #

		self._datatb      = []
		self._stringmap   = {}
		self._refcount    = []  # String starts from #1

		if content:
			self.Load(content)

	def Load(self, content):
		# This is not the complete process for load data
		# AddRef must be called for all string indexes
		self._datatb.clear()
		self._stringmap.clear()

		stringcount = binio.b2i2(content, 0)
		self._refcount = [0] * stringcount
		for i in range(stringcount):
			stringoffset = binio.b2i2(content, i*2+2)
			send = stringoffset
			while content[send] != 0:
				send += 1

			string = content[stringoffset:send]

			self._datatb.append(string)
			if not string in self._stringmap: # complicated
				self._stringmap[string] = i

	def GetStringIndex(self, string):
		# returns representative string id
		string = ubconv.u2b(string)

		if string in self._stringmap:
			_id = self._stringmap[string]
		else: # append new one
			if 0 in self._refcount:
				_id = self._refcount.index(0)
				self._datatb[_id] = string
				self._stringmap[string] = _id
			else:
				_id = len(self._datatb)
				self._datatb.append(string)
				self._stringmap[string] = _id
				self._refcount.append(0)
		self._refcount[_id] += 1
		return _id+1

	def GetString(self, index):
		assert 0 < index <= len(self._datatb)
		return self._datatb[index-1]

	def Save(self):
		res = []

		# consider holes from the high-index part
		actualcount = len(self._datatb)
		while self._refcount[actualcount - 1] == 0:
			actualcount -= 1

		# calculate offset of each string
		stroffset = []
		outindex = 2 * actualcount + 2
		for i in range(actualcount):
			if self._refcount[i] == 0:
				stroffset.append(0)
			else:
				stroffset.append(outindex)
				if outindex > 0xFFFF:
					raise RuntimeError("STRSection : limit on string count")
				outindex += len(self._datatb[i]) + 1

		# string count
		res.append(binio.i2b2(actualcount))

		# string offsets
		res += map(binio.i2b2, stroffset)

		# string data
		for i in range(actualcount):
			if self._refcount[i] != 0:
				res.append(self._datatb[i])
				res.append(b'\0')

		return b''.join(res)

	def ReplaceString(self, stringid, string):
		assert 0 < stringid <= len(self._datatb)
		self.SubRef(stringid)
		return self.GetStringIndex(string)

	def AddRef(self, stringid):
		# receives representative string id
		assert 0 < stringid <= len(self._datatb)
		self._refcount[stringid-1] += 1

	def SubRef(self, stringid):
		# receives representative string id
		assert 0 < stringid <= len(self._datatb)
		self._refcount[stringid-1] -= 1

		if self._refcount[stringid-1] == 0:
			string = self._datatb[stringid-1]
			# print("subref:", string)
			self._datatb[stringid-1] = ''

			# necessary from complicated case in Load()
			if string in self._datatb:
				self._stringmap[string] = self._datatb.index(stringmap)
			else:
				del self._stringmap[string]

if __name__ == "__main__":
	s = STRSection()
	s.Load(b'\x02\x00\x06\x00\x09\x00HH\x00TT\x00')
	s.AddRef(1)
	s.AddRef(2)

	s.SubRef(1)
	print(s.Save()) # b'\x02\x00\x00\x00\x06\x00TT\x00'
	print(s.GetStringIndex("1")) # 1
	print(s.Save()) # b'\x02\x00\x06\x00\x08\x001\x00TT\x00'

	print(s.GetStringIndex("1")) # 1
	print(s.GetStringIndex("2")) # 3
	print(s.Save()) # b'\x03\x00\x08\x00\n\x00\r\x001\x00TT\x002\x00'
	s.SubRef(2)
	print(s.Save()) # b'\x03\x00\x08\x00\x00\x00\n\x001\x002\x00'

	print(s.GetStringIndex("2")) # 3
	# refs = [2, 0, 2]
	s.SubRef(1)
	s.SubRef(3)
	print(s.Save()) # b'\x03\x00\x08\x00\x00\x00\n\x001\x002\x00'
	s.SubRef(1)
	print(s.Save()) # b'\x03\x00\x00\x00\x00\x00\x08\x002\x00'
	s.SubRef(3)
	print(s.Save()) # b'\x00\x00'