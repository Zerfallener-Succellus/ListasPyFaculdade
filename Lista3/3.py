numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

menor = min(numero1, numero2)
maior = max(numero1, numero2)

pares = 0

for numero in range(menor, maior+1):
    if numero % 2 == 0:
        pares += 1


print(f"A quantidade de números pares entre {menor} e {maior} é {pares}.")