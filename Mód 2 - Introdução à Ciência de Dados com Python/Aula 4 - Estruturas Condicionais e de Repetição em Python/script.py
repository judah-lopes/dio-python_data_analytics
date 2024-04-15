def sacar(valor):
    saldo = 300
    
    if valor <= saldo:
        saldo -= valor
        print(f'Saque sucedido. Seu saldo agora é R${float(saldo)}')
        

sacar(200)

def depositar(valor):
    saldo = 1000

    if valor > 0:
        saldo += valor
        print(f'Parabéns! Depósito efetuado com sucesso! Seu saldo agora é R${float(saldo)}')

depositar(200)