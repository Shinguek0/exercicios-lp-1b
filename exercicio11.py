#11)Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("Digite o preço do produto: "))

print("O preço R${}, com 5% de desconto fica: R${:.2f}".format(preco,preco+(preco/100)*5))