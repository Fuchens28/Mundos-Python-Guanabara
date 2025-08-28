# elif -> colocasse após o if, significa senão
# Pode ter diversos elif, sempre dentro de if


nome = str(input('Qual o seu nome? '))

if nome == 'Matheus':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bempopular no Brasil. ')
elif nome in 'Giovanna':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
    
print(f'Tenha um bom dia, {nome}!')