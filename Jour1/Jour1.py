valeurs = open("Jour1.txt","r") #mode lecture

val = valeurs.readlines()
l = []
for ligne in val:
    l.append(int(ligne))
    


for i in range(len(l)-2):
    for j in range(i+1,len(l)-1):
        for k in range(j+1,len(l)):
            if l[i]+l[j]+l[k] == 2020:
            
                print("la somme vaut 2020",)
                print("le produit vaut : ",l[i]*l[j]*l[k])
