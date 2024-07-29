n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

inicio = min(n1, n2)
fim = max(n1, n2)

soma = 0
multiplicacao = 1
impar = False

for i in range(inicio, fim + 1):
    if i % 2 == 0:
        soma += i

    else:
        multiplicacao *= i
        impar = True


print("soma pares: ", soma)
print("multiplicao impares: ", multiplicacao)