# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cit = input('Qual cidade você mora? ').strip()  
cit = cit.upper()                               

primeiro_nome = cit.split()[0]                 

print('SANTO' in primeiro_nome)   


