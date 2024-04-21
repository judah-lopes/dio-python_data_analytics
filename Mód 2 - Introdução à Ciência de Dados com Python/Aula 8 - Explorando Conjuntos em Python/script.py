# ==etapa 1 - como criar conjuntos ==

# - Criando

# > EXEMPLO
set([1, 2, 3, 1, 3, 4])
# >> {1, 2, 3, 4}

set("abacaxi")
# >> {'a', 'i', 'c', 'b', 'x'}

set(('palio', 'gol', 'palio', 'celta'))
# >> {'palio', 'gol', 'celta'}

#- Acessando - 

# > __EXEMPLO__
numeros = {1, 2, 3, 2}

numeros = list(numeros)

numeros[0]

# - iterar conjuntos (for)
carros = {'gol', 'celta', 'palio'}

for carro in carros:
	print(carro)

# >> gol
# >> celta
# >> palio

# - função enumerate()
carros = {'gol', 'celta', 'palio'}

for indice, carro in enumerate(carros):
	print(f'{indice}: {carro}')

# >> 0: gol
# >> 1: celta
# >> 2: palio

# ==== etapa 2 - métodos da classe set ====

# - método .union() (set1 + set1)
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b)   
# >> {1, 2, 3, 4}    

# - método .intersection() (∩)
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.intersection(conjunto_b)  
# >> {2, 3}

# - método .difference() (set - set)
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.difference(conjunto_b)   # >> {4}
conjunto_b.difference(conjunto_a)   # >> {1}

# - método .symmetric_difference() (set1, set2 - ∩)
conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

conjunto_a.symmetric_difference(conjunto_b)   # >> {1, 4}

# - método .issubset() (é subconjunto?)
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issubset(conjunto_b)   # >> True
conjunto_b.issubset(conjunto_a)   # >> False

# - método .issuperset() (é conjunto pai?)
conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

conjunto_a.issuperset(conjunto_b)   # >> False
conjunto_b.issuperset(conjunto_a)   # >> True

# - método .isdisjoint() (são conjuntos independentes entre si?)
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

conjunto_a.isdisjoint(conjunto_b)    # >> True
conjunto_a.isdisjoint(conjunto_c)    # >> False

# - método .add() (adicionar elemento)
sorteio = {1, 23}

sorteio.add(25)     # >> {1, 23, 25}
sorteio.add(42)     # >> {1, 23, 25, 42}
sorteio.add(25)     # >> {1, 23, 25, 42}

# - método .clear() (limpa o conjunto)
sorteio = {1, 23}

print(sorteio)
# >> {1, 23}

sorteio.clear()

print(sorteio)
# >> {}

# - método .copy() (copia a o conjunto)
sorteio = {1, 23}

sorteio2 = sorteio.copy()

print(sorteio)
print(sorteio2)

# >> {1, 23}
# >> {1, 23}

# - método .discard(x) (apaga o argumento (x))
numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

numeros.discard(1)
numeros.discard(45)  # <-- se o elemento não existe, não da erro
print(numeros)
# >> {2, 3, 4, 5, 6, 7, 8, 9, 10}

# - método .pop()  (tira e retorna o 1º valor)
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.pop()  # >> 0
numeros.pop()  # >> 1
print(numeros) # >> {2, 3, 4, 5, 6, 7, 8, 9}

# - método .remove(x) (tira o elemento (x))
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

numeros.remove(4)  
print(numeros) # >> {1, 2, 3, 5, 6, 7, 8, 9}

numeros.remove(45)  # <-- se não existe, dá erro

# - método len() (tamanho do conjunto)
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

len(numeros)  # >> 10

# - método in (verifica se um valor está em um conjunto)
numeros = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

1 in numeros  # >> True
10 in numeros # >> False