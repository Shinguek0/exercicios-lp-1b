# if e for :)
import random

def fibomath():
    jorge = [1]
    a = 0
    p = 0
    item = 0
    for item in jorge:
        jorge.append(item + p) 
        print(item)
        p = item
        if(item > 1000):
            break
    print("-o- ",jorge)


def forToString():
    palavras = ["jorginho","roberto","carlos","yuri","samael","hikyuu","ribamar","fegussan","valeria","attack on titan"]
    mistake = 0
    rand = random.randint(0,9)
    palavra = palavras[rand]
    for x in palavra:
        print(palavras[rand])
        ab=False
        while ab == False:
            cha = input("...")
            if (cha == x):
                print("")
                ab = True 
            elif(cha == "" or cha == " " or cha == "  "):
                print("preencha com algo")  
            else:
                print("mistake")
                mistake += 1
    else:
        print("nice cock")
        print(mistake, " Mistakes")

def forstyling():
    for i in range(1,10,2): #Printa de 2 em 2 dos numeros de 1 a 10
        print(i)

    for i in range(10,1,-1): #Printa os numeros de 10 a 1, de 1 em 1
        print(i)

    for i in range(1, 10): #Printa os numeros de 1 a 10
        print(i, end=" ")  #O end serve pra formatar a forma de printa
    print("")  #so pra dar espaço
    for i in range(1, 10): #Printa os numeros de 1 a 10
        print(i, end=" <-> ")  #O end serve pra formatar a forma de printa

def breakcontinue():
    for i in range(10):
        if(i == 4):
            break
        else:
            print(i)

interupitor = int(input("-->"))
if (interupitor==1):
    fibomath()
elif(interupitor==2):
    forToString()
elif(interupitor==3):
    forstyling()
elif(interupitor==4):
    breakcontinue()