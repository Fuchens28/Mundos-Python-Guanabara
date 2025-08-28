# Crie um programa que leia duas notas de um aluno e calcue sua média, mostrando uma mensagem no final, de acordo com a mèdia
# atingida 
# -> Média abaixo de 5.0: REPROVADO
# -> Média entre 5.0 e 6.9: RECUPERAÇÃO
# -> Média 7.0 ou superior: APROVADO 


n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print(f'Sua média foi {media:.1f}')

if media < 5.0:
    print('Você está REPROVADO')

elif 5.0 <= media <= 6.9:
    print('Você está de RECUPERAÇÃO')

else:
    print('Você foi APROVADO')
