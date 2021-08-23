#lista 1.1 ler int e print
fin = True

while(fin):
    n = input("Digite um numero inteiro: ")
    if(n.isalpha() and n.isalnum()):
        print("digite apenas numeros inteiros!!")
    else:
        print(int(n))
        fin = False