# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço. com 5% de desconto

preco = float(input('Qual o valor do produto? '))
print(f'O valor do seu produto é de R${preco} e o valor com desconto vai ficar R${preco - preco * 5/100}')