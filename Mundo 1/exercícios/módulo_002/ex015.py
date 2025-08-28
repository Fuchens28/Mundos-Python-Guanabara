# Escreva um programa que pergunta a quantidade de Km percorridos por um carro aluado e a quantidade de dias pelos quais foi
#alugado e calcule o preço a pagar, Sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado

d = int(input('Insira quantos dias o carro foi alugado: '))
km = float(input('Insira quantos Kms foram rodados nesses dias: '))

p1 = (d * 60) + (km * 0.15)

print(f'O valor a pagar pelo aluguel é de R${p1:.2f}')

