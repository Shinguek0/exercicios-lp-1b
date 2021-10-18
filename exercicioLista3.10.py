#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa mostre:
# a. A media de idade do grupo;
# b. Qual é o nome do homem mais velho;
# c. Quantas mulheres tem menos de 20 anos

idade = []
nome = []
sexo = []
maiorIdade=0
mulherMenor=0

for i in range(4):
    nome.append(input("Digite seu nome: "))
    idade.append(int(input("Digite sua idade: ")))
    sexo.append(input("Digite seu sexo [M/F]: ").upper())

print("A media de idade do grupo é: ",sum(idade)/2)
for i in range(4):
    if (sexo[i]=="M"):
        if(idade[i]>maiorIdade):
            maiorIdade=idade[i]
    else:
        if(idade[i]<20):
            mulherMenor+=1


print(nome[idade.index(maiorIdade)],"é o nome do homem mais velho")
print("{} mulheres tem menos de 20 anos".format(mulherMenor))