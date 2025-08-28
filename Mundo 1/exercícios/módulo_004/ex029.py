# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$7,00 POR CADA kM acima do limite 

velocidade = float(input('Velocidade que passou no radar em km/h: '))
limite = 80

if velocidade >= 80:
    multa = (velocidade - limite) * 7
    print(f'Você foi multado no valor de R${multa}')

else:
    print("Você está em uma velocidade permitida")

