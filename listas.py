#https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html
# site explicandos uns bagui de lista

#

#criando listas
nomeLista = []
numLista = [1,2,3,4,10.5,14.5]
commLista = []

def sortedRevers():
    listaSorted = [1,32,43,5,46,4]
    print(sorted(listaSorted))
    print(list(reversed(listaSorted)))
    print(listaSorted)
    listaSorted.reverse()
    print(listaSorted)

    numMin = min(listaSorted)       # menor numero da lista
    numMax = max(listaSorted)       # maior numero da lista
    somaTotal = sum(listaSorted)    # soma de todos os numeros da lista
    print(somaTotal)

    soma1 = min(listaSorted) + max(listaSorted)
    soma2 = numMax + numMin
    print(numMin,numMax,soma1,soma2)

def deletarDaLista():
    # Deletar um item da lista
    delLista = ["a","b","c","d","e"]
    delLista.append("So pra deleta") # adicionei so pra deleta
    print(delLista)
    del delLista[-1]  #deleta o index[-1] que eh o ultimo.
    print(delLista)
    del delLista[2:]  #deleta do index[2] pra frente
    print(delLista)

    removeLista = ["um", "dois" , "tres", "quatro", "um"]  #Lista criada para testar o remove
    print(removeLista)
    removeLista.remove("um")  #remove o prieiro indeice que achar
    print(removeLista)

def allListComands():
    print(commLista)
    commLista.append("Jorge henrique") #append adiciona algo no final da lista.
    print(commLista)
    commLista.insert(0, "Ricardo cisero") #insert escolhe [index] (lugar da lista) onde botar o item novo
    print(commLista)
    commLista.insert(7, "jose dinisio") #insert se nao tiver ea posiçao apenas coloca na mais prossima
    print(commLista)
    commLista[0] = "Outro cara"         #Subistutui um item na lista
    print(commLista)

    print(len(commLista))  # printa o tamanho da lista
    x = len(commLista)     # ""
    print(x)               # ""

    print(commLista.index("jose dinisio")) # procura um item em uma lista
    x = commLista.index("Jorge henrique")  # ""
    print(x)                               # ""

    print(commLista[0:2])  # printa do index[0] ate < 2
    print(commLista[1:])   # printa tudo depois de index (pode ser antes tambem)

    listacopia = commLista.copy()  # copia as coisas de uma lista pra outra
    commLista.clear()  # limpa os dados da lista

    print(commLista)
    print(listacopia)

    gg  = listacopia.pop(1)   # Pop remove um item da lista, e da de salvar numa variavel o intem salvo
    print(listacopia)
    print(gg)

    maisUmaLista = ["um","dois","tres","quatro","cinco","um","dois","um"]
    print(maisUmaLista.count("um"))     #Couunt serve para ver quanta vezes algo se repete na lista
    print(maisUmaLista.count("dois"))   #


def appednComInput():
    x = 0
    while x < 5:
        nomeLista.append(input("Digite um nome: "))
        x+=1
    for i in nomeLista:
        print(i)

def imprimeLista():
    for i in numLista:
        print(i)     

print("<1> usar input na lista <2> Imprimir tudo da lista <3> comandos da lista")
escolha = int(input())

if escolha == 1:
    appednComInput()
elif escolha == 2:
    imprimeLista()
elif escolha == 3:
    allListComands()
elif escolha == 4:
    deletarDaLista()
elif escolha == 5:
    sortedRevers()
else:
   print("nop")