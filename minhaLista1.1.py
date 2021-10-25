#Faça um programa que use uma estrutura de repetiçao para printar a sequência de Fibonacci
#Fibonacci é, na matemática, uma sequência em que cada número seguinte corresponde à soma dos dois anteriores.
#ex: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584...

a = 0
b = 1
c = 1
print(a)
while True:
    a = a
    b = c
    c = a+b
    a=b
    print(b)
    if(a>2000):
        break