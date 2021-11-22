FILENAME = open("Jour7.txt","r")

liste = []
for f in FILENAME:
    liste.append(f)



    
def holdshiny():
    l = []
    for f in liste:
        if 'shiny gold' in f:
            ligne = f.split(" ")
            couleuract = ligne[0]+" "+ligne[1]
            if couleuract != 'shiny gold':
                ligne = f.split(" ")
                c = ligne[0]+" "+ligne[1]
                l.append(c)
    return(l)



def isholded(color,l):
    for f in liste:
        if color in f:
            ligne = f.split(" ")
            c = ligne[0]+" "+ligne[1]
            if c != color and c not in l:
                l.append(c)
    return(l)


    
def main():
    already = holdshiny()
    for f in already:
        ligne = f.split(" ")
        color = ligne[0]+" "+ligne[1]
        already = isholded(color,already)
    print(len(already))
    return(None)

#main()


def nothing():
    n = []
    for f in liste:
        test = True
        for e in '123456789':
            if e in f:
                test = False
                break
        if test:
            ligne = f.split(" ")
            c = ligne[0]+" "+ligne[1]
            n.append(c)
    return(n)
        
n = nothing()

def holds(color='shiny gold'):
    m = 0
    for f in liste:
        if color in f:
            ligne = f.split(" ")
            c = ligne[0]+" "+ligne[1]
            if c in n:
                return(0)
            if c == color:
                compt = 0
                for e in ligne:
                    if e in '1234567890':
                        b = ligne[compt+1]+" "+ligne[compt+2]
                        m += int(e)+int(e)*holds(b)
                    compt += 1
    print(color,m)
    return(m)

holds()
         
              








