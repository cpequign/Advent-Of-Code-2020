FILENAME = "Jour4.txt"



with open(FILENAME) as f:
    lines = f.readlines()


    

donnee = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
y = len(lines)
eyecolor = ["amb","blu","brn","gry","grn","hzl","oth"]
abcdef = "abcdef"


x = 0
valide = 0
while x<y:
    compteur = 0
    while x<y and lines[x] != "\n":
        for d in donnee:
            if d in lines[x]:
                
                if d == "byr":
                    ind = lines[x].index(d)
                    if len(lines[x]) >= ind+8:
                        if 1920 <= int(lines[x][ind+4:ind+8]) <= 2002:
                            compteur +=1
                
                
                
                
                
                elif d == "iyr":
                    ind = lines[x].index(d)
                    if len(lines[x]) >= ind+8:
                        if 2010 <= int(lines[x][ind+4:ind+8]) <= 2020:
                            compteur +=1        
                
                
                
                
                
                
                elif d == "eyr":
                    ind = lines[x].index(d)
                    if len(lines[x]) >= ind+8:
                        if 2020 <= int(lines[x][ind+4:ind+8]) <= 2030:
                       
                            compteur +=1                    
                
                
                
                
                
                
                elif d == "hgt":
                    ind = lines[x].index(d)
                    if len(lines[x]) >= ind+9:
                        if lines[x][ind+6:ind+8] == "in":
                            if 59 <= int(lines[x][ind+4:ind+6]) <= 76:
                
                                compteur+=1
                        
                    if len(lines[x]) >= ind+9:
                        if lines[x][ind+7:ind+9] == "cm":
                            if 150 <= int(lines[x][ind+4:ind+7]) <= 193:
                                              
                                compteur += 1





                elif d == "hcl":
                    ind = lines[x].index(d)
                    test = True
                    if len(lines[x]) >= ind+10:
                        if lines[x][ind+4] != "#":
                            test = False
                        for i in range(ind+5,ind+8):
                            if not lines[x][i] in "abcdef0123456789":
                                test = False
                        for j in range(ind+8,ind+11):
                            if not lines[x][i] in "abcdef0123456789":
                    
                                test = False
                                
                    else:
                        test = False
                    if test:
              
                        compteur+=1
                        
                        
                        
                
                elif d == "ecl":
                    ind = lines[x].index(d)
                    if len(lines[x]) >= ind+7:
                        a = lines[x][ind+4:ind+7]
                        if a in eyecolor:
                
                            compteur +=1
                            
                            
                            
                elif d == "pid":
                    ind = lines[x].index(d)
                    
                    test = True
                    if len(lines[x]) >= ind+14:
                        for j in range(ind+4,ind+13):
                            if not lines[x][j] in "0123456789":
                                test = False
                    else:
                        test = False
                    if test:
            
                        compteur+=1
                        
                        
                    
                        
        
        x +=1
        if x<y and lines[x] == "\n":
            print(compteur)
            if compteur == 7:
                valide +=1
                
            compteur = 0
            x+=1

        
print(valide)
            


