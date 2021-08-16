import datetime

dia = int(input("Digite o dia do seu nascimento: "))
mes = int(input("Digite o mes do seu nascimento: "))
ano = int(input("Digite o ano do seu nascimento: "))

print("{}/{}/{}".format(dia,mes,ano))
print("Dia: {}\nMes: {}\nAno: {}".format(dia,mes,ano))

x = datetime.datetime(ano, mes, dia)
print(x)