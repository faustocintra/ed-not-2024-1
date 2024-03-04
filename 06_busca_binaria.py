comps = 0       # Contador de comparações

def busca_binaria(lista, val):
    """
    ALGORITMO DE BUSCA BINÁRIA
    Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
    e um valor de busca, divide a lista em duas partes,
    procurando pelo valor de busca apenas na metade onde
    o valor de busca poderia estar. Novas subdivisões são
    feitas até que se encontre o valor de busca ou que
    reste apenas uma sublista vazia, quando então se
    conclui que o valor de busca não existe na lista
    """

    # Declaramos que queremos usar a variável global comps
    # inicializada na linha 1
    global comps
    comps = 0

    ini = 0                 # Posição inicial da lista
    fim = len(lista) - 1    # Posição final da lista

    while ini <= fim:
        # Calculando o meio da lista
        meio = (ini + fim) // 2     # Divisão inteira

        # Verifica se o valor que está no meio da lista
        # é igual ao valor de busca. Em caso afirmativo,
        # retornamos a posição do meio, pois o valor de
        # busca foi encontrado
        if val == lista[meio]:
            comps += 1
            return meio
        
        # Senão, se o valor de busca é MENOR do que o
        # valor do meio, reinicia a busca na metade esquerda
        # da (sub)lista
        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        # Por fim, se o valor de busca é MAIOR do que o
        # valor do meio, reinicia a busca na metade direita
        # da (sub)lista
        else:
            comps += 2
            ini = meio + 1

    # <- CUIDADO COM A INDENTAÇÃO AQUI!
    # Se chegamos a este ponto, é porque o valor de busca não
    # existe na lista
    return -1

############################################################

import sys
sys.dont_write_bytecode = True

from time import time

# TESTES COM NOMES
from data.nomes_completos import nomes

hora_ini = time()
resultado1 = busca_binaria(nomes, "EDSON PEREIRA")
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição {resultado1}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultado2 = busca_binaria(nomes, "MARIA FERREIRA")
hora_fim = time()
print(f"MARIA FERREIRA encontrado na posição {resultado2}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")


hora_ini = time()
resultado3 = busca_binaria(nomes, "VALDIR SILVA")
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição {resultado3}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

hora_ini = time()
resultado4 = busca_binaria(nomes, "GILCINEIA GARCIA")
hora_fim = time()
print(f"GILCINEIA GARCIA encontado na posição {resultado4}")
print(f"Comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")