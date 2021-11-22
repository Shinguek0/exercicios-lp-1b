
def allIknow():
    print("Nothing :)")

allIknow()


# Input

def theKilller(a=0,b=0,c=0):
    if(a<1 or b<1 or c<1):
        print("O valor nao pode ser 0")
    else:
        print(a+b+z)

x = int(input("A: "))
y = int(input("B: "))
z = int(input("C: "))


theKilller(x,y,z)

#varios valores

#def val(*n);
   # print(":")


# Return

def retur(a,b,c):
    s = a+b+c
    return s

print(retur(2,3,6))


# Return de 2 valores

def cadastro():
    nome = input("Digite o seu nome: ")
    idade = int(input("Digite sua idade: "))
    return nome,idade

nome, idade = cadastro()
print(nome,idade)


def par(n=0):
    if n%2 == 0:
        return True
    else:
        return False

a = ""
while a!="S":
    x = int(input("Digite um numero par: "))
    if(par(x)):
        print("É par!!")
    else:
        print("É impar!")
    a = input("você deseja encerrar(S/N)").upper()

#expressao lambda

def quadrado(x):
    return x**2

print(quadrado(2),"Usando func")
print(quadrado(5),"Usando func")

print((lambda x:x**2)(8),"Lambda") #lambda

#xx

x = lambda a,b:a+b
print(x(2,3), "Lambida em uma variavel")