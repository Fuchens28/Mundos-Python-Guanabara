
total_maior_18 = 0
total_homens = 0 
total_mulheres_menor_20 = 0

while True:
    print('-=' * 20)
    print('CADASTRO DE PESSOAS')
    print('-=' * 20)

    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade > 18:
        total_maior_18 += 1

    if sexo == 'M':
        total_homens += 1
    elif sexo == 'F' and idade < 20:
        total_mulheres_menor_20 += 1

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'\nRESULTADOS:')
print(f'A) Pessoas com mais de 18 anos: {total_maior_18}')
print(f'B) Homens cadastrados: {total_homens}')
print(f'C) Mulheres com menos de 20 anos: {total_mulheres_menor_20}')


