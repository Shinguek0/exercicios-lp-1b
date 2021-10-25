#faça um programa que funcione como uma lista de afazeres, onde o usuario pode adicionar itens e remover, e
#os itens removidos, devem ser guardados em uma lista de tarefas cumpridas que o usuario tambem pode ver

listaAfaz = []
tarefasCumpridas = []

while True:

    print("O que você deseja fazer: ")
    choice = int(input("<1> Adicionar um item à lista\n<2> Remover um item da lista\n<3> Ver os itens na lista\n<4> Ver lista de tarefas cumpridas\n<5> Finalizar programa"))
    if(choice==1):
        print(listaAfaz)
        listaAfaz.append(input("Digite o que voce deseja adicionar: \n"))
    elif(choice==2):
        print(listaAfaz)
        tarefasCumpridas.append("a")
    elif(choice==3):
        print(listaAfaz)
    elif(choice==4):
        print(tarefasCumpridas)
    elif(choice==5):
        break
    else:
        print("voce digitou algo errado tente novamente!")