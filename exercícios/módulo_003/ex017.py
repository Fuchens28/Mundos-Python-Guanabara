# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retãngulo, calcule e mostre
# o comprimento da hipotenusa.

import math 

cat_o = int(input('Digite seu cateto oposto: '))
cat_a = int(input('Digite seu cateto adjacente:'))

hip = math.hypot(cat_o, cat_a)

print(f'O seu cateto oposto é {cat_o}, o cateto adjacente {cat_a} e a sua hipotenusa é {hip}')