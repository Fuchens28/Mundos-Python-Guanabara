# A python é uma linguagem que tem algumas limitações para deixar algo mais leve por conta disso é preciso importar certas coisas
# Para importar algo usa-se -> import
# Usar nas primeiras linhas o import
# Para frazer importações espicificas, limitadas -> from nome do módulo import o que quer importar 
# exemplo -> Biblioteca math: ceil -> arredonda para cima; floor -> arredonda para baixo; trunc -> tira as casas depois da virgula
# pow -> potência; sqrt -> raiz quadrada; factorial -> fatorial
# import math -> importa todas as funções da biblioteca
# from math import sqrt,... -> importa somente o sqrt

import math # Importa a biblioteca inteira

num = int(input('Digite um número: '))
raiz = math.sqrt(num)
raiz_arredondada = math.floor(raiz)
print(f'A raiz de {num} é igual a {raiz_arredondada}')

from math import sqrt # Importando só o sqrt 

# Para ver as bibliotecas -> olhar a documentação do Python 
# randon -> Gera um número aleatorio
# Para gerar um número interio usa randon.randint 

# Exercícios feitos: 016 ao 021
# Para instalar algum pack usa no terminal: pip install nome do pacote
