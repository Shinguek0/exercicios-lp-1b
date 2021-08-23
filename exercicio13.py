#13)ler a largura e a altura de uma parede em metros, e calcule a sua área e a quantidade da tinta necessária para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m².
#2m²
largura = int(input("Digite a largura da parede(em metros quadrados): "))
altura = int(input("Digite a altura da parede(em metros quadrados): "))

areaParede = largura*altura
tinta = areaParede/2

print("Altura {}2m², Largura {}2m², Area da parede {}2m²".format(altura,largura,areaParede))
print("A quantidade de tinta necessária para pintar tuda a parede é: ", tinta)
