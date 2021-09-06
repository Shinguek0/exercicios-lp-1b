#Escreve um Programa que leia uma lista com no minino 5 itens, contendo itens repetidos e 
#mostre os itens repetidos. 

from iteration_utils import duplicates

lista1 = ["um","dois","tres","quatro","cinco","seis","sete","oito","dois","tres"]
lista2 = []
x = 0

print(list(duplicates(lista1)))