# Cadeia de texto: é nada maais que uma frase
# sempre está em '' ou ""
# uma frase sempre vai ser str

# frase = 'Curso em Vídeo Python
# OPERAÇÕES 

# Fatiamento: 
# ex: frase[9] -> o python vai pegar o 9° caracterie; 
# ex1: frase[9:13] -> vai pegar do 9 ao 12
# ex2: frase[9:21] -> vai pegar do 9 ao 20; 
# ex3: frase[9:21:2] -> vai pegar de 9 ao 20 pulando 2 em 2
# ex4: frase[:5] -> vai começar no iniciou ao 4; 
# ex5: frase[15:] -> pega do 15 até o final; 
# ex6: frase{9::3} -> vai começar no 9 até o final de 3 em 3

# Análise
# len(frase) -> Vai contar quantos caracteries tem na str
# frase.count('o') -> conta quantas letras o tem na str; frase.count('o',0,13) -> conta quantos o tem entre 0 ao 12
# frase.find('deo') -> vai mostrar onde começa o que foi indicado para achar; frase.find('Android") -> recebe -1 pois não encontrou 
# 'Curso' in frase -> procura se existe a palavra dentro da frase

# Trasformação
# frase.raplace('Python', 'Android') -> Substitui as palavras
# frase.upper() -> A str fica toda em maiusculo 
# frase.lower() -> Deixa a str em mínusculo 
# frase.capitalize() -> Joga a frase inteira para mínusculo e só deixa a primeira letra em maiusculo
# frase.title() -> vai trasformar a primeira letra de cada palavra em maiusculo 
# frase.strip() -> Remove todos os espaços inuteis na str 
# frase.rstrip() -> remove só os espaços da direira 
# frase.lstrip() -> Remove só os espaços da esquerda

# Divisão 
# frase.split() -> Divide entre os espaços, quebra a frase e deixa palavras separadas 

# Junção
# '-'.join(frase) -> Vai juntar as palavras da lista e colocar o - entre as palavras

# print("""...""") -> pega o texto todo e mostra de forma separada por linhas 

frase = 'Curso em Vídeo Python'
print(frase[3:13])
print(frase[1:15:2])
print(frase[::2])
print(frase.upper().count('o'))
print(len(frase))
print(frase.strip())
print(frase.replace('Python', 'Android'))
print(frase.find('Curso')) # -> Qual posição se enconta a palavra
print(frase.split())
dividido = frase.split()
print(dividido[0])
print(dividido[2] [3])

