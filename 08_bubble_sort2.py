# Variáveis de contagem
comps = trocas = passd = 0

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR do que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última passada,
    nenhuma troca tenha sido efetuada.    
    """
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop eterno; não sabemos antecipadamente quantas passadas
    # serão necessárias
    while True:

        passd += 1

        # Variável que controla se houve trocas na passada
        trocou = False

        # Percurso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição
        # VERSÃO 2: o range encolhe à medida que o número de
        # passadas aumenta
        for pos in range(len(lista) - passd):

            # Se o valor que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # efetuamos uma TROCA
            if lista[pos + 1] < lista[pos]:
                # Troca
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocas += 1
                trocou = True   # Houve troca na passada

            comps += 1

        print(lista)

        # Se não houve trocas na passada, a lista está ordenada
        # e interrompemos o loop eterno while True
        # <~ CUIDADO COM A INDENTAÇÃO
        if not trocou:
            break

#########################################################################
        
nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

# Pior caso       
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        
# Melhor caso
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print('ANTES:', nums)
bubble_sort(nums)
print('DEPOIS:', nums)
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")

exit()  # Termina o progama aqui

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
bubble_sort(nomes)
hora_fim = time()
print(nomes)    # Lista após ordenação
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")
print(f"Passadas: {passd}; comparações: {comps}; trocas: {trocas}")