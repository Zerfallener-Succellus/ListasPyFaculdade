
def fatorial_iterativo(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


numero = int(input("Digite um número inteiro para calcular o fatorial: "))


fatorial = fatorial_iterativo(numero)


if fatorial is None:
    print("O fatorial não está definido para números negativos.")
else:
    print(f"O fatorial de {numero} é {fatorial}.")
