#Faça um programa que peça dois números e imprima o maior deles.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

if (n1 > n2):
    print("O numero ", n1 , "é maior que o numero:", n2)
else:
    print("O numero ", n2 , "é maior que o numero:", n1)