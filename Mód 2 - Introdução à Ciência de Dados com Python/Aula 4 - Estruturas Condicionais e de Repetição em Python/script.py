# ----- for -----

texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
print()

# ----- range() -----
list(range(4))

# ----- range com for -----
for numero in range(11):
	print(numero, end=" ")
    
print()

for numero in range(0, 51, 5):
	print(numero, end=" ")
      
# ----- while -----
print()

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair\n'))

    if opcao == 1:
          print('sacando...')
    elif opcao == 2:
          print('exibindo extrato...')

# ----- while/else -----
print()

opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Extrato \n[0] Sair\n'))

    if opcao == 1:
          print('sacando...')
    elif opcao == 2:
          print('exibindo extrato...')
else:
	print('Obrigado, até logo!')
      
    
