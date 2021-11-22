#3)	Faça um programa que tenha uma função chamada voto() que vai receber como parametro 
# o ano de nascimento de alguém, e irá retornar um valor indicando se essa pessoal tem voto negado
#  opcional ou obrigatório nas eleições.

def voto(ano):
    if(ano>2003):
        return False
    else: 
        return True

x = int(input("Digite o ano do seu nascimento: "))
print(voto(x))