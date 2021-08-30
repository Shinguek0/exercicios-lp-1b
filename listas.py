#https://panda.ime.usp.br/pensepy/static/pensepy/09-Listas/listas.html
# site explicandos uns bagui de lista

#pesquisar pra que serve o pop

#criando listas
nomeLista = []
numLista = [1,2,3,4,10.5,14.5]
commLista = []

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

    # Deletar um item da lista
    commLista.append("So pra deleta") # adicionei so pra deleta
    print(commLista)
    del commLista[-1]  #deleta o index[-1] que eh o ultimo.
    print(commLista)

    removeLista = ["um", "dois" , "tres", "quatro", "um"]  #Lista criada para testar o remove
    print(removeLista)
    removeLista.remove("u")  #remove o prieiro indeice que achar
    print(removeLista)

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
else:
   print("nop")