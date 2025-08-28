# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule se IMC e mostre seu status, de acordo com a tabela:
# -> Abaixo de 18.5: Abaixo do Peso
# -> Entre 18.5 e 25: Peso ideal
# -> 25 até 30: Sobrepeso
# -> 30 até 40: Obesidade
# -> Acima de 40 Obesidade mórbida


peso = float(input('Qual o seu peso em kg? '))
altura = float(input('Qual a sua altura em mêtros? '))

imc = peso / (altura ** 2)


if imc < 18.5:
    print(f'Seu IMC é {imc: .2f} e você está ABAIXO DO PESO')

elif 18.5 <= imc <= 25:
    print(f'Seu IMC é {imc: .2f} e você está no PESO IDEAL')

elif 26 <= imc <= 30:
    print(f'O seu IMC é {imc: .2f} e você está com SOBREPESO')

elif 31 <= imc <= 40:
    print(f'O seu IMC é {imc: .2f} e você está com OBESIDADE')

else:
    print(f'O seu IMC é {imc: .2f} e você está com OBESIDADE MÓRBIDA')