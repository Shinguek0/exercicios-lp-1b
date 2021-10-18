#Faça um script que leia um número inteiro e diga se ele é ou não um número primo. Obs: numero primo é
#apenas os números que são divisíveis por um e por ele mesmo..
num = int(input("Digite um numero pra saber se ele é primo: "))
x= 0
for i in range(2,10):
    if ((num%i!=0)or(num==i)):
        continue
    else:
        x+=1
if (x==0):
    print("É primo!")
else: 
    print("Não é primo!!")