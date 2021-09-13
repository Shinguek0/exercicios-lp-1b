#Escreva o menu de opções abaixo. Leia a opção do usuario e execute a operação escolhida.
#Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
#• Soma de 2 n´umeros.
#• Diferença entre 2 números (maior pelo menor).
#• Produto entre 2 números.
#• Divisão entre 2 números (o denominador não pode ser zero)
n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print("")
print("Escolha uma operação: ")
print("<1>Soma\n<2>diferença\n<3>produto\n<4>divisao\n")
esc = int(input(""))

if (esc == 1):
    print("A soma dos dois numeros é",n1+n2)
elif(esc==2):
    print("A soma dos dois numeros é",n1+n2)
elif(esc==3):
    print("A soma dos dois numeros é",n1+n2)
elif(esc==4):
    print("A soma dos dois numeros é",n1+n2)
else:
    print("Nao é uma escolha valida")