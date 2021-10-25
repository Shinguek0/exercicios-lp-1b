#Faça um sistem de aposta onde o usuario entra com o seu saldo, e ele possa apostar se o numero de uma
#roleta aleatoria vai cair par ou impar, se ele acertar ele ganha o dobro do que apostou, e se ele errar ele
#perde a quantia que apostou, o programa deve parar quando o saldo do cara acabar, ou quando ele desejar sair

from random import randint

saldo = float(input("Digite o seu saldo: "))
while True:
    aposta = float(input("Digite o valor de sua aposta: R$"))
    choice = int(input("Você aposta em par <1> ou impar <2> "))
    print("-"*50)
    x = randint(0, 100)
    if ((x%2==0)):
        print("Caiu o numero {}º, e ele é par".format(x))
        if(choice==1):
            saldo+=aposta*2
            print("Você acertou!!")
        else:
            saldo-=aposta
            print("Você errou!!")
    else:
        print("Caiu o numero {}º, e ele é impar".format(x))
        if(choice==2):
            saldo+=aposta*2
            print("Você acertou!!")
        else:
            saldo-=aposta
            print("Você errou!!")
    print("Seu saldo agora é:",saldo)
    cond = input("\nVoce deseja sair?\n(S/N)").upper()
    print("-"*50)
    if((saldo<=0)or(cond=="S")):
        print("Você desejou sair, ou está sem saldo.")
        break