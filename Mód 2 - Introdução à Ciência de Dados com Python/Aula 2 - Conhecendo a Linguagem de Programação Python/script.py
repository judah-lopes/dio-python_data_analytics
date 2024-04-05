# -------- Tópico 5 - Funções de entrada e saída --------

#! ===== etapa 1 - Lendo valores com a função input =====
#   
nome = input('Informe seu nome: ') 
sobrenome = input('Informe seu sobrenome: ') 
#
#! ===== etapa 2 - Exibindo valores com a função print =====
#   Todos os objetos são convertidos para string
#   1 argumento obrigatório e
#   4 opcionais:
#   - sep (separa os objetos)
#   - end (termina os objetos)
#   - file
#   - flush
#
print(nome, sobrenome)
print(nome, sobrenome, end="...\n") # \n = quebra de linha
print(nome, sobrenome, sep=' #')