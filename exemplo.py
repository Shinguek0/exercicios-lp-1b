butt = 1
while butt != 2:
    nome = int(input('\n'"Digite uma numer de 1 a 10: "))
    while nome > 10 or nome < 0:
        print("wrong!!")
        nome = int(input('\n'"Digite uma numer de 1 a 10: "))

    if(nome==8):
        print('\n'"acerto!!")
    else:
        print("errou!!")

    print('\n' "tentar novamente? ")
    butt = int(input("<1>sim <2>nao"))

n1 = 10
n2 = 15
s= n1 + n2

print("n1 é : {} e o n2 eh {} e a soma dos dois eh {}".format(n1,n2,s))
    