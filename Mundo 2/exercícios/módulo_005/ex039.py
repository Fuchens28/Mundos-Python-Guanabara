# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# -> se ele ainda vai se alistar ao serviço militar
# -> Se é a hora de se alistar 
# -> Se já passou do tempo do alistamento
# Seu programa tambèm deverá mostrar o tempo que falta ou que passou do prazo

idade = int(input('Qual a sua idade? '))

if idade < 18:
    falta = 18 - idade
    print(f'Você ainda não pode se alistar, ainda faltam {falta} anos')

elif idade == 18:
    print('Já esta na idade de se alistar, fique de olho nas datas de alistamento')

elif idade > 18:
    passou = idade - 18
    print(f'Você já passou da idade de se alistar em {passou} anos, procure mais informações')