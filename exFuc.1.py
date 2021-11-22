#1)	Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
x = ""
def qtdN(a):
    print(len(a))

while(x != "S"):
    x = input("Digite o numero: ")
    qtdN(x)