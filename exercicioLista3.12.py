#Crie um programa que leia dois valores e mostre na tela um menu :
#1. Somar
#2. Multiplicar
#3. Maior
#4. Menor
#5. Sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso
n = []
n.append(float(input("Digite um valor: ")))
n.append(float(input("Digite outro vaor: ")))

choice = int(input("Escolha a operação: \n<1> Somar\n<2> Multiplicar\n<3> Maior\n<4> Menor\n<5> Sair do programa\n"))

if(choice==1):
    print(f"{n[0]} + {n[1]} = {n[0]+n[1]}")
elif(choice==2):
    print(f"{n[0]} x {n[1]} = {n[0]*n[1]}")
elif(choice==3):
    print(f"Entre {n[0]} e {n[1]}, o numero {max(n)} é maior")
elif(choice==4):
    print(f"Entre {n[0]} e {n[1]}, o numero {min(n)} é o menor")
elif(choice==5):
    pass