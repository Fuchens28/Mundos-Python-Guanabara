# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi
# o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


n = 0
c = 'S'
soma = quant = 0

while c == 'S':
    n = int(input('Digite um número: '))

    soma += n
    quant += 1
    
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    c = str(input('Você quer continuar? [S/N] ')).upper().strip()

media = soma / quant

print(f'Você digitou {quant} números e a média deles é {media:.2f}')
print(f'O maior número digitado foi {maior} e o menor foi {menor}')
