# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. no final do programa, mostre:
# -> Média de idade do grupo
# -> Nome do homem mais velho 
# -> Quantas mulheres tem menos de 20 anos 


somaidade = 0
médiaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0

for p in range(1, 5):
    print(F'----- {p}° PESSOA -----')
    nome = str(input('Nome: ')).strip
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    somaidade += idade

    if p == 1 and sexo in 'Mm':
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1


print(f'A média de idade do grupo é de {somaidade / 4}')
print(f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}')
print(f'Ao todo são {totmulher20} mulheres com menos de 20 anos')


