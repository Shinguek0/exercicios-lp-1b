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

forToString()