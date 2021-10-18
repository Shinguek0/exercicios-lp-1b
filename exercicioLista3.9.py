#Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

pesos = []

for i in range(5):
    pesos.append(float(input("Digite o seu peso: ")))

print(max(pesos),"foi o maior peso, e o menor peso foi",min(pesos),)