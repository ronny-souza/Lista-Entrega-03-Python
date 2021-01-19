# QUESTÃO 03 - Uma varejista está dando 60% de desconto em uma variedade de produtos para queima de estoque. 
# Ela gostaria de ajudar seus clientes a calcular a redução de preço nos anúncios imprimindo uma tabela de 
# descontos que mostra o preço original e o preço depois do desconto aplicado. Escreva um programa que receba
# vários preços de produtos e que no final imprima uma tabela com o preço original e o preço novo. 
# Deixe o formato em reais.

# porcentDesconto = 60
# preco = 100.00
# precoFinal = (preco * porcentDesconto) / 100
# print(precoFinal)

preco = 0.0
precos = []
precoDesconto = 0.0
precosDesconto = []
porcentDesconto = 60.0
desconto = 0.0
contador = 0
continuar = "SIM"

while continuar != 0:
  
    preco = float(input("Digite o preço original: R$ "))
    precos.append(preco)
    desconto = (preco * porcentDesconto) / 100
    precosDesconto.append(preco - desconto)
    continuar = int(input("Deseja continuar ? 1 = Sim / 0 = Não "))

for i in range(len(precos)):
    print(f"Preço do {contador + 1}º produto: R$ {precos[i]}\t | Com Desconto: R$ {precosDesconto[i]}")
    contador += 1
