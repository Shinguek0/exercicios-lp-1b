#Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a
#operação de multiplicação ou de divisão e que, a partir desta escolha, mostre o resultado na tela.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

print("Voce deseja relizar uma conta de multiplicaçao ou de divisao?")
print("          <1> multiplicaçao       <2> divisao")
op = int(input(""))

if(op==1):
    print("A multiplicaçao dos numeros é: ", n1*n2)
elif(op==2):
    print("A divisao dos numeros é: ", n1/n2)
else:
    print("Operaçao invalida")