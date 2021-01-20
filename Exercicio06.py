# O valor de π (pi) pode ser aproximando pela seguinte série infinita:
# -> Tabela aqui <-
#
# Escreva um programa que exiba 15 aproximações de π. A primeira aproximação deve fazer uso apenas do primeiro
# termo da série infinita (3). Cada próxima aproximação exibida pelo seu programa deve incluir um ou mais 
# termos na série. (Utilize o laço for)

aproximacao = []
par1 = 2
par2 = 3
par3 = 4
resultadoNumeros = 0.0
pi = 3

for i in range(15):
    aproximacao.append(4/ (par1 * par2 * par3))
    par1 += 3
    par2 += 3
    par3 += 3

resultadoNumeros += aproximacao[0]
for i, aprox in enumerate(aproximacao):
    if i != 0:
        resultadoNumeros -= aproximacao[i]

pi += resultadoNumeros
print(f"15 aproximações de PI equivalem a {pi}")



