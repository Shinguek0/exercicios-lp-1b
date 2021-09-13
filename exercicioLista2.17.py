#Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou nao se
#aposentar. As condições para aposentadoria são:
#• Ter pelo menos 65 anos,
#• Ou ter trabalhado pelo menos 30 anos,
#• Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input("Digite sua idade: "))
tempoTrabalho = int(input("Digite o tempor que voce trabalhou em meses: "))

if(idade>=65 or tempoTrabalho>=30*12):
    print("Pode aposentar")
elif(idade>=60 and tempoTrabalho>=25):
    print("Pode aposentar")
else:
    print("Nao pode aposentar!")