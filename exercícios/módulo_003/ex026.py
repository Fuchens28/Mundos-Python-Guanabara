# Faça um programa que leia uma frase pelo teclado e mostre: 
# -> Quantos vezes aparece a lettra "A"
# -> Em que posição ela aparece a primeira vez
# -> Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()

print(frase.count('A'))
print(frase.find("A") + 1)
print(frase.rfind('A'))