# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais algum termo. O programa encerra quando ele disser que quer
# mostrar o termo 0 

print('Gerador de PA')
print('-=' * 10)

n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da sua PA: '))

termo = n1
cont = 1
total = 0
mais = 10 

while mais !=0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end = '')
        termo += r
        cont += 1

    print('PAUSA')
    
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('FIM')