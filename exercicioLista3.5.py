#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
#Se o valor digitado for ímpar desconsidere-o.

lista = []

for i in range(6):
    lista.append(int(input("Digite um numero: ")))
    if(lista[i]%2==0):
        print(lista[i],"É par")
