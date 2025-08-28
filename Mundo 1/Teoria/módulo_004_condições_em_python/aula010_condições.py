# if carro.esquerda(): -> funciona como se -> Bloco True 
# else: -> funciona como senão -> bloco False
# Quando for uma estrutrua simples coloca-se "if" quando for uma estrutura composta coloca-se "else"

tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Carro novo')

else:   
    print('Carro velho')

print('--FIM--')


nome = str(input('Qual seu nome? '))

if nome == 'Matheus':
    print('Que nome lindo você tem! ')

print(f"Bom dia {nome}! ")


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

m = (n1 + n2)/2

print(f'A sua média foi {m}')

if m >= 6.0:
    print('Sua média foi boa! Parabéns!')
else:
    print('Sua média não foi boa! Estude mais! ')