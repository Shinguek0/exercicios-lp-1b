#Faça um programa que jogue par ou impar com o computador. O jogo será interrompido quando o jogador
#perder. Mostre ao final, o total de vitórias consecutivas que o jogador conquistou no jogo.

import random

choice = int(input("Você escolhe par <1> ou impar <2>"))


n = random.randrange(1,2)
print(n)

if(num%2==0):
    print("par ganhou")
else:
    print("impar ganhou")