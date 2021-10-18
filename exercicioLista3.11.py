#Faça um programa que leia o sexo de uma pessoa. Mas só aceite os valores M ou F. Caso esteja errado,
#peça a digitação novamente até ter um valor correto.
sex=""
x=0
fin = False

while(fin==False):
    if(x>0):
        print("Tente novamente (O programa so aceita os valores \"M\" ou \"F\")")
    sex = input("Digite o seu sexo [M/F]: ").upper()
    if(sex=="M"):
        print("numero de tentativas:",x)
        print("Você é Homem")
        fin = True
    elif(sex=="F"):
        print("numero de tentativas:",x)
        print("Você é mulher")
        fin = True
    x+=1
