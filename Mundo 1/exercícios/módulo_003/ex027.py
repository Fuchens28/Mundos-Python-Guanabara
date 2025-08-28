# Faça um programa que leia o nome completo de uma pessoa. mostrando em seguida o primeiro e o ultimo nome separadamente
# ex: Ana Maria de Souza -> primeiro= Ana e último= Souza

nome = str(input('Digite o seu nome completo: ')).strip()

lista = nome.split()

print(f'Seu primeiro nome é {lista[0]} e o seu ultimo nome é {lista[-1]}')


