# ====== criação e metodo list ======

# ------------ CRIAÇÃO ------------

# ---- com colchete ----
frutas = []   # <--- vazia

frutas = ["laranja", "maca", "uva"]

# ---- com método list ----
letras = list('python')

# ---- com list + range ----
numeros = list(range(10))

# ---- Em uma lista, podemos aceitar dados de vários tipos ----

carros = ['ferrari', 'f8', 420000, 2020, 2900, 'Brasília', True]

# ------------ ACESSO ------------

# ---- acesso direto usando índices ([i]) ----
frutas = ['maçã','laranja', 'uva', 'pera']

# - índices positivos -
print(frutas[0])    # >> maçã
print(frutas[2])    # >> uva

# - índices negativos -
print(frutas[-1])   # >> pera
print(frutas[-3])   # >> laranja

# ---- acesso a listas aninhadas ([[], [], []]) ----
matriz = [[1, 'a', 2],
		  ['b', 3, 4],
		  [6, 5, 'c']]

matriz[0]      # >> [1, 'a', 2]
matriz[0][0]   # >> 1
matriz[0][-1]  # >> 2
matriz[-1][-1] # >> 'c'

# ---- fatiamento (...:...:...) ----
lista = ['p', 'y', 't', 'h', 'o', 'n']

lista[2:]     # >> ['t', 'h', 'o', 'n']
lista[:2]     # >> ['p', 'y']
lista[1:3]    # >> ['y', 't']
lista[0:3:2]  # >> ['p', 't']
lista[::]     # >> ['p', 'y', 't', 'h', 'o', 'n']
lista[::-1]   # >> ['n', 'o', 'h', 't', 'y', 'p']

# ---- iterar listas (for) ----
carros = ['gol', 'celta', 'palio']

for carro in carros:
	print(carro)


# ---- função enumerate() ----
carros = ['gol', 'celta', 'palio']

for indice, carro in enumerate(carros):
	print(f'{indice}: {carro}')

# ---- Compreensão de lista ----
# A compreensão de lista oferece uma sintaxe mais curta quando você deseja: <ins>criar uma nova lista com base nos valores de uma já existente (__filtro__)</ins> ou <ins>gerar uma nova lista explicando alguma modificação nos elementos de uma lista existente</ins>.

# - filtro - 

# _Versão 1_
numeros = [1, 20, 30, 28, 2, 9, 23]
pares = []

for numero in numeros:
	if numero % 2 == 0:
		pares.append(numero)

# _Versão 2 (comprehension)_
numeros = [1, 20, 30, 28, 2, 9, 23]
pares = [numero for numero in numeros if numero % 2 == 0]

# - modificando valores -

# _Versão 1_
numeros = [1, 20, 30, 28, 2, 9, 23]
quadrado = []

for numero in numeros:
	quadrado.append(numero ** 2)

# _Versão 2_
numeros = [1, 20, 30, 28, 2, 9, 23]
quadrado = [numero ** 2 for numero in numeros]
