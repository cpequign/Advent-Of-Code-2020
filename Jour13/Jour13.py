with open("Jour13.txt","r") as f:
    val = [ligne.split(',') for ligne in f]
    
def part1():
    start = int(val[0][0])
    ecart = []
    ID = []
    for l in val[1]:
        if l =='x':
            continue
        else:
            l = int(l)
            if not start % l:
                print(0)
                return(0)
            else:
                ecart.append(l - start%l)
                ID.append(l)
    m = min(ecart)
    i = ecart.index(m)
    print(ID[i]*m)
    return(None)

part1()
        

def positions():
    pos = []
    ID = []
    for l in val[1]:
        if l=='x':
            continue
        else:
            pos.append(int(l)-val[1].index(l))
            ID.append(int(l))
    print(pos)
    print(ID)
    return(pos,ID)

positions()

#Will take insane amont of time
def part2():
    start = 0
    pos,ID = positions()
    test = True
    while test:
        for p in range(len(pos)):
            t = True
            ecart = pos[p]
            identite = ID[p]
            if t and (start + ecart) % identite:
                t = False
                start += pos[0]
            if t and p == len(pos) -1:
                print(start)
                return(None)
            
def solve_crt(a: list, m: list):
    """
    Solve according to chinese remainder theorem
    Implementation follows this tutorial
    https://www.youtube.com/watch?v=0dbXaSkZ-vc&ab_channel=CenterofMath
    Examples:
    >>> a = [0, 12, 55, 25, 12]
    >>> m = [7, 13, 59, 31, 19]
    >>> solve_crt(a, m)
    1068781
    >>> a = [2, 3, 2]
    >>> m = [3, 5, 7]
    >>> solve_crt(a, m)
    23
    """
    M = 1
    for v in m:
        M *= v
    Mi = [M // m[i] for i in range(len(m))]
    yi = [inverse(Mi[i], m[i]) for i in range(len(m))]

    X = sum([a[i] * Mi[i] * yi[i] for i in range(len(yi))])
    return X % M



def inverse(a: int, n: int):
    """
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    Find t such that a*t ≋ 1 (mod n)
    Examples:
    >>> inverse(3, 11)
    4
    which satisfies 3*4 ≋ 1 (mod 11)
    """

    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += n

    return t







pos, ID = positions()
print(solve_crt(pos,ID))