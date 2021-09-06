#Escreva um Programa que leia uma lista de 5 números inteiros, mostre a soma deles.
lista = []
i = 0
while i < 5:
    lista.append(int(input("Digite um numero: ")))
    i+=1

print(sum(lista))