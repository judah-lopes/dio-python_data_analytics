# # === etapa 1 - if / if-else / elif ===

# # ---- if ----
saldo = 2000.0
saque = float(input('Qual o valor que desejas sacar?'))

if saldo >= saque:
	print('Saque realizado com sucesso.')
	
if saldo < saque:
	print('Não foi possível realizar o saque.')
	
# # ---- if-else ----
saldo = 2000.0
saque = float(input('Qual o valor que desejas sacar?'))

if saldo >= saque:
    saldo -= saque
    print('Saque realizado com sucesso.')
else:
    print('Não foi possível realizar o saque.')

# ---- elif ----
opcao = int(input('Informe uma opção: \n[1] Sacar \n[2] Estrato\n'))

if opcao == 1:
	valor = float(input('Qual a quantia a ser sacada?'))
elif opcao == 2:
	print('Exibindo o extrato...')
else:
	exit('Opção inválida')

# === etapa 2 - if aninhado ===
if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    elif saque <= (saldo + cheque_especial):
        print('Saque realizado com sucesso.') 
elif conta_universitária:
    if saldo >= saque:
        print('Saque realizado com sucesso')
    else:
    	print('Saldo insuficiente')

# === etapa 3 - if ternário ===
status = 'Sucesso' if saldo >= saque else 'Falha'