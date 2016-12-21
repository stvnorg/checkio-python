import re

def translate(str):
	result = ""
	for s in str.split(' '):
		while len(s) != 0:
			m = re.match(r'[bcdfghjklmnpqrstvwxz]'+r'[aiueoy]',s,re.M|re.I)
			if m: s = s[s.index(m.group())+len(m.group()):]; result += m.group()[0]
			n = re.match(r'[aiueoy]{3}',s,re.M|re.I)
			if n: s = s[s.index(n.group())+len(n.group()):]; result += n.group()[0]
		result += ' '
	print (result)

translate("hieeelalaooo")
translate("hoooowe yyyooouuu duoooiiine")
translate("aaa bo cy da eee fe")
translate("sooooso aaaaaaaaa")
