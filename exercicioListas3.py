#Escreva um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []
i = 0
while i < 4:
    notas.append(int(input("Digite sua nota: ")))
    i+=1

print("Notas",notas)
print("Media ",sum(notas)/len(notas))