# Refaça o Desafio 009, mostrando a tabuada de um númeor que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Digite um nùmero para ver a tabuada: '))

for c in range(0, 11):
    print(f'''Sua tabuada é: {n} x {c :2} = {n * c}''')