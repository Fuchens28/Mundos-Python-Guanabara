# ITERAÇÃO
# LAÇOS DE REPETIÇÃO
# Faz uma petetição de certa coisa 
# for c in range(1,10): -> O c pode ser qualquer variavel
#   passo 
#pega


for c in range(0,6):  # -> ele conta sempre uma vez a menos 
    print('OI')

print('FIM')

for c in range(6, 0, -1):
    print(c)

n = int(input('Digite um nùmero: '))

for c in range(0, n+1):
    print(c)

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c)

print('FIM')


s = 0

for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n

print(f'O somatorio de todos os valores foi {s}')