pares = [2, 4, 6, 8, 10]
impares = [1, 3, 5, 7, 9, 11]


# Fazer uma função que receba uma lista de inteiros e devolva a soma dos seus elementos
def soma(lista):
    sum = 0
    # Exemplo: [4, 6, 2, 3, 9, 1, 10]
    for elemento in lista:  # primeira vez: 4, segunda vez: 6, ...
        sum = sum + elemento  # primeira vez: 0 + 4 = 4, segunda vez: 4 + 6 = 10, ...

    return sum

print(soma(pares))
print(soma(impares))
print(soma([4, 6, 2, 3, 9, 1, 10]))

# Exercicio 2:
# Fazer uma função que receba uma lista de inteiros
# e devolva o maior dos seus elementos
def maior(lista):
    max = lista[0]  # Assumimos que o maximo e o primeiro da lista
    for elemento in lista:  # Vamos percorrer a lista
        if elemento > max:  # Se o elemento em que estamos e maior que o maximo
            max = elemento  # Atualizamos o maximo

    return max  # Retornamos o maximo

print(maior(pares))
print(maior(impares))
print(maior([3, 7, 11, 1, 8, 5, 19, 2, 0, 5, 6, 17]))

# Exercicio 3:
# Fazer uma função que receba uma lista de strings e devolva a maior
nomes = ["filipa", "mario", "margarida", "leo", "clara", "mariana", "carolina", "olivia"]
def comprida(lista):
    comp = lista[0]
    for nome in lista:
        if len(nome) > len(comp):
            comp = nome

    return comp, len(comp)

print(comprida(nomes))


# Exercicio 4:
# Fazer uma função que receba uma lista de inteiros
# e devolva o menor dos seus elementos
def menor(lista):
    minimo = lista[0]
    for elemento in lista:  # [2, 1, 3, 4, 5]
        if elemento < minimo:
            minimo = elemento

    return minimo

print(menor(pares))
print(menor(impares))
print(menor([3, 7, 11, 1, 8, 5, 19, 2, 0, 5, 6, 17]))

# Exercicio 5:
# Fazer uma função que receba uma lista de strings
# e devolva a mais curta
nomes = ["filipa", "mario", "margarida", "leo", "clara", "mariana", "carolina", "olivia"]
def curta(lista):
    curt = lista[0]
    for elemento in lista:
        if len(elemento) < len(curt):
            curt = elemento

    return curt

print(curta(nomes))


# Exercicio 6: Fazer uma função que receba uma lista de inteiros e remova os repetidos
# Exemplo de lista = [2, 6, 4, 7, 2, 1, 3, 7, 2, 0, 9, 6, 6, 1, 3, 5]
def rep(lista):
    elementos = {}  # Exemplo de dicionarios: {"chave": "valor", "key": "value"}

    for elemento in lista:
        elementos[elemento] = True  # {2: True} ; {2: True, 6: True}; {2: True, 6: True, 4: True}

    return list(elementos.keys())

print(rep([2, 6, 4, 7, 2, 1, 3, 7, 2, 0, 9, 6, 6, 1, 3, 5]))

# Exercicio 7: Fazer uma função que receba uma lista de inteiros e
# retorna um dicionario com quantas vezes existe cada elemento
# Exemplo de lista = [2, 6, 4, 2, 1, 3, 7, 2, 0, 9, 6, 6, 1, 3, 5]
def conta(lista):
    elementos = {}

    for elemento in lista:
        if elemento in elementos:
            # somar
            elementos[elemento] = elementos[elemento] + 1  # {2: 2, 6: 1, 4:1}
        else:  # Primeira vez, poe la 1
            elementos[elemento] = 1  # {2: 1} {2: 1, 6: 1} {2: 1, 6: 1, 4: 1} {2: 2, 6: 1, 4: 1, 1: 1}

    return elementos

print(conta([2, 6, 4, 2, 1, 3, 7, 2, 0, 9, 6, 6, 1, 3, 5]))