# QUESTÃO 02 - Agora crie um algoritmo parecido com o da primeira questão, com a diferença de que não se 
# tem determinada a quantidade de valores que o usuário irá inserir. O programa deve parar de calcular a 
# média quando o usuário digitar o valor 0. (Utilize apenas o laço while)

notas = []
somaNotas = 0.0
media = 0.0
contador = 0
continuar = 1

print("***** Cálculo de Média *****")
print("1. Para continuar")
print("0. Para sair")

while continuar != 0:
    notas.append(float(input(f"Digite a {contador + 1}º nota: ")))
    somaNotas += notas[contador]
    contador += 1
    continuar = int(input("Deseja continuar? Sim = 1 / Não = 0: "))

media = somaNotas / len(notas)
print(f"Média  = {round(media, 1)}")