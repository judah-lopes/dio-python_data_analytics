#! -------- Tópico 3 - Variáveies e Constantes --------

# ===== etapa 1 - constante =====
#   
#   Não existe constante em python. Como >CONVENÇÃO<, quando
#   queremos uma constante, escrevemos o nome da variável TODA em maiúsculo.

AGE = 19

print(AGE)

# ===== etapa 2 - boas práticas =====
#   
#   - O padrão dos nomes deve ser o snake case. ("preço_total")
#   - Escolher nomes sujestivos.
#   - Nome de constantes todos em MAIÚSCULO.

SALDO = 10000

limite_saque_diário = 1000

dias_para_acabar_o_saldo = SALDO / limite_saque_diário

print(f'Serão necessários {int(dias_para_acabar_o_saldo)} para sacando o limite de R${float(limite_saque_diário)} para o dinheiro do saldo acabar.')

