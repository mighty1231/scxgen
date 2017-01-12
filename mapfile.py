import os
from struct import unpack

from . import binio, chktok, mpqapi, ubconv
from .sections.uprpsection import UnitProperty

__all__ = ['MapFile']

def _PutDict_NoDup(d, key, value):
	if key in d:  # Duplication
		d[key] = None  # Mark as duplicate
	else:
		d[key] = value
		
def IgnoreColor(s):
	stb = []
	for ch in s:
		if 0x01 <= ch <= 0x1F or ch == 0x7F:  # Special characters.
			continue
		else:
			stb.append(bytes([ch]))
	return b''.join(stb)

class MapFile:
	def __init__(self, loadname, savename, backupdb=None):
		if os.path.abspath(loadname) == os.path.abspath(savename):
			raise RuntimeError("Overwrite input file is prohibited.")
		self.loadname = loadname
		self.savename = savename
		self.backupdb = backupdb
		self.hooks = []

	def LoadMap(self, fname=None):
		if fname is None:
			fname = self.loadname

		print('Loading map %s' % fname)

		# read mpq content. The file will be copied to output file.
		self._mpqcontent = open(fname, 'rb').read()

		# open mpq file
		mr = mpqapi.MpqRead()
		if not mr.Open(fname):
			raise RuntimeError('Failed to open map file \'%s\'.' % fname)

		# extract scenario.chk
		rawchk = mr.Extract('staredit\\scenario.chk')
		self.chk = chktok.CHK(self)
		self.chk.loadchk(rawchk)

		## load basic map setting
		# settings related with STR section
		strsection = self.chk.getsection('STR')

		sprpsection = self.chk.getsection('SPRP')
		scenario_name, scenario_desc = unpack('<HH', sprpsection.content)
		strsection.AddRef(scenario_name)
		strsection.AddRef(scenario_desc)

		forcsection = self.chk.getsection('FORC') # general section
		forces_name = unpack('<HHHH', forcsection.content[8:8+8])
		for n in forces_name:
			strsection.AddRef(n)

		wavsection = self.chk.getsection('WAV') # general section
		if wavsection:
			for i in range(0, len(wavsection.content), 4):
				strid = binio.b2i4(wavsection.content, i)
				if strid != 0:
					strsection.AddRef(strid)

		# get location names
		self.locnametable = {}
		mrgnsection = self.chk.getsection('MRGN') # specialized section
		if mrgnsection:
			locstrids = mrgnsection.Iterate(lambda i, p:p.stringid)
			for i, strid in enumerate(locstrids):
				if strid != 0:
					locstr = strsection.GetString(strid)
					strsection.AddRef(strid)
					_PutDict_NoDup(self.locnametable, locstr, i + 1)

		# get unit names
		self.unitnametable = {}
		unixsection = self.chk.getsection('UNIx') # general section
		if unixsection:
			for i in range(228):
				unitstrid = binio.b2i2(unixsection.content, 3192 + i * 2)
				if unitstrid != 0:
					unitstr = strsection.GetString(unitstrid)
					strsection.AddRef(unitstrid)
					_PutDict_NoDup(self.unitnametable, unitstr, i)
					cignored = IgnoreColor(unitstr)
					if cignored != unitstr:
						_PutDict_NoDup(self.unitnametable, cignored, i)

		# get switch names
		self.swnametable = {}
		swnmsection = self.chk.getsection('SWNM') # general section
		if swnmsection:
			for i in range(256):
				swnameid = binio.b2i4(swnmsection.content, i * 4)
				if swnameid != 0:
					swname = strsection.GetString(swnameid)
					strsection.AddRef(swnameid)
					_PutDict_NoDup(self.swnametable, swname, i)


		# exceptional cases
		mbrfsection = self.chk.getsection('MBRF', required = True)
		if mbrfsection.mbtriggers:
			with open('mbtrigger.txt', 'w', encoding='euc-kr') as fp:
				for mbtrigger in mbrfsection.mbtriggers:
					fp.write(mbtrigger.Decode(self))
					fp.write('\n')

			raise RuntimeError('All mbtriggers of original map should be removed')
		mbrfsection.InstallMBTriggerHook()

		trigsection = self.chk.getsection('TRIG', required = True)
		if trigsection.triggers:
			with open('trigger.txt', 'w', encoding='euc-kr') as fp:
				for trigger in trigsection.triggers:
					fp.write(trigger.Decode(self))
					fp.write('\n')

			raise RuntimeError('All triggers of original map should be removed')
		trigsection.InstallTriggerHook()
		
		uprpsection = self.chk.getsection('UPRP', required = True)
		uprpsection.Clear()
		uprpsection.InstallUnitPropertyHook()

	def SaveMap(self, fname=None):
		if fname is None:
			fname = self.savename
		print('Saving map %s' % fname)

		self.chk.getsection('TRIG').UninstallTriggerHook()
		self.chk.getsection('MBRF').UninstallMBTriggerHook()
		self.chk.getsection('UPRP').UninstallUnitPropertyHook()

		# dump
		rawchk = self.chk.savechk()

		# dump mpq content and modify it
		open(fname, 'wb').write(self._mpqcontent)
		mw = mpqapi.MpqWrite()
		if not mw.Open(fname, preserve_content=True):
			raise RuntimeError('Cannot open output file \'%s\'.' % self._mpqcontent)

		mw.PutFile('staredit\\scenario.chk', rawchk)

		# Compact & close
		mw.Compact()
		mw.Close()

		if self.backupdb:
			assert self.backupdb[-4:] == '.zip'
			mapfile = open(fname, 'rb').read()
			with zipfile.ZipFile(self.backupdb, 'a') as z:
				tm = time.localtime()
				timestr = '%d%d%d_%d%d%d' % (
					tm.tm_year,
					tm.tm_mon,
					tm.tm_mday,
					tm.tm_hour,
					tm.tm_min,
					tm.tm_sec
				)
				z.writestr('backup_%s.scx' % timestr, mapfile)


	def EncodeLocation(self, locstring):
		assert type(locstring) in [str, bytes]

		string = ubconv.u2b(locstring)

		if string in self.locnametable:
			locidx = self.locnametable[string]
			if not locidx:
				raise RuntimeError('Ambigious location name %s' % locstring)
			return locidx
		return None


	def EncodeUnit(self, unitstring):
		assert type(unitstring) in [str, bytes]

		string = ubconv.u2b(unitstring)

		if string in self.unitnametable:
			unitidx = self.unitnametable[string]
			if not unitidx:
				raise RuntimeError('Ambigious unit name %s' % unitstring)
			return unitidx
		return None


	def EncodeSwitch(self, swstring):
		assert type(swstring) in [str, bytes]
		
		string = ubconv.u2b(swstring)

		if string in self.swnametable:
			swidx = self.swnametable[string]
			if swidx is None:
				raise RuntimeError('Ambigious switch name %s' % swstring)
			return swidx

		return None


	def EncodeString(self, string):
		'''
		String -> string id.
		   If matching string -> returns its string id.
		   If no match -> Creates new string & returns its id.
			(May cause string overflow error.)
		'''
		assert type(string) in [str, bytes]

		bstring = ubconv.u2b(string)
		return self.chk.getsection('STR').GetStringIndex(bstring)


	def EncodeUnitProperty(self, uprp):
		assert isinstance(uprp, UnitProperty)

		return self.chk.getsection('UPRP').EncodeUnitProperty(uprp)

	def DecodeUnitProperty(self, uprpid):
		assert type(uprpid) is int
		
		return self.chk.getsection('UPRP').DecodeUnitProperty(uprpid)

	def DecodeLocation(self, locid):
		assert type(locid) is int

		if 0 < locid < 256:
			mrgn = self.chk.getsection('MRGN')
			if mrgn:
				locstrids = mrgn.Iterate(lambda i, p:p.stringid)
				res = self.chk.getsection('STR').GetString(locstrids[locid-1])
				return res
		return None

	def DecodeUnit(self, unitid):
		assert type(unitid) is int

		if 0 <= unitid <= 227:
			unix = self.chk.getsection('UNIx')
			if unix:
				unitstrid = binio.b2i2(unix.content, 3192 + unitid * 2)
				if unitstrid != 0:
					return IgnoreColor(self.chk.getsection('STR').GetString(unitstrid))
		return None

	def DecodeSwitch(self, swid):
		assert type(swid) is int

		if 0 <= swid < 256:
			swnm = self.chk.getsection('SWNM')
			if swnm:
				swnameid = binio.b2i4(swnm.content, swid * 4)
				return self.chk.getsection('STR').GetString(swnameid)
		return None

	def DecodeString(self, strid):
		assert type(strid) is int
		
		return self.chk.getsection('STR').GetString(strid)

	def __enter__(self):
		self.LoadMap(self.loadname)
		return self

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type == None and exc_val == None and exc_tb == None:
			self.SaveMap(self.savename)
		else:
			print('Error')
			print('MapFile.__exit__(', exc_type, exc_val, exc_tb, ')')
