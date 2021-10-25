#Faça um sistema onde o usuario possa apostar em um cavalo, numa competiçao com 5 cavalos
#ele poderá apostar um valor qualquer, e o premio é o quintuplo do valor se o cavalo ganhar.
#é o triplo e se o cavalo chegar em segundo, e o dobro do valor se ele chegar em terceiro.
#no final do programa mostre o premio do usuario e a posição em que seu cavalo ficou.

from random import randint

print("Escolha um cavalo: ")
cavalo = int(input("<1> Jorge\n<2> Pocoto\n<3> Ricardo\n<4> Faisca\n<5> Miracle\n"))
cavalo-=1 
aposta = float(input("Digite o valor de sua aposta: "))

cavalos = ["Jorge","Pocoto","Ricardo","Faisca","Miracle"]
cavposition = [0,0,0,0,0]
print(cavalos)
win = True
while(win):
    cavposition[0]+= randint(0, 5)
    cavposition[1]+= randint(0, 5)
    cavposition[2]+= randint(0, 5)
    cavposition[3]+= randint(0, 5)
    cavposition[4]+= randint(0, 5)
    print(cavposition)
    for i in range(len(cavposition)):
        if(cavposition[i]>=100):
            win = False         

posicao = cavposition[cavalo]
cavposition = sorted(cavposition)
cavposition = list(reversed(cavposition))
lugar = cavposition.index(posicao)+1

if(lugar==1):
    aposta*=5
elif(lugar==2):
    aposta*=3
elif(lugar==3):
    aposta*=2

print("O seu premio é:",aposta)
print("O seu cavalo {}, ficou em {}º lugar".format(cavalos[cavalo],lugar))
    

