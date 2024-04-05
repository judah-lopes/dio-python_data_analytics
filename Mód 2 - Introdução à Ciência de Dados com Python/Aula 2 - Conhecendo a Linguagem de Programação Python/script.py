# -------- Tópico 4 - Conversão de Dados --------

#! ===== etapa 1 - Convertendo tipos =====
#   
#!  - inteiro (int) pra float:
#
preco = 10
print(preco)

preco = float(preco)
print(preco)
#   OU usando divisão
preco = preco / 1
print(preco)
#
#__________________________________________
#!  - float pra inteiro
#
valor = 10.50
print(valor)

valor = int(valor)
print(valor)
#   e pra EVITAR que saia um float na divisão, use duas barras
valor = 10 // 2
print(valor)
#
#__________________________________________
#!  - numerico pra string
#
preco_por_pao = 0.80
quantidade_de_paes = 10

print(str(preco_por_pao))
print(str(quantidade_de_paes))

frase = f"preço por pão {preco_por_pao}, quantidade de pães {quantidade_de_paes}"
print(frase)
#
#__________________________________________
#!  - string pra numerico
#
idade = '14'
peso = '70.30'

print(int(idade))
print(float(peso))