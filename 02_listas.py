# LISTAS são uma estrutura de dados nativa da
# linguagem Python. Elas permitem que vários
# valores possam ser associados a uma única
# variável

# Lista de strings
legumes = ["batata", "cenoura", "beterraba", "mandioquinha", "batata doce"]

# Lista de números
nums = [3, 10, -7, 12.8, -0.5]

# Lista com valores de vários tipos
mistureba = ["Joaquim", 37, 1.81, 88, True]

## OPERAÇÕES SOBRE LISTAS ##

# 1) PERCURSO
# Percorrer uma lista significa visitar cada um de
# seus itens e fazer algo com ele. No exemplo abaixo,
# vamos dar print() em cada um dos legumes da lista
for leg in legumes:
    print(leg)

# Traço separador
print("-" * 60)

# Percorendo a lista de números e printando o valor
# do dobro de cada item
for n in nums:
    print(n * 2)
