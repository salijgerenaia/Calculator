#advanced asevtkvat high-order funkciebis biblioteka
from functools import reduce

#shekrebis funkcia + shekvanili input ricxvebi userismier
def addition(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersSum = sum(newList)
    return NumbersSum

#gamoklebis function
def subtraction(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersSub = newList[0] - sum(newList[1:])
    return NumbersSub

#gamravlebis function
def multiplication(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersMult = reduce(lambda x, y: x*y, newList)
    return NumbersMult

#gakopis function
def division(*args):
    newList = []
    for i in inputList:
        z = int(i)
        newList.append(z)
    NumbersDiv = reduce(lambda x, y: x/y, newList)
    return NumbersDiv

#bechdavs mocemul teksts
print("AIRCHIET MOKMEDEBA\n" +
      "1 -> SHEKREBA\n" +
      "2 -> GAMOKLEBA\n" +
      "3 -> GAYOPA\n" +
      "4 -> GAMRAVLEBA\n")

#archevanis inputi dabechdili mokmedebebis
choice = int(input("GTOXVT SHEIYVANOT MOKMEDEBIS NOMERI: "))
if 1 <= choice <= 4:
    print("SHEIKVANET CIFREBI: ")
    print("GTXOVT SHEIKVANOT CIFREBI MAGALITIS MSGAVSAD : 5 5 5 5 5 5 (TKVENTVIS SASURVELI)")
    inputList = input().split()

#archevanis if-elif 
    if choice == 1:
        varList = addition(inputList)
        print("TKVENI SHEKVANILI CIFREBIS JAMIA: ", varList)
    elif choice == 2:
        varList = subtraction(inputList)
        print("TKVENI SHEKVANILI CIFREBIS SXVAOBAA: ", varList)
    elif choice == 3:
        varList = multiplication(inputList)
        print("TKVENI SHEKVANILI CIFREBIS GANAKOPIA: ", varList)
    elif choice == 4:
        varList = division(inputList)
        print("TKVENI SHEKVANILI CIFREBIS NAMRAVLIA: ", varList)
else:
    #bechdavs amas im shemtxvevashi tu Userma airchia 1-4 cifrebs shoris sxva ram
    not_valid = "{}, TKVEN VER AIRCHIET MOKMEDEBA SWORAD, GTXOVT AIRCHIO (1-4) SHUALEDSHI TKVENTVIS SASURVELI CIFRI\n".format(choice)
    print(not_valid)