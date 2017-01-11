'''
Useful utilities. You may freely use these functions.
'''


def EPD(offset):
	'''
	Offset to EPD player.
	'''
	return (offset - 0x0058A364) // 4


'''
Nested list / Single item -> Flat list
 ex) FlattenList([a, [b, c], d]) -> [a, b, c, d]
 ex) FlattenList([a, b, c])      -> [a, b, c]
 ex) FlattenList(a)              -> [a]
'''


def FlattenList(l):
	try:
		ret = []
		for item in l:
			ret.extend(FlattenList(item))
		return ret

	except TypeError:  # l is not iterable
		return [l]


'''
Parses SCMDraft2 style text message
'''


def SCM2Text(s):
	#
	# normal -> xdigitinput1 -> xdigitinput2 -> xdigitinput3 -> normal
	#        '<'           xdigit          xdigit            '>'
	#                        -> normal
	#                       '>' emit '<>'
	#                                        -> normal
	#                                        '>' emit x00
	#                                                        -> normal
	# xdigit/normal  emit '<xx'
	def toxdigit(i):
		if '0' <= i <= '9':
			return ord(i) - 48
		elif 'a' <= i <= 'z':
			return ord(i) - 97 + 10
		elif 'A' <= i <= 'Z':
			return ord(i) - 65 + 10
		else:
			return None

	state = 0
	buf = [None, None]
	bufch = [None, None]
	out = []

	# simple fsm
	for i in s:
		if state == 0:
			if i == '<':
				state = 1
			else:
				out.append(i)

		elif state == 1:
			xdi = toxdigit(i)
			if xdi is not None:
				buf[0] = xdi
				bufch[0] = i
				state = 2

			else:
				out.extend(['<', i])
				state = 0

		elif state == 2:
			xdi = toxdigit(i)
			if xdi is not None:
				buf[1] = xdi
				bufch[1] = i
				state = 3

			elif i == '>':
				out.append(chr(buf[0]))
				state = 0

			else:
				out.extend(['<', bufch[0], i])
				state = 0

		elif state == 3:
			if i == '>':
				out.append(chr(buf[0] * 16 + buf[1]))
				state = 0

			else:
				out.extend(['<', bufch[0], bufch[1], i])
				state = 0

	return ''.join(out)


'''
s = mapstring2str(ARG)                     >>> print(s)
mapstring2str('def\x20\x09\x0a\x1f abc')   >>> 'def \t\n\x1f abc\'
mapstring2str('dd\x0a', stringize = False) >>> dd\n
mapstring2str(b'tt')                       >>> 'tt'
mapstring2str(b'tt', stringize = False)    >>> tt
mapstring2str(4)                           >>> 4
mapstring2str(4, stringize = False)        >>> 4 # no meaning for int
'''
def mapstring2str(item, stringize = True):
	assert type(item) in [str, bytes, int]
	if type(item) is bytes:
		res = ''
		index = 0
		while index < len(item):
			b = item[index]
			if b == 0:
				return res
			elif b == ord('\n'):
				res += '\\n'
			elif b == ord('\t'):
				res += '\\t'
			elif b == ord('\\'):
				res += '\\\\'
			elif b == ord('\''):
				res += '\\\''
			elif b == ord('\"'):
				res += '\\\"'
			elif 0x01 <= b <= 0x1F or b == 0x7F:
				res += '\\x%02x' % b
			else:
				end = index
				while end < len(item) and 0x20 <= item[end] and \
						item[end] not in (ord('\\'), ord('\''), ord('\"'), 0x7F):
					end += 1
				res += item[index:end].decode('euc-kr')
				index = end
				continue
			index += 1
		return '\'%s\'' % res if stringize else res
	if type(item) is int:
		return str(item)
	if type(item) is str:
		return '\'%s\'' % item if stringize else item

