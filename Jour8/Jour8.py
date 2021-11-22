FILENAME = open("Jour8.txt","r")

val = []

for l in FILENAME:
    val.append(l.split("\n"))
    
long = len(val)   
    
def main():
    dejavu = []
    indice = 0
    acc = 0
    while indice not in dejavu:
        print(val[indice])
        dejavu.append(indice)
        ligne = val[indice][0]
        if ligne[:3] == 'acc':
            acc += int(ligne[3:])
            indice += 1
        elif ligne[:3] == 'jmp':
            indice += int(ligne[3:])
            indice = indice % long
        else:
            indice +=1
    print(acc)
    return(None)

main()


def isterminate(v):
    dejavu = []
    indice = 0
    acc = 0
    while indice not in dejavu:
        dejavu.append(indice)
        ligne = v[indice][0]
        if ligne[:3] == 'jmp':
            indice += int(ligne[3:])
            indice = indice % long
        else:
            indice += 1
    if long-1 in dejavu:
        return(True)
    return(False)

def part2():
    compt = 0
    while compt < long-1:
        l = val[compt]
        if l[0][:3] == 'jmp':
            stock = l
            nouveau = ['','']
            nouveau[0] += 'nop'
            for e in val[compt][0][3:]:
                nouveau[0] += e
            val[compt] = nouveau
            if isterminate(val):
                main()
                return("fini, jmp en nop")
            val[compt] = stock
            
        elif l[0][:3] == 'nop':
            stock = l
            nouveau = ['','']
            nouveau[0] += 'jmp'
            for e in val[compt][0][3:]:
                nouveau[0] += e
            val[compt] = nouveau
            if isterminate(val):
                main()
                return("fini, nop en jmp") 
            val[compt] = stock
        compt += 1
            
        
    return("raté")
                

part2()