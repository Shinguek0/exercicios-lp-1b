#Faça um programa que mostre na tela uma pergunta de múltipla escolha, e que, a partir da
#resposta do usuário, mostre na tela se ele acertou ou não.

print('O livro "o principe" foi escrito por: ')
print("<A> Socrates\n<B> Jhon Lock\n<C> Nicolau Maquiavel\n<D> Carl Marx\n<E> Shakespeare\n")
r = input("resposta: ")

if (r == "c" or r=="C"):
    print("A resposta está certa!!")
else:
    print("A reposta está errada!")