# ===== Interpolação de Variáveis ======

# > EXEMPLO
nome = 'Pedro Judah'
idade = 20
peso = 97.3

pessoa = {"nome":"Pedro Judah", "idade":20, "peso":97.3}
# ----- no método old style (%) -----

# str = %s
# int = %d
# float = %f

print('Olá, meu nome é %s! Tenho %d anos e peso %fkg.' %(nome, idade, peso))

# ----- no método format -----

print('Olá, meu nome é {}! Tenho {} anos e peso {} kg.'.format(nome, idade, peso))

# OU

print('Olá, meu nome é {1}! Tenho {2} anos e peso {0} kg.'.format(peso, nome, idade))

# OU

print('Olá, meu nome é {nome}! Tenho {idade} anos e peso {peso} kg.'.format(nome=nome, idade=idade, peso=peso))

# OU  (Dicionário)

print('Olá, meu nome é {nome}! Tenho {idade} anos e peso {peso} kg.'.format(**pessoa))


# ----- no método f string -----

print(f'Olá, meu nome é {nome}! Tenho {idade} anos e peso {peso} kg.')

# -----

PI = 3.14159

print(f'Valor de PI: {PI:.2f}')
