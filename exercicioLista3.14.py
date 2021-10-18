#Crie um programa que leia vários números inteiros pelo teclado. No final, mostre a média entre todos os
#valores lidos e qual foi o maior e o menor valor lido. O programa deve perguntar ao usuário se ele quer ou
#não continuar a escrever valores.

rep = "N"
n = []

while(rep!="S"):
    n.append(int(input("Digite um valor: "))).upper()
    rep=input("Você deseja parar [S/N]: ")

print("A media de todos os valores é:",sum(n)/2)
print("O maior valor é:",max(n))
print("O menor valor é:",min(n))