# ==== etapa 1 - criação e acesso aos dados ====

# - Criando -
# ----- pelas chaves diretamente ({... : ...}) ----
pessoa = {"nome": "Pedro", "idade": 20}

# ----- pela classe dict() ----
pessoa = dict(nome="Pedro", idade=20)


# ----> para adicionar uma nova chave em um dict já existente ----
pessoa["telefone"] = "2932-2232"

# >> {"nome": "Pedro", "idade": 20, "telefone": "2932-2232"}

# - Acessando -
# ----- acesso direto usando índices ([i]) ----
dados = {"nome": "Pedro", "idade": 20, "telefone": "2932-2232"}

dados["nome"]       # >> "Pedro"
dados["idade"]      # >> 20
dados["telefone"]   # >> "2932-2232"

# ----- dicionários aninhados ({... : {... : ...}}) ----
contatos = {
    "dev.judahlopes@gmail.com": {"nome": "Pedro", "telefone":"0239-9142"},
    "carlos.cafejs@gmail.com": {"nome": "Carlos", "telefone":"1359-9452"},
    "baruidepombo@gmail.com": {"nome": "Ulisses", "telefone":"6539-9774"},
    "otaviomensde@gmail.com": {"nome": "Otavio", "telefone":"4329-4175"}
}

contatos["otaviomensde@gmail.com"]["telefone"] 
# >> "4329-4175" 

# ----- iterar dicionário (for) ----
for chave in contatos:
	print(chave, contatos[chave])
#-----------------------------------------------------------

                          # .items(), retorna lista de tuplas
for chave, valor in contatos.items():  
	print(chave, valor)   

