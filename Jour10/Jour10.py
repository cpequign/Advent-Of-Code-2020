import Jour10.txt

with open("Jour10.txt",'r') as f:
    val = f.readlines()
    
ent = [int(i) for i in val]
ent.append(0)
ent = sorted(ent)
    
def part1():
    j1, j3 = 1, 1
    i = 1
    compt = 0
    while compt < len(ent):
        if i+1 in ent:
            j1 += 1
            i += 1
        elif i+3 in ent:
            j3 += 1
            i += 3
            
        compt +=1
    print(j1,j3)
    print(j1*j3)
    return(None)

part1()

def part2():
    p2 = 0
    p7 = 0
    for e in ent:
        if (e+1 in ent) and (e+2 in ent) and (e+3 in ent) and (e+4 in ent):
            p7 +=1
            print(e,7)
        elif (e+1 in ent) and (e+2 in ent) and (e+3 in ent) and (e-1 not in ent):
            p2 += 2
            print(e,4)
        elif (e-1 not in ent) and (e+1 in ent) and (e+2 in ent):
            p2 +=1
            print(e,2)
    print(p2,p7)
    print(2**p2*7**p7)
        

    
part2()