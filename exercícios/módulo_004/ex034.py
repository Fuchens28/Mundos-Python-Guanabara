# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%
# Para os inferiores ou iguais, o aumento é de 15%


salario = float(input('Qual o seu salário atual em reais? '))

s10 = salario + salario * 10/100
s15 = salario + salario * 15/100

if salario > 1250:
    print(f'Seu novo salário vair ser {s10}')

else:
    print(f'Seu novo salário vair ser {s15}')