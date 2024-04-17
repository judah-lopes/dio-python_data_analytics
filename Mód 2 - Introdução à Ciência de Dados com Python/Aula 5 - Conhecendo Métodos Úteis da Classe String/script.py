

# == etapa 1 - conhecendo métodos úteis da classe string ==

# > métodos para mudar o case dos caracteres

curso = "pYthON"

# ----- método para maiúsculas (uppercase)

print(curso.upper())

# ----- método para minúsculas (lowercase)

print(curso.lower())

# ----- método para título (title)

print(curso.title())

# > métodos para eliminar espaços

curso = "     Python  "

# ----- método para eliminar todos os espaços (antes e depois)

print(curso.strip())

# ----- método para eliminar os espaços antes (left)

print(curso.lstrip())

# ----- método para eliminar os espaços depois

print(curso.rstrip())

# > junções e centralização

curso = "Python"

# ----- método para centralizar ----

# recebe 2 valores: nº total de caracteres + algum caractere para completar o nº total
print(curso.center(10, "!")) 

# ---- método para juntar ------

# recebe: o que será juntado + ONDE será juntado como ARGUMENTO
print(".".join(curso))