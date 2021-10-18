#Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada, utilizando o laço for.

num = int(input("Digite um numero para receber sua tabuada: "))
fin = int(input("Digite ate que tabuada você quer: "))

for i in range(1,fin+1):
    print(num,"x",i," = ",num*i)