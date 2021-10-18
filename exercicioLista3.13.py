#Crie um programa que leia vários números inteiros pelo teclado. O programa só pode para quando for
#digitado o numero 1000. No final, mostre quantos números foram digitados e qual foi a soma deles.
#Desconsiderando o valor 1000 da parada.

n=[]
rep=0
while rep!=1000:
    rep = int(input("Digite um numero: "))
    if(rep!=1000):n.append(rep)

print("Foram digitados",len(n),"numeros")
print("A soma dos numeros é:",sum(n))