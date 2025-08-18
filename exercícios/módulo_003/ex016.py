# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porçãõ inteira
# EX: digite um número: 6.127; o número 6.127 tem parte inteira 6

import math 
num = float(input('Digite um número: '))
num1 = math.floor(num)
print(f'O número {num} tem parte inteira {num1}')