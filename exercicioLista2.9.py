#. Faça um programa que peça para o usuário inserir dois números e que verifique qual é o maior
#ou se eles são iguais.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if (n1 > n2):
    print("O numero",n1,"é maior que o numero",n2)
elif(n2 > n1):
    print("O numero",n2,"é maior que o numero",n1)
else:
    print("O numero",n1,"é igual ao numero",n2)