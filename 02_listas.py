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

# Traço separador
print("-" * 60)

# 2) INSERÇÃO DE UM NOVO ELEMENTO NO *FIM* DA LISTA: append()

nums.append(6)
legumes.append("mandioca")

print(nums)
print(legumes)

# Traço separador
print("-" * 60)

# 3) INSERÇÃO DE UM NOVO ELEMENTO NA POSIÇÃO ESPECIFICADA: insert()
#    Parâmetros:
#    1º ~> a posição onde será feita a inserção
#    2º ~> o novo elemento a ser inserido

# Inserindo um novo elemento na QUARTA posição
legumes.insert(3, "tomate")
print(legumes)

# Inserindo um novo elemento na PRIMEIRA posição
legumes.insert(0, "milho")
print(legumes)

# Traço separador
print("-" * 60)

# 4) ACESSANDO VALORES, INFORMANDO A RESPECTIVA POSIÇÃO
print("Elemento na QUINTA posição:", legumes[4])
print("Elemento na PRIMEIRA posição:", legumes[0])
print("Elemento na ÚLTIMA posição:", legumes[-1])
print("Elemento na PENÚLTIMA posição:", legumes[-2])

# Traço separador
print("-" * 60)

# 5) SUBSTITUINDO VALORES EXISTENTES

print("ANTES:", legumes)

# Substituindo o valor na posição 3 (QUARTA posição)
legumes[3] = "vagem"
# Substituindo o valor na posição 0 (PRIMEIRA posição)
legumes[0] = "nabo"
# Substituindo o valor na posição -1 (ÚLTIMA posição)
legumes[-1] = "inhame"

print("DEPOIS:", legumes)

# Traço separador
print("-" * 60)

# 6) DETERMINANDO A QUANTIDADE DE ELEMENTOS DA LISTA: len()
print("Quantidade de elementos da lista de legumes:", len(legumes))
print("Quantidade de elementos da lista de números:", len(nums))

# Traço separador
print("-" * 60)

# 7) REMOVENDO O ÚLTIMO ELEMENTO DE UMA LISTA: pop() (sem parâmetro)
print("ANTES:", legumes)
removido = legumes.pop()
print("Valor removido:", removido)
print("DEPOIS:", legumes)

# Traço separador
print("-" * 60)

# 8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmetro
removido = legumes.pop(3)       # Remove o elemento da posição 3
print("Valor removido da posição 3:", removido)
print(legumes)

removido = legumes.pop(0)       # Remove o primeiro elemento
print("Valor removido da primeira posição:", removido)
print(legumes)

# Traço separador
print("-" * 60)

# 9) REMOVENDO UM ELEMENTO POR SEU VALOR: remove()
legumes.remove("mandioquinha")  # Não retorna valor
print(legumes)

# Traço separador
print("-" * 60)

# 10) JUNTANDO (CONCATENANDO) DUAS LISTAS: extend()
mais_legumes = ["abobrinha", "quiabo", "jiló", "cabotiá", "cará"]

legumes.extend(mais_legumes)

print(legumes)

# Traço separador
print("-" * 60)

# 11) FATIANDO UMA LISTA
#     Fatiar significa copiar um pedaço da lista (uma sublista)
#     para uma nova lista

# Cria uma sublista que contém os elementos das posições 2 a 5
# (posição 6 NÃO entra)
sublista2_5 = legumes[2:6]
print("Sublista de 2 a 5:", sublista2_5)

# Cria uma sublista que contém os elementos desde o início a até
# a posição 6 (posição 7 NÃO entra)
sublista_inicio_6 = legumes[:7]
print("Sublista do início até a posição 6:", sublista_inicio_6)

# Cria uma sublista que contém os elementos da posição 4 até o final
sublista_4_fim = legumes[4:]
print("Sublista da posição 4 até o final:", sublista_4_fim)
