# QUESTÃO 08 - Escreva um programa que converta um valor binário (base 2) em um número decimal (base 10).
# Seu programa deve começar lendo o número binário de um usuário como uma string. Depois, ele deve calcular o
# equivalente decimal processando cada dígito do valor binário. No fim de tudo, o programa deve imprimir o 
# valor decimal.
# Ex: “001011” → 11

numeroBinario = input("Digite o número binário: ")
numeroBinario = numeroBinario[::-1]
numeroDecimal = 0
listaNumeros = []
for i, valor in enumerate(numeroBinario):
    listaNumeros.append((2 ** i) * int(valor))

for i, valor in enumerate(listaNumeros):
    numeroDecimal += listaNumeros[i]

print(numeroDecimal)