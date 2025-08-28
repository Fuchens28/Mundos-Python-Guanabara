# Crie um programa que leia uma frase qualquer e diga se ela é um políndromo, desconsiderando os espaços 
# Frase que da para ler de trás para sempre e fica a mesma frase


frase = str(input('Digite uma frase para ver se ela é um palíndromo: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('Temos um palíndromo! ')

else:
    print('A frase digitada não é um palíndromo. ')


