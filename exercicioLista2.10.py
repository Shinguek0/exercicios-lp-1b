# Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a
# operação de adição ou de subtração e, que a partir desta escolha, mostre o resultado na tela.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite um numero: "))

print("Voce deseja relizar uma conta de adiçao ou de subtração?")
print("           <1> adição       <2> subtração")
op = int(input(""))

if(op==1):
    print("A soma dos numeros é: ", n1+n2)
elif(op==2):
    print("A diferença dos numeros é: ", n1-n2)
else:
    print("Operaçao invalida")