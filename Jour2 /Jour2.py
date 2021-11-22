mdp = open("Jour2.txt","r")
val = mdp.readlines()
valide = 0
for i in range(len(val)):
    
    coupe = val[i].split("-")
    premier = int(coupe[0])
    coupe = coupe[1].split(" ")
    deuxieme = int(coupe[0])
    lettre = coupe[1][0]
    motdepasse = coupe[2].split("\n")[0]
    compteur = 0
    for l in motdepasse:
        if l==lettre:
            compteur +=1
    if premier <= compteur <= deuxieme:
        valide += 1

print(valide)
    
        
valide = 0
for i in range(len(val)): 
    coupe = val[i].split("-")
    premier = int(coupe[0])
    coupe = coupe[1].split(" ")
    deuxieme = int(coupe[0])
    lettre = coupe[1][0]
    motdepasse = coupe[2].split("\n")[0]
    test = True
    if motdepasse[premier-1] == lettre and motdepasse[deuxieme-1] != lettre:
        valide +=1
        
    if motdepasse[premier-1] != lettre and motdepasse[deuxieme-1] == lettre:
        valide +=1
print(valide)