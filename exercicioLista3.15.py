#Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
#perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.

import random
jogador = True

while(jogador):
    choice = int(input("Você escolhe par <1> ou impar <2>: "))
    num1 = int(input("Escolha um numero de 1 a 5: "))

    num = random.randrange(1,6)
    numTotal = num + num1

    if((choice==1)and(numTotal%2==0)):
        print("Você: {}\nComputador: {}\n".format(num1,num))
        print("Você ganhou!!\n----------------------------------------")
    elif((choice==2)and(numTotal%2!=0)):
        print("Você: {}\nComputador: {}\n".format(num1,num))
        print("Você ganhou!!\n----------------------------------------")
    else:
        print("Você: {}\nComputador: {}\n".format(num1,num))
        print("Você perdeu!\n----------------------------------------")
        jogador = False