#8)	Faça um programa que leia algo pelo teclado e mostre na tela seu tipo de dado e todas as informações sobre ele.

inp = input("Digite alguma coisa: ")
print("")
if(inp.isalpha()):
    print(inp + " é uma String!" '\n')

if(inp.isnumeric()):
    print(inp, " é uma int!" '\n')

if(inp.isalnum() and not(inp.isalpha()) and not(inp.isnumeric())):
    print(inp, " tem int e String!")