with open("Jour16Test.txt",'r') as f:
    val = [ligne.split(':') for ligne in f]
            
 

 
def condition():
    non = ['your ticket','nearby tickets']
    cond = []
    for ligne in val:
        if len(ligne) == 2:
            if ligne[0] not in non:
                l = ligne[1].split(' ')
                a,b = l[1],l[3]
                la = a.split("-")
                lb = b.split("-")
                ca,da = int(la[0]),int(la[1])
                cb,db = int(lb[0]),int(lb[1])
                cond.append([ [ca,da] , [cb,db] ])                
    return(cond)
cond = condition()
    
def isvalid(n):
    for c in cond:
        ca,da = c[0][0],c[0][1]
        cb,db = c[1][0],c[1][1]
        if ca <= n <= da or cb <= n <= db:
            return(True)
    return(False)
    
    
def trouve_indice():
    for compt in range(len(val)):
        if 'nearby tickets' in val[compt]:
            return(compt)
            
    
def part1():
    compteur = 0
    i = trouve_indice()
    for e in range(i+1,len(val)):
        ligne = val[e]
        if len(ligne) == 1:
            l = ligne[0].split(',')
            for f in l:
                f = int(f)
                if not isvalid(f):
                    compteur += f
    print(compteur)
    return(compteur)


#part1()

def condition2():
    non = ['your ticket','nearby tickets']
    d = {}
    for ligne in val:
        if len(ligne) == 2:
            if ligne[0] not in non:
                l = ligne[1].split(' ')
                a,b = l[1],l[3]
                la = a.split("-")
                lb = b.split("-")
                ca,da = int(la[0]),int(la[1])
                cb,db = int(lb[0]),int(lb[1])
                d[ ligne[0] ] = [ [ca,da] , [cb,db]  ]  
    return(d)

d = condition2()

def isvalid2(ligne):
    l = ligne[0].split(',')
    for f in l:
        f = int(f)
        if not isvalid(f):
            return(False)
    return(True)    



def row(pos,cond):
    c = 0
    i = trouve_indice()
    for e in range(i+1,len(val)):
        l = val[e][0].split(',')
        if isvalid2(val[e]):
            if not (cond[0][0] <= int(l[pos]) <= cond[0][1] or cond[1][0] <= int(l[pos]) <= cond[1][1]):
                return(False)
    return(True)


def part2():
    place = {}
    position = []
    for nom in d:
        for pos in range(len(d)):
            if pos not in position and row(pos,d[nom]):
                place[nom] = pos
                position.append(pos)
                break
    print(place)
    return(place)

#place = part2()

"""

La les commentaires sont jolis

et peu importe le nombre de lignes ça passe à la fin


"""




















