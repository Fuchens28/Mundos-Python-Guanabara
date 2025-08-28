# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# nescessaária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m^2

alt = float(input('Qual é a altura em mêtros da parede? '))
larg = float(input('Qual é a largura em mêtros da sua parede? '))
area = (alt * larg)
tinta = (area / 2)
print(f'A área da parede é {area} mêtros quadrados e a quatidade de tinta nescessaria para pintar toda a parede é {tinta} litros de tinta')
