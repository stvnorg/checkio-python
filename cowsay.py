COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

def splitText(t):
    s = [i for i in t.split(' ') if i != '']
    r = []
    tmp = ''
    i = 0
    while i < len(s):
        if len(s[i]) >= 40:
            r.append(s[i][:39])
            s[i] = s[i][39:]
        if len(tmp+s[i]+' ') >= 41:
            r.append(tmp.strip(' '))
            tmp = ''
        else:
            tmp+=s[i]+' '
            i += 1
    r.append(tmp.strip(' '))
    r = [i for i in r if i != '']
    return r       
        
def cowsay(text):
   
    s = splitText(text)
    if len([i for i in text.split(' ') if i != ''])==1 and len(text)<40: s[0] = text; print(s)
    if len(" ".join(s)) < 40:
        f_l = ' '+'_'*(len(" ".join(s))+2)+'\n'
        l_l = ' '+'-'*(len(" ".join(s))+2)
        s_l = '< '+" ".join(s)+' >'+'\n'        
        return ('\n'+f_l+s_l+l_l+COW)
        
    else:            
        m = max([len(i) for i in s])
        if len(s) == 2:
            f_l = ' '+'_'*(m+2)+'\n'
            l_l = ' '+'-'*(m+2)
            s_l = '/ '+s[0]+' '*(m-len(s[0]))+' \\'+'\n'
            t_l = '\\ '+s[1]+' '*(m-len(s[1]))+' /'+'\n'
            return ('\n'+f_l+s_l+t_l+l_l+COW)
        else:
            f_l = ' '+'_'*(m+2)+'\n'
            l_l = ' '+'-'*(m+2)
            s_l = '/ '+s[0]+' '*(m-len(s[0]))+' \\'+'\n'
            n_l = ['| '+i+' '*(m-len(i))+' |'+'\n' for i in s[1:len(s)-1]]
            n_l = ''.join(n_l)
            t_l = '\\ '+s[len(s)-1]+' '*(m-len(s[len(s)-1]))+' /'+'\n'
            return ('\n'+f_l+s_l+n_l+t_l+l_l+COW)

if __name__ == '__main__':
	print (cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.'))
	print (cowsay("loooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong"))
	print (cowsay("spaces                           inside"))
	print (cowsay(" a"))
	print (cowsay("    c     "))
