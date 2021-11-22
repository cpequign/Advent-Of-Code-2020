FILENAME = open("Jour9.txt","r")

val = []
for l in FILENAME:
    val.append(int(l))
    
def part1():
    l = [val[i] for i in range(25)]
    long = len(val)
    for i in range(25,long):
        v = val[i]
        for j in range(25):
            if v-l[j] in l and l[j]*2!=v:
                l = val[i-24:i+1]
                break
            elif j ==24:
                print("INTRUS !",v)
                return(v)

part1()
 

def part2():                   
    b = 1721308972
    for i in range(len(val)):
        compt = val[i]
        indice = i
        while compt < b:
            indice += 1
            compt += val[indice]
        if compt == b:
            mini = min(val[i:indice+1])
            maxi = max(val[i:indice+1])
            print("Somme +petit, +grand",mini+maxi)
            return(None)
        
part2()