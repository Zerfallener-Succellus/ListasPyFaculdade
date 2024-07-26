numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

numeros = [numero1, numero2, numero3]

menor = min(numeros)

maior = max(numeros)

print("O menor número digitado foi {}".format(menor))
print("O maior número digitado foi {}".format(maior))