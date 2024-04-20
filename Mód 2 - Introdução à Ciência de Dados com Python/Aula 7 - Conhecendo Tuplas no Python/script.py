# ==== etapa 1 - criação e acesso aos dados ====

# - Criação -

# ---- pela classe tuple (([])) ----
letras = tuple("python")
# ('p', 'y', 't', 'h', 'o', 'n')

numeros = tuple([1, 2, 3, 4])
# (1, 2, 3, 4)

# ---- usando parênteses, separando os elementos por vírgulas ((..., ..., ...,)) ----
frutas = ("laranja", "maçã", "uva",)

numeros = (1, 2, 3, 4,)

pais = ("Brasil",)

# - Acesso -

# ---- acesso direto usando índices ([i]) ----
frutas = ('maçã','laranja', 'uva', 'pera',)

# ---- índices positivos ----
frutas[0]    # >> maçã
frutas[2]    # >> uva

# ---- índices negativos ----
frutas[-1]   # >> pera
frutas[-3]   # >> laranja

# - acesso a listas aninhadas (((), (), ()))
matriz = (
	    (1, 'a', 2),
		('b', 3, 4),
		(6, 5, 'c')
)

matriz[0]      # >> (1, 'a', 2)
matriz[0][0]   # >> 1
matriz[0][-1]  # >> 2
matriz[-1][-1] # >> 'c'

# - fatiamento (... : ... : ...)
lista = ('p', 'y', 't', 'h', 'o', 'n')

lista[2:]    # >> ('t', 'h', 'o', 'n')
lista[:2]    # >> ('p', 'y')
lista[1:3]   # >> ('y', 't')
lista[0:3:2] # >> ('p', 't')
lista[::]    # >> ('p', 'y', 't', 'h', 'o', 'n')
lista[::-1]  # >> ('n', 'o', 'h', 't', 'y', 'p')

# - iterar listas (for)
carros = ('gol', 'celta', 'palio')

for carro in carros:
	print(carro)

# >> gol
# >> celta
# >> palio

# - função enumerate()
carros = ('gol', 'celta', 'palio')

for indice, carro in enumerate(carros):
	print(f'{indice}: {carro}')

# >> 0: gol
# >> 1: celta
# >> 2: palio

# ==== etapa 2 - métodos da classe tuple ====

# ---- método .count (conta quantas vezes um elemento aparece na lista) ----
cores = ('verde', 'amarelo', 'verde', 'azul', 'amarelo', 'verde')

cores.count('verde')   # >> 3
cores.count('amarelo') # >> 2
cores.count('azul')    # >> 1

# ---- método .index (primeiro índice de um elemento) ----
linguagens = ('js', 'c', 'java', 'python', 'java', 'swift')

linguagens.index('js')   # 0
linguagens.index('java')   # 2

# ---- método len (tamanho da lista) ----
len(linguagens)
# >> 5