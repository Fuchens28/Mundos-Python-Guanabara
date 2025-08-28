# A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria
# de acordo com a sua idade:
# -> ate 9 anos: Mirim
# -> até 14 anos: Infantil
# -> até 19 anos: Junior`
# -> até 20 anos: Sênior
# -> acima: Master`


from datetime import date

atual = date.today().year
nasc = int(input('Digite o seu ano de nascimento: '))
idade = atual - nasc

print(f'Você nasceu em {nasc}, e tem {idade} anos.')

if idade <= 9:
    print('A sua categoria é MIRIM')

elif 10 <= idade <= 14:
    print('A sua categoria é INFANTIL')

elif 15 <= idade <= 19:
    print('A sua categoria é JUNIOR')

elif idade == 20:
    print('A sua categoria é SÊNIOR')

else:
    print('A sua categoria é MASTER')
