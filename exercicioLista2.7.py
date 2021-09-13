#Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja
#“sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha. No caso de o usuário
#responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha.

print("Digite você tem irmãos?")
print("   <1>Sim <2>Não")
p1 = int(input(""))

if(p1 == 1):
    qtdIrmaos = int(input("Qual a quantidade de irmãos?"))
    if(qtdIrmaos<=0):
        print("Entao voce nao tem irmaos!")
    else:
        print("Você tem",qtdIrmaos,"irmãos")
elif(p1 == 2):
    print("Você queria ter irmãos?")
    print("   <1>Sim <2>Não")
    choice = int(input(""))
    if (choice == 1):
        print("O usuario gostaria de ter irmaos")
    elif(choice == 2):
        print("O usuario nao gostaria de ter irmaos")
    else:
        print("resposta invalida")
else:
    print("resposta invalida")