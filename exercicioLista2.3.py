#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
#F - Feminino,
#M - Masculino,
#Sexo Inválido.
print("Digite o seu sexo")
print("<F> Feminino <M> Masculino")
sexo = input("")

if(sexo=="F" or sexo=="f"):
    print("O sexo é feminino")
elif(sexo=="M" or sexo=="m"):
    print("O sexo é masculino")
else:
    print("Sexo invalido")