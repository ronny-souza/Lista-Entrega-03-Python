# QUESTÃO 04 - Uma universidade utiliza a tabela abaixo para mapear notas dadas com letras em valores decimais.
#
#   A+      A-      B+      B-      C+      C-      D+      D-
#   4.0     3.7     3.3     2.7     2.3     1.7     1.3     0
# 
# Seu programa deverá calcular o valor em pontos a partir de uma das notas com letras disponíveis na tabela,
# para os 13 alunos de uma turma. Cada nota inserida servirá para calcular a média da turma. Ao final, o 
# programa deve parar de solicitar as notas e este deve então imprimir todas as notas inseridas e a média
# calculada. (Utilize o laço for)

def converteNotas(nota):
    if nota.upper() == "A+":
        nota = float(4.0)
        return nota

    elif nota.upper() == "A-":
        nota = float(3.7)
        return nota

    elif nota.upper() == "B+":
        nota = float(3.3)
        return nota
    
    elif nota.upper() == "B-":
        nota = float(2.7)
        return nota
    
    elif nota.upper() == "C+":
        nota = float(2.3)
        return nota
    
    elif nota.upper() == "C-":
        nota = float(1.7)
        return nota
    
    elif nota.upper() == "D+":
        nota = float(1.3)
        return nota
    
    elif nota.upper() == "D-":
        nota = float(0.0)
        return nota
    
    else:
        print("A nota digitada não corresponde a nenhuma das possíveis!")

notas = []
notasConvertidas = []
somaNotas = 0.0
media = 0.0
for i in range(13):
    
    notas.append(input(f"Digite a {i + 1}º nota: "))
    notasConvertidas.append(converteNotas(notas[i]))
    somaNotas += notasConvertidas[i]

for i in range(len(notasConvertidas)):
    print(f"{i + 1}º nota: {notas[i].upper()} = {notasConvertidas[i]}")

media = somaNotas / len(notasConvertidas)
print("Média:", round(media, 1))