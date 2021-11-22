with open("Jour19.txt","r") as f:
    val = [ligne.split('\n')[0] for ligne in  f]

rules = val[:val.index('')]
messages = val[val.index('')+1:]
nbrules = [(l[:l.index(':')],l) for l in rules]

#Dictionnary for the rules
# d["0"] = ["4","1","5"]

def dico():
    d = {}
    for l in rules:
        n,follow = l[:l.index(':')], l[l.index(':')+1:].split(' ')[1:]
        d[n] = follow
    return(d)

d = dico()
 
def follows(message,indice,nbr): #message en question, indice actuel du message, numéro de la règle à suivre

    if d[nbr] == ['"a"']:
        if message[indice] == "a":       
            return(True,indice+1)
        else:
            return(False,0)
        
    elif d[nbr] == ['"b"']:        
        if message[indice] == "b":
            return(True,indice+1)
        else:
            return(False,0)
        
    elif '|' in d[nbr] and len(d[nbr]) == 5: #or    
        test1, i1 = follows(message,indice,d[nbr][0])
        test2, i2 = follows(message,i1,d[nbr][1])
        test3, i3 = follows(message,indice,d[nbr][3])
        test4, i4 = follows(message,i3,d[nbr][4])
        if not ((test1 and test2) or (test3 and test4)):
            return(False,0)
        if (test1 and test2):
            return(True,i2)
        
        elif (test3 and test4):
            return(True,i4)
        
    elif '|' in d[nbr] and len(d[nbr]) == 3:
        test1, i1 = follows(message,indice,d[nbr][0])
        test2, i2 = follows(message,indice,d[nbr][2])
        if not (test1 or test2):
            return(False,0)
        if test1:
            return(True,i1)
        elif test2:
            return(True,i2)
    
    else:
        n = len(d[nbr])
        for j in range(n):
            test, indice = follows(message,indice,d[nbr][j])
            if not test:
                return(False,0)
            
        if nbr == '0':
            if indice == len(message):
                return(True,0)
            else:
                return(False,0)
        else:
            if test:
                return(True,indice)
            else:
                return(False,0)




#The message has to follow the rule 0.

def part1():
    c = 0
    for message in messages:
        print('message',message)
        if follows(message,0,'0')[0]:
            c += 1
    print(c)
    return(c)

#part1()


def follows2(message,indice,nbr,compt): #message en question, indice actuel du message, numéro de la règle à suivre
    if indice > len(message):
        return(False,0)
    compt += 1
    if d[nbr] == ['"a"']:
        if message[indice] == "a":       
            return(True,indice+1)
        else:
            return(False,0)
        
    elif d[nbr] == ['"b"']:        
        if message[indice] == "b":
            return(True,indice+1)
        else:
            return(False,0)
        
    elif '|' in d[nbr] and len(d[nbr]) == 5: #or    
        test1, i1 = follows2(message,indice,d[nbr][0],compt)
        test2, i2 = follows2(message,i1,d[nbr][1],compt)
        test3, i3 = follows2(message,indice,d[nbr][3],compt)
        test4, i4 = follows2(message,i3,d[nbr][4],compt)
        if not ((test1 and test2) or (test3 and test4)):
            return(False,0)
        if (test1 and test2):
            return(True,i2)
        
        elif (test3 and test4):
            return(True,i4)
        
    elif '|' in d[nbr] and len(d[nbr]) == 3:
        test1, i1 = follows2(message,indice,d[nbr][0],compt)
        test2, i2 = follows2(message,indice,d[nbr][2],compt)
        if not (test1 or test2):
            return(False,0)
        if test1:
            return(True,i1)
        elif test2:
            return(True,i2)
        
    elif nbr == '8':
        test1, i1 = follows2(message,indice,d[nbr][0],compt)
        test2, i2 = follows2(message,indice,d[nbr][2],compt)
        test3, i3 = follows2(message,i2,d[nbr][3],compt)
        if not (test1 or (test2 and test3)):
            return(False,0)
        if test1:
            return(True,i1)
        elif test2:
            return(True,i3)   
    elif nbr == '11':
        test1, i1 = follows2(message,indice,d[nbr][0],compt)
        test2, i2 = follows2(message,i1,d[nbr][1],compt)
        test3, i3 = follows2(message,indice,d[nbr][3],compt)
        test4, i4 = follows2(message,i3,d[nbr][4],compt)
        test5, i5 = follows2(message,i4,d[nbr][5],compt)
        if not ((test1 and test2) or (test3 and test4 and test5)):
            return(False,0)
        if test1:
            return(True,i2)
        elif test2:
            return(True,i5)     
    
    else:
        n = len(d[nbr])
        for j in range(n):
            test, indice = follows2(message,indice,d[nbr][j],compt)
            if not test:
                return(False,0)
            
        if nbr == '0':
            if indice == len(message):
                return(True,0)
            else:
                return(False,0)
        else:
            if test:
                return(True,indice)
            else:
                return(False,0)
            
def part2():
    c = 0
    for message in messages:
        print('message',message)
        if follows2(message,0,'0',0)[0]:
            c += 1
    print(c)
    return(c)

part2()


























            