
numero = int(input("Digite um número inteiro: "))


if numero % 2 == 0:
    tipo_paridade = "par"
else:
    tipo_paridade = "ímpar"


if numero > 0:
    tipo_sinal = "positivo"
elif numero < 0:
    tipo_sinal = "negativo"
else:
    tipo_sinal = "zero"


print(f"O número {numero} é {tipo_paridade} e {tipo_sinal}.")
