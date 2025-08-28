# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas já são maiores. 
# 21 anos para ser maior 

from datetime import date 

atual = date.today().year
totmaior = 0
totmenor = 0

for pess in range(1, 8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu?  '))
    
    anos = atual -  nasc
    
    if anos >= 21:
        totmaior += 1
    
    else:
        totmenor += 1

print(f'Ao todo tivemso {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menores de idade')