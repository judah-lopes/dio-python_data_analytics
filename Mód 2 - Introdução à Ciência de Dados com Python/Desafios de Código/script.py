# Desafio 1 - A Aventura do Explorador
#------------------------------------------------------------------------------
# --> Entrada
# Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, 
# representando a quantidade de passos que o explorador deve dar na floresta. .

# --> Saída
# O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. 
# Utilize um laço de repetição para simular os passos do explorador. 
# A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

quantidade_passos = int(3)

if quantidade_passos == 0:
  print("Nenhum passo dado na floresta.")
else:
  for passo in range(1, quantidade_passos + 1):
    if passo == 1:
      print(f"Explorador: {passo} passo")
    else:
      print(f"Explorador: {passo} passos")

# =============================================================================

# Desafio 2 - Lista para itens de RPG
#------------------------------------------------------------------------------
# Crie um programa que permita cadastrar uma lista de itens que o personagem possui. 
# A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

# --> Entrada
# O programa deve solicitar ao usuário o nome dos 3 itens que o personagem possui. 
# Cada item deve ser cadastrado separadamente.

# --> Saída
# Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela 
# a lista de itens que o personagem possui. A saída deve ter o seguinte formato:

# Lista de itens:
# - [item1]
# - [item2]
# - [item3]

itens = []

for item in range(3):
  novo_item = input()
  itens.append(novo_item)

print("Lista de itens:")
for item in itens:
    print(f"- {item}")

# =============================================================================

# Desafio 3 - Nova capacidade de mithril
#------------------------------------------------------------------------------

# --> Entrada
# Dois valores inteiros positivos, representando a capacidade atual 
# total em teraflops e o aumento percentual, separados por espaço.

# --> Saída
# A nova capacidade total em teraflops.

capacidade_atual, aumento_percentual = map(int, input().split())

capacidade_atual += int(capacidade_atual / 100 * aumento_percentual)

print(capacidade_atual)