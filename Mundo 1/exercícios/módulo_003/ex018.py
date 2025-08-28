# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo

import math 

ang = float(input('Digite o ângulo: '))

sen = math.sin(ang)
cos = math.cos(ang)
tag = math.tan(ang)

print(f'Seu ângulo é {ang}, o seno {sen}, o cosseno {cos} e sua hipotenusa {tag}')