FILENAME = open("Jour5.txt","r")


l = FILENAME.readlines()
def row(f):
    n = 0
    a = 0
    b = 127
    while a!=b:
        if f[n] == 'F':
            b = b - 2**(6-n)
            n += 1
            
        if f[n] == 'B':
            a = a + 2**(6-n)
            b = b
            n += 1
    return(a)
    
def column(f):
    n = 0
    a = 0
    b = 7
    while a!=b:
        if f[n+7] == 'L':
            b = b - 2**(2-n)
            n += 1
        if f[n+7] == 'R':
            a = a + 2**(2-n)
            n += 1
    return(a)



def seatID(f):
    r = row(f)
    c = column(f)
    return(r*8+c)

def maximisons():
    m = 0
    seats = []
    for f in l:
        seats.append(seatID(f))
        if seatID(f) > m :
            m = seatID(f)
    print(m)
    return(seats)


def missingrow():
    lignes = [0 for i in range(128)]
    for f in l:
        r = row(f)
        lignes[r] += 1
    return(lignes.index(7))

def missingseat():
    m = missingrow()
    seats = maximisons()
    for c in range(8):
        seatID = m*8+c
        if not seatID in seats:
            print(seatID)
            return(seatID)
        
missingseat()


"""Des trucs VACHEMENT STYLES QUAND MEME


def get_seat_id(data):
    x = int("".join(["1" if i == "B" else "0" for i in data[:7]]),2)
    y = int("".join(["1" if i == "R" else "0" for i in data[7:]]),2)  
    return x * 8 + y

du coup on peut faire mieux :
"""
def seat_id(data):
    x = int("".join(["1" if i in ["B","R"] else "0" for i in data[:10]]),2)
    return(x)






