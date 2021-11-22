tob = open("Jour3.txt","r")

val = tob.readlines()

l = []
for i in val:
    a = i.split("\n")[0]
    l.append(a)


def descente(droite,bas):
    compteur = 0
    x,y = 0,0
    
    while y+bas<len(l):
        y += bas      
        x = (x + droite) % len(l[y])
        if y<len(l) and l[y][x] == "#":
            compteur +=1    
            
    return(compteur)

def plusieurs_descentes(l):
    compt = 1
    for i in l:
        droite,bas = i
        a = descente(droite,bas)
        print(a)
        compt *= a
    return(compt)



print(plusieurs_descentes([(3,1),(1,1),(5,1),(7,1),(1,2)])) 
 
    