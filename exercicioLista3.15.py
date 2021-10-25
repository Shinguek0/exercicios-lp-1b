#Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
#perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.

import random
vitorias = 0
maxvitorias = 0
cond = ""

while (cond!="N"):
    choice = 0
    while(choice<1 or choice>2):
        choice = int(input("Você escolhe par <1> ou impar <2>: "))
    
    num1 = int(input("Escolha um numero de 1 a 10: "))

    num = random.randint(1,10)
    numTotal = num + num1

    if((choice==1)and(numTotal%2==0)):
        vitorias+=1
        print("Você: {}\nComputador: {}\n".format(num1,num))
        print("Você ganhou!!\nVitorias consecutivas:",vitorias,"\n----------------------------------------")
    elif((choice==2)and(numTotal%2!=0)):
        vitorias+=1
        print("Você: {}\nComputador: {}\n".format(num1,num))
        print("Você ganhou!!\nVitorias consecutivas:",vitorias,"\n----------------------------------------")
    else:
        vitorias = 0
        print("Você: {}\nComputador: {}\n".format(num1,num))
        print("Você perdeu!\n----------------------------------------")
    if(vitorias>maxvitorias):
        maxvitorias=vitorias
    cond = input("Você deseja continuar?\n(S/N) ").upper()

print("Maior numero de vitorias consecutivas: ",maxvitorias)