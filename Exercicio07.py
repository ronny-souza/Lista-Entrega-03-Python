# QUESTÃO 07 - O máximo divisor comum (M.D.C.) de dois inteiros positivos, n e m, é o maior número em que é 
# possível dividir estes dois inteiros ao mesmo tempo. Existem vários algoritmos que resolvem o problema de 
# encontrar o M. D. C., e um deles é o que segue:
# Inicialize d com o mínimo de m e n
# Enquanto divisão de m por n não é exata ou a
# divisão de n por d também não é exata:
# Decresça o valor de em d 1 unidade
# Exiba d como o maior divisor comum de m e n

m = int(input("Digite o valor de m: "))
n = int(input("Digite o valor de n: "))
d = n

if m > 0 and n > 0:

    while m % d != 0 or n % d != 0:
        d -= 1
    
    print(f"MDC de {m} e {n} = {d}")

else:
    print("Não é possível dividir por 0!")