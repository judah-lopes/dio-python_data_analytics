# ====== etapa 1 - fatiamento de strings ======

# > EXEMPLO

nome = 'Pedro Judah Gomes Nogueira Lopes'

# ----- para um caractere específico -----

print(nome[0])

# ----- para um grupo de caracteres *a partir da posição inicial* (:...) -----

print(nome[:5])      # <- do início : até posição 5 - 1 

# ----- para um todos os caracteres *a partir de um início* (...:) -----

print(nome[6:])      # <- da posição 6 : pra frente

# ----- para um grupo de caracteres especificado (...:...)  -----

print(nome[6:11])   # <- da posição 6 : até a posição 11 - 1

# ----- para um grupo de caracteres especificado e com um step (...:...:...) -----

print(nome[6:11:2]) # <- da posição 6 : até a 11 - 1 : pulando de 2 em 2 caracteres

# ----- para a string sem nenhum parâmetro (:) -----

print(nome[:])

# ----- para a string invertida -----

print(nome[::-1])
