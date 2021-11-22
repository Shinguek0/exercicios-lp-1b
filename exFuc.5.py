#5)	Faça um programa que solicite o nome do usuário e a idade do usuário
#  depois disso exiba a mensagem: “{nome} possui {idade} anos.”.

def resp(nome,idade):
    print(nome,"possui", idade,"anos")

x = input("Digite seu nome: ")
y = input("Digite sua idade: ")

resp(x,y)