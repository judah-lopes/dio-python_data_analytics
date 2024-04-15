# São operadores utilizados para verificar se um objeto está presente em uma sequência.    
#      *como se fosse um includes()*

# - operador "em" (in)
curso = "Curso de Python"
frutas = ['laranja', 'uva', 'limão']
saques = [1500, 100]

"Python" in curso
# >> True    <--- string é uma sequência de caracteres

"maçã" not in frutas

200 in saques