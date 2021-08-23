#12)Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("Digite o salario do funcionario: "))

print("O salario atual é: R${}, com 15% de aumento fica: R${:.2f}".format(salario,salario+(salario/100)*15))