FILENAME = open("Jour6.txt","r")

val = []

for l in FILENAME:
    val.append(l[:len(l)-1])
    
    
def main():
    compt = 0
    fin = len(val)
    somme = 0
    liste = ''
    for l in val:
        compt +=1
        if l == '':
            somme += len(liste)
            liste = []
        if compt == fin:
            for e in l:
                if not e in liste:
                    liste += e
            somme += len(liste)
            print(somme)
            return(somme)
        else:
            for e in l:
                if not e in liste:
                    liste += e
        

#main()


def group():
    compt = 0
    fin = len(val)
    somme = 0
    lref = val[0]
    liste2 = ''
    while compt <= fin:
        compt += 1
        
        if compt == fin:
            liste2 = l+'u'
            copie = ''
            for e in liste2:
                if e in lref:
                    copie += e
                    
            lref = copie
            somme += len(lref)
            print(somme)
            return(somme)
        elif val[compt-1] =='':
            somme += len(lref)
            lref = val[compt]   
            print(somme)

        else:
            copie = ''
            liste2 = val[compt-1]
            print("lref",lref)
            print("L2",liste2)
            for e in liste2:
                if e in lref:
                    copie += e
            print("COPIIIIE",copie)
            lref = copie
            
                
#group()
#AAAAAAAAAH CEST DE LA MERDE
















