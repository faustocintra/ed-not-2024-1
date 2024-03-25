# Variáveis de contagem
passd = comps = trocas = 0

def quick_sort(lista, ini = 0, fim = None):
    """
    ALGORITMO DE ORDENAÇÃO QUICK SORT
    Escolhe um dos elementos da lista para ser o pivô
    (na nossa implementação, será o último) e, na primeira
    passada, divide a lista, a partir da posição final do
    pivô, em uma sublista à esquerda, contendo apenas
    valores menores que o pivô, e outra sublista à direita,
    contendo apenas valores maiores que o pivô.
    Em seguida, recursivamente, repete o processo em cada
    uma das sublistas, até que toda a lista esteja ordenada.
    """
    global passd, comps, trocas

    # Quando não soubermos o valor da variável 'fim',
    # atribuímos o valor da última posição da lista
    if fim is None: fim = len(lista) - 1

    # Para que o algoritmo trabalhe, é necessário que a
    # faixa delimitada pelas variáveis 'ini' e 'fim' tenha,
    # pelo menos, dois elementos. Caso contrário, saímos da
    # função sem fazer nada
    if fim <= ini: return

    # Inicialização das variáveis
    pivot = fim
    div = ini - 1

    passd += 1

    # Percorre a lista da posição 'ini' até a posição 'fim' - 1
    for pos in range(ini, fim):
        # Se o elemento na posição 'pos' for MENOR do que o
        # elemento na posição 'pivot', executa algumas ações
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1   # Avança 'div' em uma posição
            # Efetua a troca entre os elementos das posições
            # 'pos' e 'div', caso sejam diferentes entre si
            if(pos != div):
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    # <~ CUIDADO COM A INDENTAÇÃO AQUI
    # Depois que 'pos' chega à sua posição final, 'div' deve
    # ser incrementado uma última vez
    div += 1

    # Troca os elementos das posições 'div' e 'pivot' entre
    # si, colocando este último em seu lugar, se forem distintos
    if(div != pivot):
        lista[div], lista[pivot] = lista[pivot], lista[div]
        trocas += 1

    # Agora, todos os elementos à esquerda do pivô são MENORES
    # do que ele, enquanto todos os elementes à sua direita
    # são MAIORES do que ele. Chamamos a função recursivamente
    # para cada uma dessas sublistas
    quick_sort(lista, ini, div - 1)   # Sublista da esquerda
    quick_sort(lista, div + 1, fim)   # Sublista da direita

###############################################################

#nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#nums = [9, 0, 1, 2, 3, 4, 5, 6, 7, 8]
nums = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]

print('ANTES:', nums)
quick_sort(nums)
print('DEPOIS:', nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

#############################################################
# TESTE COM 1M+ DE NOMES

import sys, tracemalloc
sys.dont_write_bytecode = True  # Impede a criação do cache
from time import time

# Importando a lista de nomes
from data.nomes_desord import nomes

# Recortando os primeiros 10k nomes
#nomes = nomes[:10000]

passd = comps = trocas = 0

tracemalloc.start()         # Inicia medição do consumo de memória
hora_ini = time()
quick_sort(nomes)
hora_fim = time()

# Captura as informações de gasto de memória
mem_atual, mem_pico = tracemalloc.get_traced_memory()
tracemalloc.stop()          # Termina a medição de memória

print(nomes)    # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")
print(f"Pico de memória: { mem_pico / 1024 / 1024 }MB")
