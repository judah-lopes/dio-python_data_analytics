# ==== etapa 2 - métodos da classe list ====

# ---- método .append (adicionar) ----
lista = []

lista.append(1)
lista.append('python')
lista.append([10, 20, 30])

# >> [1, 'python', [10, 20, 30]]

# ---- método .clear (limpar a lista) ----
lista = [1, 'python', [10, 20, 30]]

lista.clear()

# >> []

# ---- método .copy (copiar) ----
lista = [1, 'python', [10, 20, 30]]

lista2 = lista.copy()

print(lista)
print(lista2.append('esta é a cópia'))

# >> [1, 'python', [10, 20, 30]]
# >> [1, 'python', [10, 20, 30],'esta é a cópia']

# ---- método .count (conta quantas vezes um elemento aparece na lista) ----
cores = ['verde', 'amarelo', 'verde', 'azul', 'amarelo', 'verde']

cores.count('verde')   # >> 3
cores.count('amarelo') # >> 2
cores.count('azul')    # >> 1

# ---- método .extend (junta duas listas) ----
linguagens = ['js', 'c', 'python']

linguagens.extend(['java', 'swift'])

# >> ['js', 'c', 'python', 'java', 'swift']

# ---- método .index (primeiro índice de um elemento) ----
linguagens = ['js', 'c', 'java', 'python', 'java', 'swift']

linguagens.index('js')   # 0
linguagens.index('java')   # 2

# ---- método .pop (exclui o <ins>último</ins> elemento, ou pelo <ins>índice</ins>) ----
linguagens = ['js', 'c', 'java', 'python', 'java', 'swift']

linguagens.pop()   # >> 'swift'
linguagens.pop()   # >> 'java'
linguagens. pop(0) # >> 'js'

# ---- método .remove (remove pelo <ins>nome</ins> do elemento) ----
linguagens = ['js', 'c', 'java', 'python', 'java', 'swift']

linguagens.remove('java')

# >> ['js', 'c', 'python', 'java', 'swift']

# ---- método .reverse (inverte a ordem dos elementos) ----
linguagens = ['js', 'c', 'python', 'java', 'swift']

linguagens.reverse()

# >> ['swift', 'java', 'python', 'c', 'js']

# ---- método .sort (ordena a lista, mas não retorna nada) ----

# ____EXEMPLO____
linguagens = ['js', 'c', 'python', 'java', 'swift']

print(linguagens)

# - padrão (alfabética) - 
linguagens.sort()
# >> ['c', 'java', 'js', 'python', 'swift']

# - ordem alfabética inversa -
linguagens.sort(reverse=True)
# >> ['swift', 'python', 'js', 'java', 'c']

# - ordem crescente em tamanho -
linguagens.sort(key=lambda x: len(x)) 
# >> ['c', 'js', 'java', 'swift', 'python']

# - ordem decrescente em tamanho -
linguagens.sort(key=lambda x: len(x), reverse=True)
# >> ['python', 'swift', 'java', 'js', 'c']

# ---- método len (tamanho da lista) ----
len(linguagens)
# >> 5

# ---- método sorted (ordena e retorna) ----
sorted(linguagens, key=lambda x: len(x), reverse=True)
# >> ['python', 'swift', 'java', 'js', 'c']
