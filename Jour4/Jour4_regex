import sys
import re


def is_valid(regex, string):
    pattern = re.compile(regex)
    return(pattern.match(string))


def check_line(myStr):
    attributes = myStr.split()
    nbAttributes = 0
    for attribute in attributes:
        if (is_valid("byr:(19[2-8][0-9]|199[0-9]|200[0-2])$", attribute)):
            nbAttributes += 1
        elif (is_valid("iyr:(201[0-9]|2020)$", attribute)):
            nbAttributes += 1
        elif (is_valid("eyr:(202[0-9]|2030)$", attribute)):
            nbAttributes += 1
        elif (is_valid("(hgt:(1[5-8][0-9]|19[0-3])cm)|(hgt:(59|6[0-9]|7[0-6])in)$", attribute)):
            nbAttributes += 1
        elif (is_valid("hcl:#[0-9a-f]{6}$",attribute)):
            nbAttributes += 1 
        elif (is_valid("ecl:(amb|blu|brn|gry|grn|hzl|oth)$", attribute)):
            nbAttributes += 1
        elif (is_valid("pid:[0-9]{9}$", attribute)):
            nbAttributes += 1
    return nbAttributes == 7

def valid_passport(mylist):
    nbValidPassports = 0
    myStr = ""
    for line in mylist:
        line = line.rstrip()
        if line != "":
            myStr += line + " "
        else:
            if (check_line(myStr)):
                nbValidPassports += 1
            myStr = ""
    if (check_line(myStr)):
                nbValidPassports += 1
    print(nbValidPassports)

def main():
    result = 1
    mylist = []
    tob = open("Jour4.txt","r")

    val = tob.readlines()
    for line in val:
       mylist.append(line) 
    valid_passport(mylist)

if __name__ == "__main__":
    main()