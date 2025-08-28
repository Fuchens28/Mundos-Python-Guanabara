# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado. peça a digitação novamente
# até ter um valor correto.

f = ''

while f not in ['M', 'F']:
    f = str(input('Qual o seu sexo? [M/F] ')).upper().strip()

