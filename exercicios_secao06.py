"""
Exercícios da Seção 6 do curso de Python da Geek University na Udemy

Exercícios básicos de Loops de Repetição
"""
# 1. Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, conside-rando números maiores que O.
"""
for numeros in range(1, 16):
    if numeros % 3 == 0:
        print(numeros)
"""
# 2. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira vez deve usar a estrutura
# de repetição for, e a segunda while
"""
for numeros in range(1, 101):
    print(numeros)

num = 1
while num < 101:
    print(num)
    num += 1  # Mesma coisa que num = num + 1
"""
# 3. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva na tela, iniciando em 10
# e terminando em 0. Mostrar uma mensagem "FIM!" após a contagem.
"""
numero = 10

while numero >= 1:
    print(numero)
    numero -= 1  # Mesma coisa que num = num - 1
print("FIM")
"""
# 4. Escreva um programa que declare um inteiro, inicialize-o com O, e incremente-o de 1000 em 1000, imprimindo seu
# valor na tela, até que seu valor seja 100000 (cem mil).
"""
for num in range(0, 101000, 1000):
    print(num)
"""
# 5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
soma = 0
for n in range(1, 11):
    numero = int(input(f'Informe o {n}º valor: '))
    soma = soma + numero
print(f'A soma é {soma}')
"""
# 6. Faça um programa que leia 10 inteiros e imprima sua média.
"""
soma = 0
contador = 0

for n in range(1, 11):
    numero = int(input(f'Informe o {n}º valor: '))
    soma += numero
    contador = 10
media = soma / contador
print(f'A média é {media}')
"""
# 7. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.
"""
soma = 0
contador = 0
media = 0
for n in range(1, 11):
    numero = int(input(f'Informe o {n}º valor: '))
    if numero > 0:
        soma += numero
        contador += 1
    if contador == 0:
        print("Nenhum número positivo foi digitado")
    else:
        media = soma / contador
print(f'A média é {media:.2f}')
"""
# 8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.
"""
numeros = []

for n in range(1, 11):
    num = float(input(f"Digite o {n}º número: "))
    numeros.append(num)  # Adiciona o valor digitado ao final da lista
menor = min(numeros)
maior = max(numeros)

print(f"O maior número digitado foi: {maior} e o menor foi: {menor}")
"""
# 9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros núrneros naturais ímpares.
"""
n = int(input("Digite um número inteiro positivo: "))
numero = 0
contador = 0

while contador < n:
    if numero % 2 != 0:
        print(numero)
        contador += 1
    numero += 1
"""
# 10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""
soma = 0
contador = 0
for num in range(1, 101):
    if num % 2 == 0:
        soma += num
        contador += 1
        if contador == 50:
            break

print(f"A soma dos 50 primeiros números pares é: {soma}")
"""
# 11. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
# de O até N em ordem crescente.
"""
n = int(input("Digite um número inteiro positivo: "))

for i in range(n+1):
    print(i)
"""
# 12. Faça um programa que leia um número inteiro positivo N e imprima todos os números naturais
# de 0 até N em ordem decrescente.
"""
n = int(input("Digite um número inteiro positivo: "))

for i in range(n, -1, -1):
    print(i)
"""
# 13. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
# de O até N em ordem crescente.
"""
n = int(input("Digite um número inteiro e par positivo: "))

for i in range(0, n+1, 2):
    print(i)
"""
# 14. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares
# de O até N em ordem decrescente.
"""
n = int(input("Digite um número inteiro e par positivo: "))

for i in range(n, -1, -2):
    print(i)
"""
# 15. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares
# de 1 até N em ordem crescente.
"""
n = int(input("Digite um número inteiro e ímpar positivo: "))

for i in range(1, n+1, 2):
    print(i)
"""
# 16. Faça um programa que leia um número inteiro positivo ímpar N e imprima todos os números ímpares
# de 1 até N em ordem decrescente.
"""
n = int(input("Digite um número inteiro e ímpar positivo: "))

for i in range(n, 0, -2):
    print(i)
"""
# 17. Faça um programa que leia um número inteiro positivo "n" e calcule a soma dos "n" primeiros números naturais.
"""
n = int(input("Digite um número inteiro positivo: "))
soma = 0

for i in range(1, n+1):
    soma += i

print(f'A soma dos {n} primeiros números naturais é: {soma}')
"""
# 18. Escreva um algoritmo que leia certa quantidade de números e imprima o maior deles e quantas vezes o maior número
# foi lido. A quantidade de números a serem lidos deve ser fomecida pelo usuário.
"""
quantidade_numeros = int(input("Digite a quantidade de números a serem lidos: "))
maior = float('-inf')  # Maior número iniciado com valor negativo infinito
vezes_maior = 0

for i in range(quantidade_numeros):
    numero = float(input(f"Digite o {i+1}º número: "))
    # Verifica se o número é o maior até o momento
    if numero > maior:
        maior = numero
        vezes_maior = 1
    # Verifica se o número é igual ao maior até o momento
    elif numero == maior:
        vezes_maior += 1

print(f"O maior número digitado foi {maior}, que apareceu {vezes_maior} vezes.")
"""
# 19. Escreva um algoritmo que leia um número inteiro entre 100 e 999 e imprima na saída cada um dos algarismos que
# compõem o número
"""
numero = int(input("Digite um número de 100 a 999: "))

# % é usado para obter o dígito mais à direita do inteiro e 
# a divisão inteira // é usada para remover esse dígito do inteiro

while numero > 0:
    digito = numero % 10  # Pega o último dígito do número
    print(digito)
    numero = numero // 10  # Remove o último dígito do número
"""
# 20. Ler uma sequência de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de
# dados lidos e número de valores pares. O processo termina quando for digitado o número 1000.
"""
numero = 0
contador = 0
pares = 0

# LOOP INFINITO QUE SÓ PARA QUANDO DIGITAR 1000
while numero != 1000:
    numero = int(input("Digite um número inteiro (ou 1000 para parar): "))
    if numero != 1000:
        contador += 1
        if numero % 2 == 0:
            pares += 1
            print(numero, "é par")
        else:
            print(numero, "é ímpar")

print(f"Foram lidos {contador} números, e dentre eles {pares} são pares.")
"""
# 21. Faça um programa que receba dois núneros. Calcule e mostre:
# a soma dos números pares desse intervalo de números, incluindo os números digitados;
# a multiplicação dos números ímpares desse intervalo, incluindo os digitados;
"""
numero1 = int(input("Insira o 1º número: "))
numero2 = int(input("Insira o 2º número: "))

soma_pares = 0  # Inicializa a variável de soma dos pares
multiplicacao_impares = 1  # Inicializa a variável de multiplicação dos ímpares

for num in range(numero1, numero2+1):
    if num % 2 == 0:
        soma_pares += num
    else:
        multiplicacao_impares *= num
print(f'A soma dós números pares é: {soma_pares} e a multiplicação dos números ímpares é: {multiplicacao_impares}.')
"""
# 22. Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado,
# uma sequência arbitrária de notas (válidas no intervalo de 10 a 20) e que mostre na tela,
# como resultado, a correspondente média aritmética. O número de notas com que o aluno
# pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
# introduzido um valor que não seja válido como nota de aprovação.
"""
soma_notas = 0
quant_notas = 0
nota = int(input("Digite uma nota entre 10 e 20 (ou uma nota fora do intervalo para sair): "))

while 10 <= nota <= 20:
    soma_notas += nota
    quant_notas += 1
    nota = int(input("Digite outra nota (ou uma nota fora do intervalo para sair): "))
if quant_notas > 0:
    media = soma_notas / quant_notas
    print(f"A média aritmética é: {media}")
else:
    print("Nenhuma nota válida foi inserida.")
"""
# 23. Faca um algoritmo que leia um número positivo e imprima seus divisores.
"""
num = int(input("Digite um número positivo: "))

print(f"Os divisores de {num} são:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
"""
# 24. Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores
# desse número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 + 66 = 144
"""
soma_num = 0
num = int(input("Digite um número positivo: "))

for i in range(1, num + 1):
    if num % i == 0:
        soma_num += i

print(f"Os divisores de {num} somados são: {soma_num}")
"""
# 25. Faça um programa que some todos os números naturais abaixo de 1000 que São múltiplos de 3 ou 5.
"""
soma_num = 0
for i in range(1, 1001):
    if i % 5 == 0 or i % 3 == 0:
        soma_num += i
print(f"A soma dos números naturais abaixo de 1000 que são múltiplos de 3 ou 5 é: {soma_num}")
"""
# 26. Faca um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número dado.
"""
numero = int(input("Digite um número: "))

while True:
    numero += 1
    if numero % 11 == 0 or numero % 13 == 0 or numero % 17 == 0:
        print("O primeiro múltiplo de 11, 13 ou 17 após o número digitado é:", numero)
        break
"""
# 27. Em Matemática, o número harmónico designado por Il(n) define-se como sendo a soma da série harmónica:
# H(n) 1 + 1/2 + 1/3 + 1/4 + ... + 1/n
# Faça um programa que leia um valor n inteiro e positivo e apresente o valor de H(n).
"""
n = int(input("Digite um valor inteiro e positivo para n: "))
h = 0

for i in range(1, n+1):
    h += 1/i

print(f"O valor de H(n) é: {h}")
"""
# 28. Faça um programa que leia um valor N inteiro e positivo, calcule o mostre o valor E, conforme a fórmula a seguir
# E = 1 + 1/1! + 1/2! + 1/3! + ... + 1/N!
"""
n = int(input("Digite um valor inteiro e positivo para n: "))
h = 0
e = 0

for i in range(1, n+1):
    e += 1 + 1/i

print(f"O valor de E é: {e}")
"""
# 29. Escreva um programa para calcular o valor da série, para 5 termos.
# S = 0 + 1/2! + 2/4! + 3/6! + ...
"""
import math

s = 0

for i in range(6):
    s += i / math.factorial(2*i)

print(f"O valor da série para 5 termos é: {s}")
"""
# 30. Faça programas para calcular as seguintes sequências:
# 1 + 2 + 3 + 4 + 5+ ... + n
# 1 - 2 + 3 - 4 + 5 + ... + (2n - 1)
# 1 + 3 + 5 + 7 + ... + (2n - 1)
"""
n = int(input("Digite um valor inteiro para n: "))
soma = 0

for i in range(1, n+1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")

n = int(input("Digite um valor inteiro para n: "))
soma = 0
sinal = 1

for i in range(1, 2*n, 2):
    soma += sinal * i
    sinal *= -1

print(f"A soma alternada de 1 até {2 * n - 1} é: {soma}")

n = int(input("Digite um valor inteiro para n: "))
soma = 0

for i in range(1, 2*n, 2):
    soma += i

print(f"A soma dos números ímpares de 1 até {2 * n - 1} é: {soma}")
"""
# 31. Faça um programa que calcule e escreva o valor de S
# S = 1/1 + 3/2 + 5/3 + 7/4 ... 99/50
"""
s = 0

for i in range(1, 51):
    s += (2*i-1) / i

print(f"O valor de S é: {s}")
"""
# 32. Faça um programa que simula o lançamento de dois dados, dl e d2, n vezes, e tem como
# saída o número de cada dado e a relação entre eles (>,<,=) de cada lançamento.
"""
import random

n = int(input("Digite o número de lançamentos: "))

for i in range(n):
    # lançamento dos dados
    d1 = random.randint(1, 11)
    d2 = random.randint(1, 11)
    # exibição dos resultados
    print(f"Lançamento {i + 1}")
    print(f"Dado 1: {d1}")
    print(f"Dado 2: {d2}")
    # determinação da relação entre os dados
    if d1 > d2:
        print("Dado 1 é maior")
    elif d2 > d1:
        print("Dado 2 é maior")
    else:
        print("Dados iguais")
    print()  # linha em branco para separar os resultados
"""
# 33. Dados n e dois números inteiros positivos, i e j, diferentes de O, imprimir em ordem
# crescente os n primeiros naturais que são múltiplos de i ou dej e ou de ambos. Exemplo:
# Para n = 6, i = 2 e j = 3 a saída deverá ser: 0,2,3,4,6,8.
"""
n = int(input("Digite a quantidade de resultados: "))
i = int(input("Digite o valor do 1º múltiplo: "))
j = int(input("Digite o valor do 2º múltiplo: "))

multiplos = []
num = 0

while len(multiplos) < n:
    if num % i == 0 or num % j == 0:
        multiplos.append(num)
    num += 1
print(f"Os {n} primeiros múltiplos de {i} ou {j} são {sorted(multiplos)}")
"""
# 34. Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20?
# Ex: 2520 é o menor número que pode ser dividido por um dos números de 1 a 10, sem sobrar resto.
"""
mmc_total = 1

for i in range(1, 21):  # Inicializa as variáveis de mdc e mdc_temp com os valores de i e mmc_total, respectivamente
    mdc = i
    mdc_temp = mmc_total
    while mdc_temp % mdc != 0:  # Usa o algoritmo de Euclides para encontrar o MDC
        temp = mdc
        mdc = mdc_temp % mdc
        mdc_temp = temp
    mmc_total = mmc_total * i // mdc  # Calcula o MMC utilizando a fórmula
print(mmc_total)  # Imprime o resultado
"""
# 35. Faça um programa que some os números impares contidos em um intervalo definido
# pelo usuário. O usuário define o valor inicial do intervalo e o valor final deste intervalo
# e o programa deve somar todos os números ímpares contidos neste intervalo. Caso o
# usuário digite um intervalo inválido (começando por um valor maior que o valor final) deve
# ser escrito uma mensagem de erro na tela, "Intervalo de valores inválido" e o programa termina.
# Exemplo de tela de saída:
# Digite o valor inicial e valor final: 5 10
# Soma dos ímpares neste intervalo: 21
"""
valor_inicial = int(input("Digite o valor inical do intervalo: "))
valor_final = int(input("Digite o valor final do intervalo: "))
num = 0

for i in range(valor_inicial, valor_final + 1, 2):
    if valor_inicial > valor_final:
        print("Intervalo de valores inválido")
    else:
        num += i
print(f"Soma dos ímpares neste intervalo: {num}")
"""
# 36. Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros
# 100 números naturais e o quadrado da soma. Ex: A soma dos dez primeiros números naturais : 1² + 2² + ... 10² = 385
# O quadrado da soma dos dez primeiros números naturais é: (1 + 2 + .. 10)² = 552 = 3025
# A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da soma é 3025-385 = 2640.
"""
soma_quadrados = 0
soma = 0

for i in range(1, 101):
    soma_quadrados = i ** 2
    soma += i

quadrado_soma = soma ** 2
diferenca = quadrado_soma - soma_quadrados

print(f"A diferença entre a Soma dos Quadrados e o Quadrado da Soma dos 100 primeiros números é: {diferenca}")
"""
# 37. Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) possuem a propriedade seguinte:
# a soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem ao quadrado é igual ao
# próprio numero. Por exemplo, para o inteiro 3025, temos que: 30 + 25 = 55 / 55² = 3025
"""
for i in range(1000, 10000):  # Separa os dígitos do número em duas partes: os dois dígitos de mais alta ordem e os dois dígitos de mais baixa ordem
    maior_numero = i // 100
    menor_numero = i % 100
    soma_numeros = maior_numero + menor_numero
    soma_quadrados = soma_numeros ** 2
    if i == soma_quadrados:
        print(i)
"""
# 38. Faça um programa que calcule o terno pitagórico a, b, c, para o qual a+b+c = 1000 Um terno pitagórico é
# um conjunto de três números naturais, a, b, c, para a qual, a² + b² = c². Por exemplo, 3² + 4² = 9 + 16 = 25 = 5²
"""
for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = 1000 - a - b
        if c > 0 and c ** 2 == a ** 2 + b ** 2:
            print(f"O terno pitagórico é {a}, {b}, {c}")
            break
"""
# 39. Faça um programa que calcule a área de um triângulo, cuja base e altura são fornecidas pelo usuário.
# Esse programa não pode permitir a entrada de dados inválidos, ou seja, medidas menores ou iguais a O.
"""
base = float(input("Digite o valor da base do triângulo: "))
altura = float(input("Digite o valor da altura do triângulo: "))
area = 0

if base <= 0 or altura <= 0:
    print("Valor inválido, digite um número maior que 0")
else:
    area = (base * altura) / 2
    print(f'O valor da área de um triângilo com base de {base} e altura de {altura} é: {area}')
"""
# 40. Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo.
# O programa tem que retornar o maior e o menor número lido.
"""
maior = float('-inf')
menor = float('inf')

# LOOP INFINITO QUE SÓ PARA QUANDO DIGITAR VALOR NEGATIVO
while True:
    num = int(input("Digite um número inteiro: "))
    if num < 0:
        break
    # Comparamos o número digitado com as variáveis maior e menor.
    elif num > maior:  # Se o número for maior que a variavel maior, atualizamos o valor de maior.
        maior = num
    elif num < menor:  # Se for menor que a variavel menor, atualizamos o valor de menor.
        menor = num

print(f"O maior número lido foi {maior} e o menor foi {menor}.")
"""
# 41. Faça um programa que calcula a associação em paralelo de dois resistores RI e R2 fornecidos pelo usuário
# via teclado. O programa fica pedindo estes valores e calculando até que o usuário entre com um valor para resistência
# igual a zero. R = R1 * R2 / R1 + R2
"""
while True:
    r1 = float(input("Digite o valor de R1: "))
    r2 = float(input("Digite o valor de R2: "))
    if r1 == 0 or r2 == 0:
        break
    else:
        r = (r1 * r2) / (r1 + r2)
        print(f"{r:.2f}")
"""
# 42. Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
# escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.
"""
import math

while True:
    valor = float(input("Digite um valor (digite 0 ou um valor negativo para encerrar): "))
    if valor <= 0:
        print("Programa encerrado!!")
        break
    quadrado = valor ** 2
    cubo = valor ** 3
    raiz_quadrada = math.sqrt(valor)
    print(f"Para o valor {valor}:\nquadrado = {quadrado}\ncubo = {cubo}\nraiz quadrada = {raiz_quadrada}\n")
"""
# 43. Faça um programa que leia um número indeterminado de idades de indivíduos (pare quando for informada a idade O),
# e calcule a idade média desse grupo.
"""
idades = []
while True:
    i = int(input("Digite a idade do indivíduo ou digite 0 para sair: "))
    if i == 0:
        print("Programa encerrado!!")
        break
    idades.append(i)
    if len(idades) > 0:
        media = sum(idades) / len(idades)
        print(f"A idade média desse grupo é: {media:.2f}")
    else:
        print("Nenhuma idade foi informada")
"""
# 44. Leia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior
# ao número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34.
"""
num = int(input("Digite um número positivo: "))

fibonacci = [0, 1]

while fibonacci[-1] <= num:
    next_num = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(next_num)

fibonacci.pop()  # remove o último número que é maior que o número lido

print(fibonacci)
"""
# 45. Faça um algoritmo que converta uma velocidade expressa em km/h para m/s e vice-versa
# Você deve criar um menu com as duas opções de conversão e com uma opção para finalizar o programa.
# O usuário poderá fazer quantas conversões desejar, sendo que o programa só será finalizado quando a opção de finalizar
# for escolhida.
"""
while True:
    print("Escolha uma opção:")
    print("1 - Converter km/h para m/s")
    print("2 - Converter m/s para km/h")
    print("0 - Finalizar o programa")
    opcao = input("Opção escolhida: ")

    if opcao == "1":
        kmh = float(input("Digite a velocidade em km/h: "))
        ms = kmh / 3.6
        print(f"{kmh} km/h equivalem a {ms:.2f} m/s\n")
    elif opcao == "2":
        ms = float(input("Digite a velocidade em m/s: "))
        kmh = ms * 3.6
        print(f"{ms} m/s equivalem a {kmh:.2f} km/h\n")
    elif opcao == "0":
        print("Programa finalizado!!")
        break
    else:
        print("Opção inválida.\nEscolha entre 0 - 2.\n")
"""
# 46. Faça um programa que gera um número aleatório de 1 a 1000. O usuário deve tentar acertar qual o número foi gerado,
# a cada tentativa o programa deverá informar se o chute é menor ou maior que o número gerado. O programa acaba quando
# o usuário acerta o número gerado. O programa deve informar em quantas tentativas o número foi descoberto.
"""
import random

tentativas = 0
num = random.randint(1, 1000)

print("Tente adivinhar o número entre 1 e 1000.\n")

while True:
    tentativa = int(input("Digite um número: "))
    tentativas += 1
    if tentativa < num:
        print("O chute é menor que o valor gerado!\n")
    elif tentativa > num:
        print("O chute é maior que o número gerado!\n")
    elif tentativa == num:
        print(f"Parabéns!, você acertou o número gerado, o número era: {num}\n")
        print(f"Você acertou em {tentativas} tentativas!")
        break
"""
# 47. Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
# • adição (opção 1)
# • subtração (opção 2)
# • multiplicação (opção 3)
# • divisão (opção 4).
# • saída (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a exitiçáo do resultado e a volta
# ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).
"""
print("Bem vindo usuário, escolha uma operação matemática a baixo!\n")
resultado = 0
while True:
    print("Escolha uma opção:")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair do Programa")
    opcao = int(input("Opção escolhida: "))

    if opcao == 1:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(resultado, '\n')
    elif opcao == 2:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(resultado, '\n')
    elif opcao == 3:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(resultado, '\n')
    elif opcao == 4:
        num1 = int(input("\nDigite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        resultado = num1 / num2
        print(resultado, '\n')
    elif opcao == 5:
        print("Programa encerrado!")
        break
    else:
        print("\nEscolha uma opção de 1 a 5")
"""
# 48. Faça um programa que some os termos de valor par da sequência de Fibonacci, cujos valores não
# ultrapassem quatro milhões.
"""
# Inicializa os valores iniciais da sequência de Fibonacci
a, b = 1, 2
result = 0

while a <= 4000000:  # Calcula os termos da sequência até 4 milhões
    if a % 2 == 0:
        result += a
    a, b = b, a + b
print(result)
"""
# 49. O funcionário Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário.
# Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela,
# pois está rendendo 2% ao mês. Joa aplicará seu salário integralmente, no fundo, de renda fixa, que está rendendo 5%
# ao mês. Construa um programa que deverá calcular e mostrar a quantidade de meses
# necessários para que o valor pertencente a João iguale ou ultrapasse o valor pertencente
# a Carlos. Teste com outros valores para as taxas.
"""
salario_carlos = 3000
salario_joao = salario_carlos / 3  # o salário de João é um terço do salário de Carlos
taxa_poupanca = 0.02  # 2% ao mês
taxa_renda_fixa = 0.05  # 5% ao mês
valor_carlos = salario_carlos
valor_joao = salario_joao
meses = 0

while valor_joao < valor_carlos:  # Aplica a taxa de rendimento na poupança e, no fundo, de renda fixa
    valor_carlos += valor_carlos * taxa_poupanca
    valor_joao += valor_joao * taxa_renda_fixa
    meses += 1
print(
    f"Serão necessários {meses} meses para que o valor pertencente a João iguale ou ultrapasse o valor"
    f" pertencente a Carlos.")
"""
# 50. Chico tem 1,50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1,10 metros e cresce 3 centímetros por ano.
# Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico.
"""
anos = 0
altura_chico = 1.50
altura_ze = 1.10

while altura_ze <= altura_chico:
    altura_chico += 0.02
    altura_ze += 0.03
    anos += 1

print(f"Serão necessários {anos} anos para que Zé fique maior que Chico!")
"""
# 51. Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000 reais. Em 1996 recebeu aumento de 1.5%.
# A partir de 1997, os aumentos sempre correspondem ao dobro do ano anterior.
# Faça programa que determine o salário atual do funcionário.
"""
salario = 2000
aumento = 0.015  # 1.5%
ano = 1996

while ano <= 2023:
  salario += (1 + aumento)
  aumento *= 2
  ano += 1
print(f"Salário atual do funcionário: R${salario:.2f}")
"""
# 52. Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um banco e retorne
# quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível.
# Serão utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.
"""
saque = int(input("Digite o valor do saque (Apenas valores inteiros): "))

notas = [100, 50, 20, 10, 5, 2, 1]
quantidades = [0, 0, 0, 0, 0, 0, 0]

for i in range(len(notas)):
    while saque >= notas[i]:
        saque -= notas[i]
        quantidades[i] += 1

print("Quantidade de notas a receber ->")
for i in range(len(notas)):
    if quantidades[i] > 0:
        print(f"Notas de {notas[i]}: {quantidades[i]}")
"""
# 53. Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado Triangulo de Floyd.
# Para n = 6, temos
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
"""
n = int(input('Digite o número de linhas: '))

m = 1
for c in range(1, n + 1):
    for i in range(1, c + 1):
        print(f'{m:<4}', end='')
        m += 1
    print()
"""
# 54. Faça um programa que receba um número inteiro maior do que 1, e verifique se o número fornecido é primo ou não.
"""
num = int(input("Digite o número para saber se é primo: "))
primo = True

for i in range(1, num + 1):
  if num % i == 0:
    primo = False
    break

if primo:
  print(f"{num} é um número primo")
else:
  print(f"{num} não é um número primo")
"""
# 55. Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros números primos.
"""
n = int(input("Digite um número inteiro não negativo: "))
soma = 0
cont_primos = 0

# itera pelos números de 2 até o infinito
i = 2
while cont_primos < n:
    # verifica se i é primo
    eh_primo = True
    for j in range(2, i):
        if i % j == 0:
            eh_primo = False
            break
    if eh_primo:  # se i for primo, adiciona à soma e incrementa o contador de primos
        soma += i
        cont_primos += 1
    i += 1
print(f"A soma dos {n} primeiros números primos é {soma}.")
"""
# 56. Faça um programa que calcule a soma de todos os números primos abaixo de dois milhões.
"""
soma = 0
cont_primos = 0

i = 2
while cont_primos <= 2000000:
  eh_primo = True
  for j in range(2, i):
    if i % j == 0:
      eh_primo = False
      break
  if eh_primo:
    soma += i
    cont_primos += 1
  i += 1
print(
  f"A soma de todos os primeiros números primos abaixo de 2.000.000 é {soma}.")
"""
# 57. Faça um programa que conte quantos números primos existem entre a e b, onde a e b são números informados pelo usuário.
"""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

count = 0

for num in range(a, b+1):
    if num > 1:
        eh_primo = True
        for i in range(2, num):
            if (num % i) == 0:
                eh_primo = False
                break
        if eh_primo:
            count += 1

print(f"Existem {count} números primos entre {a} e {b}")
"""
# 58. Faça um programa que some os números primos existentes entre a e b, onde a e b são números informados pelo usuário.
"""
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = 0
for num in range(a, b+1):
    if num > 1:
        primo = True
        for i in range(2, num):
            if (num % i) == 0:
                primo = False
                break
        if primo:
          soma += num

print(f"A soma de todos os números primos entre {a} e {b} é {soma}.")
"""
# 59. Escreva um programa que leia o número de habitantes de uma determinada cidade, o valor do kwh, e para cada habitante
# entre com os seguintes dados: consumo do mês e o código do consumidor (1 -Residencial, 2-Comercial, 3-lndustrial).
# No final imprima o maior, o menor e a média do consumo dos habitantes; e por fim o total do consumo de cada categoria de consumidor.
"""
num_habitantes = int(input("Digite o número de habitantes da cidade: "))
valor_kwh = float(input("Digite o valor do kwh: "))

maior_consumo = menor_consumo = media_consumo = 0
total_residencial = total_comercial = total_industrial = 0

for i in range(num_habitantes):
    consumo = float(input(f"Digite o consumo do habitante {i+1}: "))
    codigo = int(input(f"Digite o código do consumidor do habitante {i+1} \n(1- Residencial, 2- Comercial, 3- Industrial): "))
    
    media_consumo += consumo
    if i == 0 or consumo > maior_consumo:
        maior_consumo = consumo
    if i == 0 or consumo < menor_consumo:
        menor_consumo = consumo
    
    # adiciona o consumo atual ao total da categoria do consumidor
    if codigo == 1:
        total_residencial += consumo
    elif codigo == 2:
        total_comercial += consumo
    elif codigo == 3:
        total_industrial += consumo

media_consumo /= num_habitantes

print(f"Maior consumo: {maior_consumo}")
print(f"Menor consumo: {menor_consumo}")
print(f"Média do consumo: {media_consumo}")
print(f"Total do consumo residencial: {total_residencial}")
print(f"Total do consumo comercial: {total_comercial}")
print(f"Total do consumo industrial: {total_industrial}")
"""
# 60. Faça um programa que leia vários números, calcule e mostre:
# (a) A soma dos números digitados
# (b) A quantidade de números digitados
# (c) A média dos números digitados
# (d) O maior número digitado
# (e) O menor número digitado
# (f) A média dos números pares
# Finalize a entrada de dados caso o usuário informe o valor 0.
"""
numeros = []
num = int(input("Bem vindo usuário\n\nDigite um número (digite 0 para sair): "))
while num != 0:
    numeros.append(num)
    num = int(input("Digite outro número (digite 0 para sair): "))

soma = sum(numeros)
quantidade = len(numeros)
media = soma/quantidade
maior = max(numeros)
menor = min(numeros)
media_pares = sum([num for num in numeros if num % 2 == 0])/len([num for num in numeros if num % 2 == 0])

print(f"\nA soma dos números digitados é {soma}")
print(f"A quantidade de números digitados é {quantidade}")
print(f"A média dos números digitados é {media}")
print(f"O maior número digitado é {maior}")
print(f"O menor número digitado é {menor}")
print(f"A média dos números pares é {media_pares}")
"""
# 61. Faça um programa que calcule o maior número palíndromo feito a partir do produto de 
# dois números de 3 dígitos. Ex: O maior palíndromo feito a partir do produto de dois números de dois dígitos é 9009 = 91*99.
"""
maior_palindromo = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        produto = i * j
      # [::-1] Serve para ler uma string de trás para frente
        if str(produto) == str(produto)[::-1] and produto > maior_palindromo:
            maior_palindromo = produto
            fator1 = i
            fator2 = j

print(f"O maior palíndromo feito a partir do produto de dois números de três dígitos é: {maior_palindromo} = {fator1} * {fator2}")
"""
# 62. Se os números de 1 a 5 são escritos em palavras: um, dois, três, quatro e cinco, então há 2 + 4 + 4 + 6 + 5 = 22
# letras usadas no total. Faça um programa que conte quantas letras seriam utilizadas se todos os números de 1 a 1000
# (mil) fossem escritos em palavras. OBS: Não conte espaços ou hifens.
numeros = {
    1: 'um',
    2: 'dois',
    3: 'três',
    4: 'quatro',
    5: 'cinco',
    6: 'seis',
    7: 'sete',
    8: 'oito',
    9: 'nove',
    10: 'dez',
    11: 'onze',
    12: 'doze',
    13: 'treze',
    14: 'quatorze',
    15: 'quinze',
    16: 'dezesseis',
    17: 'dezessete',
    18: 'dezoito',
    19: 'dezenove',
    20: 'vinte',
    30: 'trinta',
    40: 'quarenta',
    50: 'cinquenta',
    60: 'sessenta',
    70: 'setenta',
    80: 'oitenta',
    90: 'noventa',
    100: 'cem',
    200: 'duzentos',
    300: 'trezentos',
    400: 'quatrocentos',
    500: 'quinhentos',
    600: 'seiscentos',
    700: 'setecentos',
    800: 'oitocentos',
    900: 'novecentos',
    1000: 'mil'
}

palavras = []

for i in range(1, 1001):
    if i in numeros:
        palavras.append(numeros[i])
    else:
        centena = i // 100 * 100
        dezena = i % 100 // 10 * 10
        unidade = i % 10
        palavra = ''
      
        if centena > 0:
            palavra += numeros[centena]
            if dezena > 0 or unidade > 0:
                palavra += 'e'
        if dezena > 0:
            if dezena == 10 and unidade > 0:
                palavra += numeros[dezena + unidade]
            else:
                palavra += numeros[dezena]
        if unidade > 0 and dezena != 10:
            if dezena > 0:
                palavra += 'e'
            palavra += numeros[unidade]

        palavras.append(palavra)

total_letras = sum(len(p.replace(' ', '').replace('-', '')) for p in palavras)

print(f'O total de letras utilizadas é {total_letras}.')
