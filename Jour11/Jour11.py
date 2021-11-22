from copy import *
FILENAME = open("Jour11.txt",'r')

val = []
for l in FILENAME:
    if l[-1] == '\n':
        val.append(l[:-1])
    else:
        val.append(l)
        
        
def part1(val):
    test = True
    voisins = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    ligne = [i for i in range(len(val))]
    colonne = [j for j in range(len(val[0]))]
    while test:
        copie = ['' for j in range(len(val))]
        for i in range(len(val)):
            for j in range(len(val[0])):
                if val[i][j] == '.':
                    copie[i] += '.'

                elif val[i][j] == '#':
                    compt = 0
                    for l,c in voisins:
                        if (i-l in ligne) and (j-c in colonne) and (val[i-l][j-c] == '#'):
                            compt += 1
                    if compt <4:
                        copie[i] += '#'          
                    else:
                        copie[i] += 'L'
                else:
                    vide = True
                    for l,c in voisins:
                        if (i-l in ligne) and (j-c in colonne) and (val[i-l][j-c] == '#'):
                            vide = False
                            break
                    if vide:
                        copie[i] += '#'
                    else:
                        copie[i] += 'L'
        if val == copie:
            test = False
        val = deepcopy(copie)
    compt = 0
    for i in range(len(val)):
        for j in range(len(val[0])):
            if val[i][j] == '#':
                compt += 1
    print(compt)
    return(None)
    
#part1(val)

def part2(val):
    test = True
    voisins = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    ligne = [i for i in range(len(val))]
    colonne = [j for j in range(len(val[0]))]
    while test:
        copie = ['' for j in range(len(val))]
        for i in range(len(val)):
            for j in range(len(val[0])):
                if val[i][j] == '.':
                    copie[i] += '.'
                elif val[i][j] == '#':
                    compt = 0
                    for l,c in voisins:
                        avance = True
                        v = 1
                        
                        while avance and v<len(val):
                            if (i-l*v in ligne) and (j-c*v in colonne) and (val[i-l*v][j-c*v] == '#'):
                                compt += 1
                                avance = False
                            elif (i-l*v in ligne) and (j-c*v in colonne) and (val[i-l*v][j-c*v] == 'L'):
                                avance = False
                            else:
                                v += 1
                    if compt < 5:
                        copie[i] += '#'
                    else:
                        copie[i] += 'L'
                else:
                    compt = 0
                    for l,c in voisins:
                        avance = True
                        v = 1
                        
                        while avance and v<len(val):
                            if (i-l*v in ligne) and (j-c*v in colonne) and (val[i-l*v][j-c*v] == '#'):
                                compt += 1
                                avance = False
                            elif (i-l*v in ligne) and (j-c*v in colonne) and (val[i-l*v][j-c*v] == 'L'):
                                avance = False
                            v += 1
                    if compt < 1:
                        copie[i] += '#'
                    else:
                        copie[i] += 'L'                    
        if val == copie:
            test = False
        val = deepcopy(copie)
    compt = 0    
    for i in range(len(val)):
        for j in range(len(val[0])):
            if val[i][j] == '#':
                compt += 1
    print(compt)
    return(None)
    
    
    
#part2(val)
    
    
    
    
    
    
    
    