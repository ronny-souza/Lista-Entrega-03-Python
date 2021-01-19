# QUESTÃO 05 - Um zoológico determina que o preço da entrada é baseado na idade do visitante. Visitantes com 
# até 2 anos de idade não pagam. Crianças de 3 a 12 anos pagam R$ 10,00. Idosos a partir dos 65 anos pagam 
# R$ 15,00. Demais pessoas pagam R$ 20,00.
# Crie um programa que ao chegar uma família, pergunta a idade de cada um dos componentes dessa família e no 
# final calcule o valor devido. O programa deve parar e exibir o resultado quando for digitado um valor vazio à 
# pergunta sobre a idade. O valor deve ser exibido no formato em reais.

def valorPorIdade(idade):

    if idade >= 0 and idade <= 2:
        valor = 0.0
        return valor
    
    elif idade >= 3 and idade <= 12:
        valor = 10.0
        return valor
    
    elif idade >= 13 and idade < 65:
        valor = 20.0
        return valor

    else: 
        valor = 15.0
        return valor


valores = []
somaValores = 0.0

while True:
    
    idade = input("Digite a idade: ")
    
    if idade != "":
        valores.append(valorPorIdade(int(idade)))       

    else: 
        for i in range(len(valores)):
            somaValores += valores[i]    
        break


print(f"Total: R$ {round(somaValores, 2)}")
