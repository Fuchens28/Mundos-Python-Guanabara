# Faça um algoritomo que leia o salário de um funcionaário e mostre seu novo salário, com 15% de aumento

salario = float(input('Qual o seu salário atual? '))
aumento = (salario + salario* (15/100))
print(f'Seu salário é de {salario} e com o aumento vai ficar {aumento}')