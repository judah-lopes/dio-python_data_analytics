# ==== etapa 2 - métodos da classe dict ====

#  > EXEMPLO
contatos = { 
	"dev.judahlopes@gmail.com": {"nome": "Pedro", "telefone":"0239-9142"}
}

# ---- método .clear() (esvazia o dict) ----
contatos.clear()

print(contatos)   
# >> {}

# ---- método .copy() ----
contatos2 = contatos.copy()

contatos["dev.judahlopes@gmail.com"]
# >> {"nome": "Pedro", "telefone":"0239-9142"}

contatos2["dev.judahlopes@gmail.com"]
# >> {"nome": "Pedro", "telefone":"0239-9142"}

# ---- método .fromkeys() (cria chaves) ----
# -> criando chaves sem atribuir o valor ----------------
 
dict.fromkeys(["nome", "telefone"])
# >> {"nome": None, "telefone": None}

# -> criando chaves atribuindo valor padrão -------------

dict.fromkeys(["nome", "telefone"], "vazio")
# >> {"nome": "vazio", "telefone": "vazio"}

# ---- método .get() ----
contatos["chave"] # <-- se n existe, dá KeyError

contatos.get("chave")  # <-- se n existe, retorna None apenas
contatos.get("chave", {})  # >> {}

contatos.get("dev.judahlopes@gmail.com", {})
# >> {"dev.judahlopes@gmail.com": {"nome": "Pedro", "telefone":"0239-9142"}}

# ---- método .items() (retorna uma lista de tuplas) ----
contatos.items()
# >> dictitems([('dev.judahlopes@gmail.com': {'nome': 'Pedro', 'telefone': '0239-9142'})])

# ---- método .keys() (retorna só as chaves) ----
contatos.keys()
# >> dictkeys(['dev.judahlopes@gmail.com])

# ---- método .values() (retorna só os valores das chaves) ----
contatos.values()
# >> dictvalues([{'nome': 'Pedro', 'telefone': '0239-9142'}])

# ---- método .pop(**x**) (remove e retorna a os valores da key x) ----
contatos.pop("dev.judahlopes@gmail.com")
# >> {'nome': 'Pedro', 'telefone': '0239-9142'}

contatos.pop("dev.judahlopes@gmail.com", {})  # >> {}

# ---- método .popitem() (retira a ultima chave e seu valor) ----
contatos["otaviomensde@gmail.com"] = {"nome": "Otavio", "telefone":"4329-4175"}

contatos.popitem()
# >> ('otaviomensde@gmail.com': {'nome': 'Otavio', 'telefone': '4329-4175'})

contatos.popitem()
# >> ('dev.judahlopes@gmail.com': {'nome': 'Pedro', 'telefone': '0239-9142'})

contatos.popitem()    
# >> KeyError    <-- quando o set está vazio

# ---- método .setdefault() ----
# Se key existe, ele apena retorna o valor. Se chave não existe, ele cria e add valor.

contato = {'nome': 'Pedro', 'telefone': '0239-9142'}

contato.setdefault("nome", "Giovanna")
# >> {'nome': 'Pedro', 'telefone':'0239-9142'}

contatos.setdefault("idade", 20)
# >> {'nome': 'Pedro', 'telefone':'0239-9142', 'idade': 20}

# ---- método .update() (atualiza o set, seja modificando keys existentes, seja adicionando novas) ----
contatos.update({'dev.judahlopes@gmail.com': {"nome": "Judah"}})

print(contatos)   
# >> {'dev.judahlopes@gmail.com': {"nome": "Judah"}}

contatos.update({'cacazinha@gmail.com': {"nome": "Maria"}})

print(contatos)
# >> {'dev.judahlopes@gmail.com': {"nome": "Judah"},  'cacazinha@gmail.com': {"nome": "Maria"}}

# ---- método in ----
'dev.judahlopes@gmail.com' in contatos  # >> True
'elonmusk@gmail.com' in contatos        # >> False

'idade' in contatos['dev.judahlopes@gmail.com']     # >> False
'telefone' in contatos['dev.judahlopes@gmail.com']  # >> True

# ---- método del (remove o argumento) ----
del contatos ['dev.judahlopes@gmail.com']['telefone']
print(contatos)
# >> {'dev.judahlopes@gmail.com': {'nome': 'Pedro' }}

del contatos ['dev.judahlopes@gmail.com']
print(contatos)
# >> {}