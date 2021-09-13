#. Faca um algoritmo que calcule a media das notas de 3 provas. A primeira e a segunda prova tem
#peso 5 e a terceira tem peso 10. Ao final, mostrar a média do aluno e indicar se o aluno foi
#aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 6.0 pontos.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
med = (n1+n2+n3)/2
if (n1 > 5 or n2 >5 or n3 >10):
    print("Voce Digitou as notas errado")
else:
    if(med>=6 and med<=10):
        print("Aprovado!!")
    elif(med >0 and med<6):
        print("reprovado!")
    else:
        print("A media nao pode ser maior que 10, nem menor qe zero")