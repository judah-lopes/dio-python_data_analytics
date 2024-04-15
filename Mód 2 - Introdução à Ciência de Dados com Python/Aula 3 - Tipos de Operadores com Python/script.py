saldo = 1000
saque = 200
limite = 100

# operador "e" (and) - para ser True TUDO tem que ser true
saldo >= saque and saque <= limite    

# operador "ou" (or) - para ser True, apenas um precisa ser True
saldo >= saque or saque <= limite

# operador de negação, inverso (not)
not 1000 > 1500

# parênteses 
conta_especial = true
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
