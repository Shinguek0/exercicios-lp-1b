#Faça um script que peça um valor e mostre na tela se o valor é positivo ou negativo.Faça um script que peça
# um valor e mostre na tela se o valor é positivo ou negativo.

valor = int(input("Digite um numero inteiro: "))

if (valor < 0):
    print("O numero",valor,"é negativo")
elif(valor==0):
    print("O numero",valor,"é igual a zero")
else:
    print("O numero",valor,"é positivo")