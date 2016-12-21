c = 'ADFGVX'

def getStr(str):
    t = []
    for i in str:
        if i not in t: t.append(i)
    return t

def encode(msg,secret,key):
    sec,k,enc,r = getStr(secret.lower()),getStr(key.lower()),[],''
    s = [sec[i*6:i*6+6] for i in range(6)]
    msg = [i for i in msg.lower() if i.isalpha() or i.isdigit()]
    for i in msg:
        for j in range(len(s)):
            try:
                n = s[j].index(i)
                enc.append(c[j])
                enc.append(c[n])
            except:
                pass
    print (k,enc,s)
    n,m = len(k),len(enc)
    table = [enc[i*n:i*n+n] for i in range(m/n)]            
    if m%n: table.append(enc[m-(m%n):]); table[len(table)-1] += ['']*(n-(m%n))
    print (table)
    for i in sorted(k):
        r += "".join([table[a][k.index(i)] for a in range(len(table))])
    print (r)      
    return r

def decode(msg,secret,key):
    sec,k = getStr(secret.lower()),getStr(key.lower())
    s = [sec[i*6:i*6+6] for i in range(6)]
    n,m = len(msg),len(key)
    full,less,enc,count = n/m+1,n/m,{},0
    for i in sorted(key):
        if i not in key[n%m:]: enc[i]=msg[count:count+full]; count += full
        else: enc[i]=msg[count:count+less]+' '; count += less
    text = [enc[i] for i in key]
    #print (text)
    r = [text[j][i] for i in range(len(text[0])) for j in range(len(text)) if text[j][i]!=' ']
    text = [s[c.index(r[i])][c.index(r[i+1])] for i in range(0,len(r),2)]
    print (text,r)
    return "".join(text)
    

if __name__ == '__main__':
    encode('I am going.', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher') 
    decode('FXGAFVXXAXDDDXGA', 'dhxmu4p3j6aoibzv9w1n70qkfslyc8tr5e2g','cipher')
    encode("ditiszeergeheim", "na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz", "piloten")
    decode("DFGGXXAAXGAFXGAFXXXGFFXFADDXGA","na1c3h8tb2ome5wrpd4f6g7i9j0kjqsuvxyz","piloten")
                                        
                                        
                                        
                                        