# ==== etapa 1 - estudando a fundo as funções ====

def exibir_mensagem():
	print('Olá, mundo!')

def exibir_mensagem_2(nome):
	print(f'Seja bem vindo, {nome}!')

def exibir_mensagem_3(nome='anônimo'):
	print(f'Seja bem vindo, {nome}!')

exibir_mensagem()     
exibir_mensagem_2("Pedro")
exibir_mensagem_3()

# - Funções que retornam valor ---------

def calcular_total(numeros):
	return sum(numeros)

def retorna_antecessor_e_sucessor(numero):
	antecessor = numero - 1
	sucessor = numero + 1

	return antecessor, sucessor

print(calcular_total([10, 20, 14]))
print(retorna_antecessor_e_sucessor(10))

# - Funções com argumento nomeado -------

# Apenas o valor:
def salvar_carro(marca, modelo, ano, placa):
    print(f'Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')
	
salvar_carro('Renault', 'Clio', '2001', 'JGB-4168')
salvar_carro(marca='Renault', modelo='Clio', ano='2001',placa='JGB-4168')
salvar_carro(**{'marca': 'Renault', 'modelo': 'Clio', 'ano': '2001', 'placa': 'JGB-4168'})  

# - *args e **kwargs --------------------

def exibir_poema(data_extenso, *args, **kwargs):
	texto = '\n'.join(args)
	meta_dados = '\n'.join([f'{chave.title()}: {valor}' for chave, valor in kwargs.items()])
	mensagem = f'{data_extenso}\n\n{texto}\n\n{meta_dados}'
	print(mensagem)
	
exibir_poema('Domingo, 10 de Agosto de 2003', 'Uma vez Flamengo', 'sempre Flamengo.','Flamengo sempre eu hei de ser.', autor='Pedro Judah', ano=2024)