#Desenvolva um programa que leia o primeiro termo e a razão de uma progressão aritmética. No final, mostre os
#10 primeiros termos dessa progressão.

num = int(input("Digite o termo inicial: "))
razao = int(input("Digite a razão da progressão aritmética:"))

ultimo = num + (10 - 1)*razao
ultimo = ultimo + 1

for var in range (num, ultimo, razao):
    print(var)