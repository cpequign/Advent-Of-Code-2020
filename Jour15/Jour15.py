with open("Jour15.txt","r") as f:
    val = [ligne.split(',') for ligne in f][0]
    
def last_seen(n,l):
    for i in range(len(l)-2,-1,-1):
        if l[i] == n:
            p = len(l)-i-1
            return(p)
        





def part1():
    l  = [int(e) for e in val]
    compt = len(val)-1
    while compt < 2019:
        n = l[compt]
        if not n in l[:len(l)-1]:
            l.append(0)
            compt += 1
        else:
            p = last_seen(n,l)
            l.append(p)
            compt += 1
    print(l[-1])
    return(None)

#part1()

def part2():
    l = [int(e) for e in val]
    d = {}
    for i in range(len(l)-1):
        d[l[i]] = [-1,i+1]
    d[l[-1]] = [len(l)]
    compt = len(l) 
    lastseen = l[-1]
    while compt < 30000000:
        compt += 1
        if lastseen in d:
            if len(d[lastseen]) == 1:
                #On doit dire la valeur 0.
                lastseen = 0
                if 0 in d:
                    d[0].append(compt)
                else:
                    d[0] = [compt]
            else:
                ecart = compt - d[lastseen][-2] -1
                lastseen = ecart
                if ecart in d:
                    d[lastseen].append(compt)  
                else:
                    d[lastseen] = [compt]
        else:
            d[lastseen] = [compt+1]
            lastseen = 0
    print(lastseen)  
    return(d)

#d = part2()