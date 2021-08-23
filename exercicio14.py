#14)Faça um programa que leia um número inteiro e mostre na tela a sua tabuada

n = int(input("Digite o numero que você deseja a tabuada: "))
i = 0
while(i < 10):
    i+=1
    print(n,"x",i,"=",(n*i))