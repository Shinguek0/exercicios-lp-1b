#Fac¸a um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso
#ideal, utilizando as seguintes formulas (onde h corresponde à altura):
#• Homens: (72.7 ∗ h) − 58
#• Mulheres: (62, 1 ∗ h) − 44, 7

alt = float(input("Digite a sua altura: "))
print("Digite o seu sexo: ")
print("<1>Homem <2>Mulher")
sex = int(input(""))

if (sex==1):
    print("Seu peso ideal é:",(72.7 * alt) - 58)
elif(sex==2):
    print("Seu peso ideal é:",(62, 1 * alt) - 44.7)
else:
    print("Sexo invalido")

