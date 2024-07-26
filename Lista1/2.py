nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

peso1 = 2
peso2 = 3
peso3 = 5

pesoSomado = peso1 + peso2 + peso3

mediaPonderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / pesoSomado

print(f"A média do aluno é : {mediaPonderada:.1f}")