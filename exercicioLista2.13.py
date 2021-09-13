#Faça um programa que pergunte ao usuário se ele quer passar uma temperatura de Fahrenheit
#para Celsius ou de Celsius para Fahrenheit, e que, a partir da resposta do usuário, faça a devida
#conversão.

print("Escolha qual a conversao que voce deseja fazer: ")
print("   <1> f para Cº         <2> Cº para f")
esc = int(input(""))
if(esc==1):
    temp = float(input("Digite a temperatura: "))
    c = ( temp - 32) * 5/9
    print(temp,"f sao iguais a",c,"Cº")
elif(esc==2):
    temp = float(input("Digite a temperatura: "))
    f =( temp * 9/5) + 32
    print(temp,"Cº sao iguais a",f,"f")
else:
    print("Invalido")