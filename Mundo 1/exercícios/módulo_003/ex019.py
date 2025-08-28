# Um professor quer sortear um dos quatro alunos para apagar o quadro. Faça um programa que ajude ele, escrever o nome escolhido

import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo Aluno: ')) 
a3 = str(input('Terceiro Aluno: '))
a4 = str(input('Quarto Aluno: '))

lista = [a1, a2, a3, a4]
escolhido = random.choice(lista)

print(f'O aluno escolhido foi {escolhido}')
