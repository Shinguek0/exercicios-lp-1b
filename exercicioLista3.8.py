#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda
#não atingiram a maioridade e quantas já são maiores de idade.

idade = []
upage=0
underage=0
for i in range(7):
    idade.append(int(input("Digite o ano de seu nascimento exemplo(1990): ")))

for i in idade:
    if(2021-i>=18):
        #print("Voce é maior de idade!!")
        upage+=1
    else:
        #print("Your under age!!")
        underage+=1
print(upage,"pessoas são maiores de idade, e",underage,"são menores de idade")