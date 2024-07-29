
pares=[]
impares=[]

for i in range(10):
    numero = int(input(f"Digite o {i+1} numero: "))

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Esses sao os pares: ", pares)
print("Esses sao os impares: ", impares)