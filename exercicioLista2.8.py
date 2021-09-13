#Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela
#a bebida escolhida.
print("Escolha entre uma das tres bebidas: ")
print("<1> Guarana\n<2> Toddy\n<3> Nesquik") 
r = int(input(""))
if (r == 1):
    print("Você escolheu guarana")
elif(r == 2):
    print("Você escolheu toddy")
elif(r == 3):
    print("Você escolheu nesquik")
else:
    print("Bebida invalida")