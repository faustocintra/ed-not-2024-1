# range() é uma função que gera uma faixa de números.
# É muito usada em associação com listas

# 1) range() COM *UM* PARÂMETRO
#    Gera uma faixa numérica que vai de 0 (zero) até o valor
#    do parâmetro - 1
for num in range(10):
    print(num)

print("-" * 60)

# 2) range() COM *DOIS* PARÂMETROS
#    1º parâmetro ~> valor inicial da faixa
#    2º parâmetro ~> valor final da faixa (não incluído)
for x in range(10, 16):
    print(x)

print("-" * 60)

# 3) range() COM *TRÊS* PARÂMETROS
#    1º parâmetro ~> valor inicial da faixa
#    2º parâmetro ~> valor final da faixa (não incluído)
#    3º parâmetro ~> passo (intervalo entre um número e outro)
for n in range(1, 22, 3):   # De 1 a 21 contando de 3 em 3
    print(n)

print("-" * 60)

# range() com passo negativo
for i in range(10, 0, -1):  # Contagem regressiva de 10 a 1
    print(i)