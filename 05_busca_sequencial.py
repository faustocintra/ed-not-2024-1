def busca_sequencial(lista, val):
    """
    Função que realiza uma busca sequencial em uma lista,
    procurando por val.
    Se val for encontrado, retorna a posição de val na lista.
    Caso contrário, retorna o valor convencional -1.
    """
    # Percorre a lista do início ao fim usando range() e len()
    # (é necessário ter acesso às posições dos elementos)
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    # <-- CUIDADO COM A INDENTAÇÃO AQUI!
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1
##############################################################

# Lista de números para testar
nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

# TESTES

pos30 = busca_sequencial(nums, 30)
print(f"Elemento 30 encontrado na posição {pos30}")

pos_menos15 = busca_sequencial(nums, -15)
print(f"Elemento -15 encontrado na posição {pos_menos15}")

pos19 = busca_sequencial(nums, 19)
print(f"Elemento 19 encontrado na posição {pos19}")

print("-" * 40)

############################################################

import sys
sys.dont_write_bytecode = True

from time import time

# TESTES COM NOMES
from data.nomes_completos import nomes

hora_ini = time()
resultado1 = busca_sequencial(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {resultado1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultado2 = busca_sequencial(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERREIRA encontrado na posição {resultado2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultado3 = busca_sequencial(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição {resultado3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultado4 = busca_sequencial(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontado na posição {resultado4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")