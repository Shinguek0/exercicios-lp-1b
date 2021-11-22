#4)	Faça um programa que tenha uma função ficha(), que receba dois parametros opcionais
#  o nome do jogador e a quantidade de gols ele marcou.

def ficha(nome,qtdGols):
    return nome,qtdGols

x = input("Digite o nome do jogador: ")
y = input("Digite a quantidade de gols: ")

# 1º jeito
print(ficha(x,y))

# 2º jeito
nome, qtdGols = ficha(x,y)
print(nome,qtdGols)