import random

poemas = []

# Ler um novo arquivo wabisabi so com os haiku
with open('wabisabi2.txt', 'r') as brutos:
    count = 1
    entradas = []
    meios = []
    saidas = []
# dividir em verso 1, 2 e 3
    for line in brutos:
        if count == 1:
            entradas.append(line)
            count += 1
        elif count == 2:
            meios.append(line)
            count += 1
        elif count == 3:
            saidas.append(line)
            count = 1

# gera todas as combinacoes de poemas
for entrada in entradas:
    for meio in meios:
        for saida in saidas:
            poemas.append(entrada + "\n" + meio + "\n" + saida + "\n\n")
# randomiza
random.shuffle(poemas)
cancioneiro = open('cancioneiro140.txt', 'w')
count = 1
for item in poemas:
    if len(item) < 140:
        cancioneiro.write(str(count) + ".\n")
        cancioneiro.write(item)
        count += 1
cancioneiro.close()
