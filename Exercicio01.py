# QUESTÃO 01 - Crie um programa que calcule a média aritmética de um conjunto de 8 valores (podem ser 
# inteiros ou float) que deve ser inserido pelo usuário. Ao final, o algoritmo deve exibir a média calculada.
# a) Utilize o laço while 
# b) Utilize o laço for

notas = []
somaNotas = 0.0
media = 0.0
contador = 0

# a)
print("A) USANDO O WHILE: ")
while contador < 8:
    notas.append(float(input(f"Digite a {contador + 1}º nota: ")))
    somaNotas += notas[contador]
    contador += 1

media = somaNotas / len(notas)
print(f"Média  = {media}")

notas = []
somaNotas = 0.0
media = 0.0

# b)
for i in range(8):
    notas.append(float(input(f"Digite a {i + 1}º nota: ")))
    somaNotas += notas[i]

media = somaNotas / len(notas)
print(f"Média = {media}")