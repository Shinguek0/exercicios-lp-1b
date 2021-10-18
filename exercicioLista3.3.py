#Faça um programa que calcule a soma entre todos os número impares que são múltiplos de três e que se
#encontram no intervalo de 1 até 500.

x = 0
#nunbers = 500
#for i in range(nunbers):
#    if((i%2)and(i>0)and(i%3==0)):
#        x+=i
#print(x)

for i in range(1,500,2):
    if(i%3==0):
        x+=i
print(x)