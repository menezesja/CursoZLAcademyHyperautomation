a, b, c = map(int, (input('Informe 3 numeros inteiros, separado por um espaço: ').split()))

if (a + b > c) or (a + c > b) or (b + c > a):
    print('Não é um triangulo')
elif (a == b) and (a ==c ) and (b == c):  #a=b=c
    print('triângulo equilatero')
elif (a == b) and (a != c ) and (b != c): #a=b!=c
    print('triângulo isósceles')
elif (a != b) and (a !=c ) and (b != c):
    print('triângulo escaleno')
else:
    print('não é um triâgulo')    

    