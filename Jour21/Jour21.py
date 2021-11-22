filename = open("Jour21.txt","r")

lines = []
for l in filename:
    lines.append(l)
    
def intersect(food,l1):
    if Dic_food[food] == []:
        Dic_food[food] = l1
        return()
    else:
        l2 = Dic_food[food]
        l3 = []
        for e in l1:
            if e in l2:
                l3.append(e)
        Dic_food[food] = l3
        return()

Dic_food = {}
def readfood(lines):
    for line in lines:
        l = line.split()
        cind = l.index('(contains')
        for i in range(cind+1,len(l)):
            f = l[i][:len(l[i])-1]
            Dic_food[f] = []     
    return()


L_ingredient = []
def readingredient(lines):
    for line in lines:
        l = line.split()
        cind = l.index('(contains')
        for i in range(cind):
            if l[i] not in L_ingredient:
                L_ingredient.append(l[i])
    return()
            
def readline(line):
    l = line.split()
    cind = l.index('(contains')
    ingredient = []
    for i in range(cind):
        ingredient.append(l[i])
    for i in range(cind+1,len(l)):
        f = l[i][:len(l[i])-1]
        intersect(f,ingredient)
    return()

readfood(lines)
readingredient(lines)

for line in lines:
    readline(line)
        
def is_allergen(ingredient):
    for f in Dic_food:
        if ingredient in Dic_food[f]:
            return(True)
    return(False)

Dic_ingredient = {}
def define_allergen():
    for ingredient in L_ingredient:
        Dic_ingredient[ingredient] = is_allergen(ingredient)
    return()
define_allergen()

def count_P1(lines):
    count = 0
    for line in lines:
        l = line.split()
        cind = l.index('(contains')
        for i in range(cind):
            ingredient = l[i]
            if not Dic_ingredient[ingredient]:
                count+=1
    return(count)

print("Le nombre devrait être : ",count_P1(lines))    


Other_dic = {}

Other_dic['nuts'] = 'qrmps'
Other_dic['wheat'] = 'qsjszn'
Other_dic['shellfish'] = 'qnvx'
Other_dic['dairy'] = 'cljf'
Other_dic['eggs'] = 'frtfg'
Other_dic['soy'] = 'cpxmpc'
Other_dic['fish'] = 'vvfjj'
Other_dic['peanuts'] = 'hvnkk'

l=[]
for f in Other_dic:
    l.append((f,Other_dic[f]))
    









