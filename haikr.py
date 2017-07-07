import random

def criarVocabulario(origem):
    # transformar esta parte em uma funcao geradora de dicionario
    palavras = []
    #  tira todas as palavras unicas do arquivo original
    with open(origem, 'r') as f:
        for line in f:
            for word in line.split():
                print(word)
                if word not in palavras:
                    palavras.append(word)
    #  cria o dicionario de palavras da obra original
    dicionario = open('dicionario.txt', 'w')
    for palavra in palavras:
        dicionario.write(palavra + "\n")
    dicionario.close()



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
#  cria o cancioneiro de poemas
cancioneiro = open('cancioneiro.txt', 'w')
count = 1
for item in poemas:
    cancioneiro.write(str(count) + ".\n")
    cancioneiro.write(item)
    count += 1
cancioneiro.close()
