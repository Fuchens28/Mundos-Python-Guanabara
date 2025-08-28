# Estrutura de repetição que usa uma condição 
# Estrutura de repetição com teste logico 

# while not algo:
#   passo
# pega

for c in range(1,10):
    print(c)

print('ACABOU')


c = 1

while c < 10:
    print(c)
    c = c + 1

print('ACABOU')

n = 1 
r = 'S' 

while n != 0:
    n = int(input('Digite um valor: '))  # essa função serve para quando não se sabe o limite
    r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM')


    