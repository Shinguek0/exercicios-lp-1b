#Faça um programa que pergunte a temperatura atual para o usuário e mostre uma mensagem na
#ela dizendo se está “quente”, “frio” ou “agradável”.

temp = float(input("Digite a temperatura: "))

if(temp<10):
    print("Está frio!")
elif(temp<26):
    print("Está agradavel!")
else:
    print("Está quente!")