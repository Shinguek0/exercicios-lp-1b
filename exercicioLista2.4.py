#Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de
#idade ou não.

idade = int(input("Confirme sua idade: "))


if (idade < 0):
    print("Idade invalida")
elif(idade < 18):
    print("Voce nao é maior de idade")
else:
    print("Voce é maior de idade")