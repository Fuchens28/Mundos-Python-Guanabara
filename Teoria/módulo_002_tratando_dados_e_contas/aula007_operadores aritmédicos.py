# OPERADORES ARITMÉTICOS
# Adição -> +
# Subtração -> -
# Multiplicação -> *
# Divisão -> /
# Potência -> **
# Divisão Interira -> //
# Resto da divisão -> %
# == -> Uma coisa é igual a outra
# Ordem de precedência -> 1: (); 2: **; 3:*, /, //, %; 4: +, -
# Para separar as linhas -> \n

print(5+3*2)
print(3*5+4**2)
print(3*(5+4)**2)

n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
print(f'A soma vale {n1+n2}')
print(f'A subtração vale: {n1-n2}')
print(f'A multiplicação valeu: {n1*n2}')
print(f'A divisão valeu: {n1/n2}')
print(f'A potência vale: {n1**n2}')
print(f'A Divisão inteira vale: {n1//n2}')
print(f'O resto da divisão vale: {n1%n2}')

# Exercícios do 003 ao 015