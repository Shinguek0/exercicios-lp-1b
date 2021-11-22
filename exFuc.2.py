#2)	Faça uma função que computa a potência ab para valores a e b (assuma números inteiros)
#  passados por parâmetro.

def ab(a,b):
    return a**b

x = int(input("Digite o numero a ser potavel: "))
y = int(input("Digite o numero da potencia: "))
print(ab(x,y))