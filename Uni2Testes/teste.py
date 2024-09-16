matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

coluna_0 = [linha[0]for linha in matriz]

print(coluna_0)

print(matriz[1][2])

for linha in matriz:
    for elemento in linha:
        print(elemento, end=' ')
        print()



def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)

print(fatorial(5))


def soma(a, b):
    return a + b

resultado = soma(10, 5)
print(resultado)

conjunto = {1,2,3,4,5}

conjunto.add(6)

conjunto.remove(2)
print(conjunto)

conjunto2 = {4,5,6,7,8}

uniao = conjunto | conjunto2

print(uniao)

interseccao = conjunto & conjunto2

print(interseccao)

diferenca = conjunto - conjunto2

print(diferenca)