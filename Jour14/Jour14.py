import itertools

with open("Jour14Loic.txt",'r') as f:
    val = [ligne.split('\n')[0] for ligne in f]
    
    
def itob(n):
    c = ''
    for i in range(35,-1,-1):
        if 2**i <= n:
            c += '1'
            n = n-2**i
        else:
            c +='0'
    return(c)

def btoi(c):
    m = 0
    for i in range(36):
        if c[i] == '1':
            m += 2**(35-i)
    return(m)

def mem(l):
    m = [e for e in l[4:]]
    b = ''
    c = 0
    while m[c] != ']':
        b += m[c]
        c += 1
    v = ''
    for e in range(c+4,len(m)):
        v += m[e]
    return(b,v)
    

def use_mask(mask,c):
    b = ''
    for i in range(36):
        if mask[i] == 'X':
            b += c[i]
        else:
            b += mask[i]
    return(b)
        

def part1():
    d ={}
    for l in val:
        if l[:4] == 'mask':
            mask = l[7:]
        else:
            m, v  = mem(l)
            c = itob(int(v))
            b = use_mask(mask,c)
            v = int(b,2)
            d[m] = v
    c = 0
    for m in d:
        c += d[m]
    print(c)
    return(d)
        
            
#part1()


def use_mask2(mask,c):
    b = ''
    for i in range(36):
        if mask[i] == 'X':
            b += 'X'
        elif mask[i] == '1':
            b += '1'
        else:
            b += c[i]
    return(b)

#Prend quelques années.
def possibilite(b):
    todolist = [b]
    for l in todolist:
        for i in range(len(l)):
            if l[i] == 'X':
                todolist.append(l[:i]+'0'+l[i+1:])
                todolist.append(l[:i]+'1'+l[i+1:])

    valeurs = []
    for l in todolist:
        if not 'X' in l:
            v = int(l,2)
            if not v in valeurs:
                valeurs.append(v)
    return(valeurs)

#Efficace.
def possibilite2(b):
    n = 0
    for e in b:
        if e =='X':
            n += 1
    p = ["".join(seq) for seq in itertools.product("01", repeat=n)] 
    l = []
    
    for e in p:
        c = 0
        v = ''
        for i in range(len(b)):
            if b[i] == 'X':
                v += e[c]
                c += 1
            else:
                v += b[i]
        l.append(int(v,2))
    

    return(l)

def part2():
    d= {}
    for l in val:
        if l[:4] == 'mask':
            mask = l[7:]
        else:
            m, v  = mem(l)
            c = itob(int(m))
            b = use_mask2(mask,c)
            p = possibilite2(b)
            for pos in p:
                d[pos] = int(v)
    
    c= 0
    for l in d:
        c += d[l]
    print(d)
    print(c)
    return(c)


#part2()







    