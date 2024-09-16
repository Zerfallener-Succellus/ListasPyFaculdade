matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def transpor_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

matriz_transp = transpor_matriz(matriz)

for linha in matriz_transp:
    print(linha)


def soma_elementos_matriz(matriz):
        return sum(sum(linha) for linha in matriz)

soma = soma_elementos_matriz(matriz)
print(soma)

matriz2 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8]
]

matriz2_tranp = transpor_matriz(matriz2)

for linha in matriz2_tranp:
    print(linha)