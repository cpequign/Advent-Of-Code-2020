import itertools as it
with open("Jour17Test.txt","r") as f:
    val = [ligne for ligne in f]
    
lign = len(val)
column = len(val[-1])

neighbor = []
for i in range(-1,2):
    for j in range(-1,2):
        for k in range(-1,2):
            if i !=0 or j!=0 or k!= 0:
                neighbor.append([i,j,k])
            
            
def init():
    tab = [ [ ['.' for j in range(column+6*2) ] for i in range(lign+6*2)] for z in range(11) ]
    for i in range(lign):
        for j in range(column):
            tab[5][i][j] = val[i][j]
    return(tab)
                    

tab = init()

def count_neighbor(z,x,y):
    c = 0
    for dz,dx,dy in neighbor:
        if 0 <= z+dz <= 4 and 0 <= x+dx < lign and 0 <= y+dy < column:
            if tab[z+dz][x+dx][y+dy] == '#':
                c +=1
    return(c)
            

from copy import *

def part1(tab):
    for n in range(6):
        copie = deepcopy(tab)
        for z in range(11):
            for x in range(lign+2*n):
                for y in range(column+2*n):
                    c = count_neighbor(z,x,y)
                    if tab[z][x][y] =='#':
                        if c==2 or c==3:
                            copie[z][x][y] = '#'
                        else:
                            copie[z][x][y] = '.'
                    else:
                        if c==3:
                            copie[z][x][y] = '#'
                        else:
                            copie[z][x][y] = '.'
    
        tab = copie
    c = 0
    
    for z in range(z):
        for x in range(lign):
            for y in range(column):
                if tab[z][x][y] =='#':
                    c +=1
    print(c)
    return(c)

#part1(tab)


#ET AVEC DES DICOS

def init2():
    d = {}
    for z in range(-10,11):
        for x in range(-8,lign+8):
            for y in range(-8,column+8):
                if z ==0 and 0 <= x < lign and 0 <= y < column:
                    d[z,x,y] = val[x][y]
                else:
                    d[z,x,y] = '.'
    return(d)

d = init2()


def count_neighbordic(z,x,y):
    c = 0
    for dz,dx,dy in neighbor:
        if d[z+dz,x+dx,y+dy] == '#':
            c +=1
    return(c)                        

def part1dic(d):
    for n in range(6):
        copie = deepcopy(d)
        for z in range(-6,7):
            for x in range(-6,lign+7):
                for y in range(-6,column+7):
                    c = count_neighbordic(z,x,y)
                    if d[z,x,y] =='#':
                        if c==2 or c==3:
                            copie[z,x,y] = '#'
                        else:
                            copie[z,x,y] = '.'
                    else:
                        if c==3:
                            copie[z,x,y] = '#'
                        else:
                            copie[z,x,y] = '.'

        d = copie
    
    c = 0
    for e in d:
        if d[e] == '#':
            c+=1
    print(c)
    return(c)


part1dic(d)


