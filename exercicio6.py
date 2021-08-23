#6)	Faça um script que leia um número e mostre o seu dobro, seu triplo e a sua raiz quadrada.
import math
n = float(input("Digite um numero: "))
print("O dobro do numero {}, é {}".format(n,n*2))
print("O triplo do numero {}, é {}".format(n,n*3))
print("A raiz quadrada do numero {}, é {}".format(n,math.sqrt(n)))