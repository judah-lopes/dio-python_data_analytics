# ==== etapa 1 - estudando a fundo as funções ====

# --------------------------------------------------------------------------------------------------------
# - Retringindo o tipo de declaração dos dados -

# ---- Postional only ----
def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Clio', 2001, 'JGB-4168', marca='Renault', motor='1.0', combustivel='Gasolina')

# criar_carro(modelo='Clio', ano=2001, placa='JGB-4168')  <--- inválido

# ---- Keyword only ----

def criar_carro(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(modelo='Clio', ano=2001, placa='JGB-4168', marca='Renault', motor='1.0', combustivel='Gasolina')

# criar_carro('Clio', 2001, 'JGB-4168')    <----- inválido

# ---- (Keyword + Positional) only ----

def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro('Clio', 2001, 'JGB-4168', marca='Renault', motor='1.0', combustivel='Gasolina')  

# criar_carro(modelo='Clio', ano=2001, placa='JGB-4168', 'Renault', '1.0', 'gasolina')   # <---- inválido

# --------------------------------------------------------------------------------------------------------
# - usando funções como objeto -

# ---- como parametro de outra função ----
def somar(a,b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f'O resultado da operação {a} + {b} = {resultado}')

exibir_resultado(10, 15, somar)

# --------------------------------------------------------------------------------------------------------
# - Usando escopo global dentro de funções -

salario = 2000

def salario_bonus(bonus):
	global salario
	salario += bonus
	return salario

print(salario_bonus(500))