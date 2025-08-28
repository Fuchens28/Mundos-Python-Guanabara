# Refaça o Desafio 035 dos triângulos acrescentando o recurso de mostrar que tipo de trângulo será formado:
# -> Equilátero: todos os lados iguais 
# -> Isósceles: Doisa lados iguais 
# -> Escaleno: Todos os lados diferentes


r1 = int(input('Digite o tamanho da primeira reta: '))
r2 = int(input('Digite o tamanho da segunda reta: '))
r3 = int(input('Digite o tamanho da terceira reta: '))

if (r1 + r2 > r3) and (r1 + r3 > r2) and (r2 + r3 > r1):
    print('Suas retas formam um triângulo!')

    if r1 == r2 == r3:
        print('Esse triângulo é EQUILÁTERO (todos os lados iguais).')

    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('Esse triângulo é ISÓSCELES (dois lados iguais).')

    else:
        print('Esse triângulo é ESCALENO (todos os lados diferentes).')

else:
    print('Suas retas NÃO formam um triângulo.')
