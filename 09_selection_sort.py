# Variáveis de contagem
comps = trocas = passd = 0

def selection_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO SELECTION SORT
    Isola (seleciona) o primeiro elemento da lista e, em seguida,
    encontra o menor valor no restante da lista. Se o valor
    encontrado for menor que o valor previamente selecionado,
    efetua a troca entre eles. Continuando, seleciona o segundo
    elemento da lista, buscando pelo menor valor nas posições
    subsequentes. Faz a troca entre os dois valores, se necessário.
    O processo se repete até que o penúltimo elemento da lista
    seja selecionado, comparado com o último e feita a troca entre
    eles, se for o caso.
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop que vai da primeira até a PENÚLTIMA posição, para
    # selecionar o elemento que será comparado aos demais
    for pos_sel in range(len(lista) - 1):

        passd += 1

        # Inicia supondo que a posição do menor valor do resto
        # da lista é o que está imediatamente à frente do selecionado
        pos_menor = pos_sel + 1

        # Percorre o restante da lista, da posição seguinte a pos_menor
        # até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor encontrado na posição pos for MENOR do que o
            # valor atual de pos_menor, então atualiza pos_menor para
            # a mesma posição de pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # <~ CUIDADO COM A INDENTAÇÃO!
        # Neste ponto, já terminamos de percorrer o restante da lista e
        # já sabemos a posição do menor elemento que há nele. Comparamos,
        # então, os valores das posições pos_menor e pos_sel. Se o
        # primeiro for MENOR do que o segundo, fazemos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

################################################################################

# nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

# Pior caso       
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        
# Melhor caso
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('ANTES:', nums)
selection_sort(nums)
print('DEPOIS:', nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

#############################################################
# TESTE COM 1M+ DE NOMES

import sys
sys.dont_write_bytecode = True  # Impede a criação do cache
from time import time

# Importando a lista de nomes
from data.nomes_desord import nomes

# Recortando os primeiros 10k nomes
nomes = nomes[:10000]

hora_ini = time()
selection_sort(nomes)
hora_fim = time()
print(nomes)    # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")