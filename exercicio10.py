#10)Faça um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
#US$ 1.00 = R$ 5.41
reais = float(input("Digite quantos reais você tem: "))

print("Com R${} voce pode comprar {:.2f} dolares".format(reais,reais/5.41))