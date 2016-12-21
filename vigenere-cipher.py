letters = [chr(i) for i in range(65,91)]
v = [letters[i:]+letters[:i] for i in range(26)]
#for i in range(26):
#    v.append(letters[i:]+letters[:i])
#for i in v:
#    print (i)
#print ("".join(letters))
def getKey(k):
    for i in range(2,len(k)+1):
        s = ["".join(k[j:j+i]) for j in range(0,len(k),i)]
        print (s)
        count = ""
        t = s[0]      
        if len(s)>=1:
            for n in s[1:]:
                if n==t: count += '1' 
                else: count += '0'
            if "111" in count: return s[0]
    return k
                        
def decode_vigenere(od,oe,ne):
    key = getKey([chr(v[ord(od[i])-65].index(oe[i])+65) for i in range(len(od))])
    print (key)
    key += key*(len(ne)/len(key)+1)
    print (key)
    decrypt = [chr(j+65) for i in range(len(ne)) for j in range(26) if letters[v[j].index(ne[i])]==key[i]]
    return "".join(decrypt)

if __name__ == '__main__':
    print (decode_vigenere('HELLO','OIWWC','ICP'))
    print (decode_vigenere(u"ANDNOWFORSOMETHINGCOMPLETELYDIFFERENT", u"PLWUCJUMKZCZTRAPBTRMFWZRICEFRVUDXYSAI", u"XKTSIZQCKQOPZYGKWZDIBZZRTNTSZAXEAAOASGPVFXPJEKOLXANARBLLMYSRHGLRWCPLWQIZEGEPYRIMIYSFHUBSRSAMPLFFXNNACALMFLBFRJHAVVCETURUPLZHFBJLWPBOPPL"))
    print (decode_vigenere(u"LOREMIPSUM", u"OCCSDQJEXA", u"OCCSDQJEXA"))