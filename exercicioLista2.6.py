#Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e,
#em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha
#na tela.

nome = input("Digite seu nome: ")
print("Você gosta do seu nome?")
print("     <Sim> <Nao>")
choice = input("")

if(choice=="Nao" or choice=="nao" or choice=="NAO"):
    print("Voce não gosta do seu nome: " + nome)
else:
    print("Você gosta do seu nome: "+nome)