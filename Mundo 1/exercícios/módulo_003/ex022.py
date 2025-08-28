# Crie um programa que leia o nome completo de um pessoa e mostre: 
# -> O nome com todas as letras maiúsculas
# -> O nome com todas minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

nome = str(input('Digite o seu nome completo: ')).strip()

print('Analisando o seu nome...')

print(f'Seu nome em maúsculo é {nome.upper()}')
print(f'Seu nome em minúsculo é {nome.lower()}')
print(f'Seu nome tem {len(nome)} letras')
print(f'Seu primeiro nome tem {format(nome.find(' '))}')