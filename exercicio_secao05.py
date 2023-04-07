"""
Exercícios da Seção 5 do curso de Python da Geek University na Udemy

Exercícios básicos de Estuturas Lógicas e Condicionais - if, else e elif
"""
# 1. Faça um programa que receba dois números e mostre qual deles é o maior.
"""
numero_1 = int(input("Insira o primeiro número: "))
numero_2 = int(input("Insira o segundo número: "))

if numero_1 > numero_2:
    maior = numero_1
else:
    maior = numero_2
print(f"O maior número é: {maior}")
"""
# 2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
# Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
import math

numero = float(input("Insira um número: "))

if numero >= 0:
    raiz = math.sqrt(numero)  # Faz a raiz quadrada
    print(f"A raiz quadrada de {numero} é: {raiz:.2f}")
else:
    print(f"O número {numero} é inválido.")
"""
# 3. Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o número ao quadrado.
"""
import math

numero = float(input("Insira um número: "))

if numero >= 0:
    raiz = math.sqrt(numero)  # Faz a raiz quadrada
    print(f"A raiz quadrada de {numero} é: {raiz:.2f}")
else:
    quadrado = numero ** 2
    print(f"O número {numero} ao quadrado é: {quadrado}")
"""
# 4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
# • O número digitado ao quadrado • A raiz quadrada do número digitado
"""
import math

numero = float(input("Insira um número: "))

if numero >= 0:
    quadrado = numero ** 2
    raiz = math.sqrt(numero)  # Faz a raiz quadrada
    print(f"A raiz quadrada de {numero} é: {raiz:.2f}")
    print(f"O número {numero} ao quadrado é: {quadrado}")
"""
# 5. Faça um programa que receba um número inteiro e verifique se este número é par ou ímpar.
"""
numero = int(input("Insira um número inteiro: "))

if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é impar")
"""
# 6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
# assim como a diferença existente entre ambos.
"""
numero_1 = int(input("Insira um número inteiro: "))
numero_2 = int(input("Insira outro número inteiro: "))

if numero_1 > numero_2:
    maior = numero_1
    diferenca = numero_1 - numero_2
else:
    maior = numero_2
    diferenca = numero_2 - numero_1

print(f"O maior número é: {maior}")
print(f"A diferença entre eles é: {diferenca}")
"""
# 7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais,
# imprima a mensagem "Números iguais."
"""
numero_1 = int(input("Insira um número: "))
numero_2 = int(input("Insira outro número: "))

if numero_1 > numero_2:
    maior = numero_1
    print(f"O maior número é: {maior}")
elif numero_1 == numero_2:
    print(f"Os número são iguais!")
else:
    maior = numero_2
    print(f"O maior número é: {maior}")
"""
# 8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média
# destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua
# um valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
nota_1 = float(input("Insira a primeira nota: "))
nota_2 = float(input("Insira a segunda nota: "))

if nota_1 < 0.0 or nota_1 > 10.0:
    print("Insira um valor entre 0.0 e 10.0")
elif nota_2 < 0.0 or nota_2 > 10.0:
    print("Insira um valor entre 0.0 e 10.0")
else:
    media = (nota_1 + nota_2) / 2
    print(f"A média das notas é: {media}")
"""
# 9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20%
# do salário imprima: Empréstimo não concedido, caso contrário imprima: "Empréstimo concedido."
"""
salario = float(input("Insira o seu salário: "))
prestacao = float(input("Insira o valor da prestação do empréstimo: "))

limite = salario * 0.2

if prestacao > limite:
    print("Empréstimo não concedido.")
else:
    print("Empréstimo concedido.")
"""
# 10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando
# as seguintes fórmulas (onde h corresponde à altura): Homens: (72.7* h) -58 • Mulheres: (62, 1 * h) — 44, 7
"""
sexo = input("Insira seu sexo (Homem ou Mulher): ")
altura = float(input("Insira a sua altura: "))

if sexo == "Homem":
    peso_ideal = (72.7 * altura) - 58
    print(f"O seu peso ideal é: {peso_ideal:.2f}")
elif sexo == "Mulher":
    peso_ideal = (62.1 * altura) - 44.7
    print(f"O seu peso ideal é: {peso_ideal:.2f}")
else:
    print('Escreva "Homem" ou "Mulher" exatamente desse jeito')
"""
# 11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
# soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá 0 valor
# 8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
"""
numero = int(input("Insira um número maior que 0: "))

if numero <= 0:
    print("Número Inválido")
else:
    soma = 0
    for algarismo in str(numero):
        soma += int(algarismo)
    print(f"A soma dos algarismos do número {numero} é {soma}.")
"""
# 12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido".
# Se o número for positivo, calcular o logaritmo deste numero.
"""
import math

numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Numero inválido")
else:
    logaritmo = math.log10(numero)
    print(f"O logaritmo de {numero} é {logaritmo}")
"""
# 13. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1
# e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado.
# A nota para aprovação deve ser igual ou superior a 60 pontos.
"""
nota_1 = float(input("Digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))
nota_3 = float(input("Digite a terceira nota: "))

media = (nota_1 * 1 + nota_2 * 1 + nota_3 * 2) / 3

if media >= 60:
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

print(f"A média ponderada do aluno é: {media:.2f}")
print(f"O aluno foi: {situacao}")
"""
# 14. A nota final de um estudante é calculada a partir três notas atribuídas entre o intervalo de O até 10,
# respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas
# mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2, Avaliação Semestral: 3, Exame Final: 5.
# De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre O e 2,9), de recuperação
# (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""
nota_1 = float(input("Digite a nota do Trabalho: "))
nota_2 = float(input("Digite a nota da Avaliação: "))
nota_3 = float(input("Digite a nota do Exame: "))

media = (nota_1 * 2 + nota_2 * 3 + nota_3 * 5) / 10

if media < 3.0:
    situacao = "Reprovado"
if media < 5.0:
    situacao = "De Recuperação"
else:
    situacao = "Aprovado"

print(f"A média ponderada do aluno é: {media:.2f}")
print(f"O aluno foi: {situacao}")
"""
# 15. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a
# este número. Isto é, domingo se I, segunda-feira se 2, e assim por diante.
"""
dia = int(input("Digite um número entre 1 e 7: "))

switch = {
    1: "Segunda-Feira",
    2: "Terça-Feira",
    3: "Quarta-Feira",
    4: "Quinta-Feira",
    5: "Sexta-Feira",
    6: "Sábado",
    7: "Domingo"
}

print(f"O dia correspondente ao número digitado é: {switch.get(dia, 'Inválido')}")
"""
# 16. Usando switch, escreva um programa que leia um inteiro entre I e 12 e imprima o mês correspondente a este número.
# Isto é, janeiro se 1, fevereiro se 2, e assim por dante.
"""
mes = int(input("Digite um número entre 1 e 12: "))

switch = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

print(f"O mês correspondente ao número digitado é: {switch.get(mes, 'Inválido')}")
"""
# 17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que: A = (basemaior + basemenor) * altura /2
# Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
base_maior = float(input("Insira o valor da Base Maior (Maior que zero): "))

base_menor = float(input("Insira o valor da Base Menor (Maior que zero): "))

altura = float(input("Insira o valor da Altura (Maior que zero): "))

if base_maior > 0 and base_menor > 0:
    area = (base_maior + base_menor) * altura / 2
    print(f"O valor da área é: {area}")
else:
    print("Insira um valor maior que 0")
"""
# 18. Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas (as básicas, por exemplo).
# O usuário escolhe uma das opções e 0 seu programa então pede dois valores numéricos e realiza a operação, mostrando o
# resultado e saindo.
"""
print("Selecione a operação matemática:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite a opção desejada (1/2/3/4): "))

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if opcao == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif opcao == 2:
    resultado = num1 - num2
    print(f"{num1} - {num2} = {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"{num1} * {num2} = {resultado}")
elif opcao == 4:
    resultado = num1 / num2
    print(f"{num1} / {num2} = {resultado}")
else:
    print("Opção inválida")
"""
# 19. Faça um programa para verificar se um determinado número inteiro e divisível por 3 ou 5, mas não simultaneamente
# pelos dois.
"""
numero = int(input("Digite um número inteiro: "))

if numero % 3 == 0 and numero % 5 == 0:
    print("O número é divisível por 3 e 5 simultaneamente.")
elif numero % 3 == 0:
    print("O número é divisível por 3.")
elif numero % 5 == 0:
    print("O número é divisível por 5.")
else:
    print("O número não é divisível por 3 nem por 5.")
"""
# 20. Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem, se é um
# triângulo escaleno, equilátero ou isóscele, considerando os seguin três conceitos:
# • O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
# • Chama-se equilátero o triângulo que tem três lados iguais.
# Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
# Recebe o nome de escaleno o triângulo que tem os três diferentes.
"""
a = float(input("Insira o valor do lado a: "))
b = float(input("Insira o valor do lado b: "))
c = float(input("Insira o valor do lado c: "))

# Verifica se é um triângulo
if a < b + c and b < a + c and c < a + b:
    # Verifica o tipo de triângulo
    if a == b == c:
        print("Triângulo equilátero.")
    elif a == b or a == c or b == c:
        print("Triângulo isósceles.")
    else:
        print("Triângulo escaleno.")
else:
    print("Não é possível formar um triângulo com os valores informados.")
"""
# 21. Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
# Escreva uma mensagem de erro se a opção for inválida. Escolha a opção:
# 1— Soma de 2 números.
# 2- Diferença entre 2 números (maior pelo menor).
# 3— Produto entre 2 números.
# 4- Divisão entre 2 números (o denominador não pode ser zero).
"""
print("Selecione a operação matemática:")
print("1 - Soma de 2 números")
print("2 - Diferença entre 2 números")
print("3 - Produto entre 2 números")
print("4 - Divisão entre 2 números")

opcao = int(input("Digite a opção desejada (1/2/3/4): "))

num1 = float(input("Digite o primeiro valor: "))
num2 = float(input("Digite o segundo valor: "))

if opcao == 1:
    resultado = num1 + num2
    print(f"{num1} + {num2} = {resultado}")
elif opcao == 2:
    if num1 >= num2:
        resultado = num1 - num2
    else:
        resultado = num2 - num1
    print(f"A diferença entre {num1} e {num2} = {resultado}")
elif opcao == 3:
    resultado = num1 * num2
    print(f"O produto entre {num1} e {num2} = {resultado}")
elif opcao == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"{num1} / {num2} = {resultado}")
    else:
        print("Erro: não é possível dividir por 0")
else:
    print("Opção inválida")
"""
# 22. Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
# As condições para aposentadoria são
# • Ter pelo menos 65 anos,
# • Ou ter trabalhado pelo menos 30 anos,
# • Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.
"""
idade = int(input("Digite a sua idade: "))
tempo_servico = float(input("Digite o tempo de serviço: "))

if idade >= 65:
    print("O senhor tem direito a aposentadoria por conta da idade")
elif tempo_servico >= 30:
    print("O senhor tem direito a aposentadoria por conta do Tempo de Serviço")
elif idade >= 60 and tempo_servico >= 25:
    print("O senhor tem direito a aposentadoria por conta da Idade e Tempo de Serviço")
else:
    print("Você não tem direito a aposentadoria por não cumprir a idade mínima ou tempo de serviço mínimo")
"""
# 23. Determine se um ano lido é bissexto. Sendo que um ano é bissexto se for divisível por 400 ou se for
# divisível por 4 e não for divisível por 100. Por exemplo: 1988, 1992, 1996
"""
ano = int(input("Digite o ano: "))

if ano % 400 == 0 or (ano % 4 == 0 and ano % 100 != 0):
    print(ano, "é bissexto")
else:
    print(ano, "não é bissexto")
"""
# 24. Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente de
# imposto sobre o produto (MG 7%' SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com o valor e
# o estado destino do produto e o programa retorne o preço final do produto acrescido do imposto do estado em que ele
# será vendido. Se o estado digitado não for válido, mostrar uma mensagem de erro.
"""
taxas = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

valor = float(input("Digite o valor do produto: "))
estado = input("Digite o estado de destino do produto (MG, SP, RJ ou MS): ")

if estado not in taxas:
    print("Estado inválido. Digite MG, SP, RJ ou MS.")
else:
    # Cálculo do preço final com o acréscimo do imposto
    preco_final = valor * (1 + taxas[estado])
    print(f"O preço final do produto é R${preco_final:.2f}")
"""
# 25. Calcule as raízes da equação de 2º grau.
# Usando a fórmula certa para equação de 2º grau
# A variável A tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Não é equação de segundo grau".
# Se A < O, não existe real. Imprima a mensagem Não existe raiz.
# Se A = 0, existe uma raiz real. Imprima a raiz e a mensagem Raiz única.
# Se A ≥ 0, imprima as duas raízes reais.
"""
import math

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

# Verificar se é uma equação de 2º grau
if a == 0:
    print("Não é equação de segundo grau")
else:
    # Calcular o delta
    delta = b ** 2 - 4 * a * c
    # Verificar se existem raízes reais
    if delta < 0:
        print("Não existe raiz")
    elif delta == 0:
        # Calcular a raiz única
        raiz = -b / (2 * a)
        print(f"Raiz única: {raiz:.2f}")
    else:
        # Calcular as duas raízes reais
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"Raízes: {raiz1:.2f} e {raiz2:.2f}")
"""
# 26. Leia a distância em km e a quantidade de litros de gasolina consumidos por um carro em um percurso, calcule
# o consumo em km/l e escreva uma mensagem conforme a tabela:
"""
distancia = float(input("Insira a distância percorrida em Km: "))
combustivel = float(input("Insira o consumo de gasolina em Litros: "))

resultado = distancia / combustivel

if resultado < 8:
    print("Venda o carro!")
elif 8 < resultado < 14:
    print("Econômico")
elif resultado >= 12:
    print("Super Econômico")
else:
    print("Insira valores válidos")
"""
# 27. Escreva um programa que, dada a idade de um nadador, classifique-o em uma das seguintes categorias:
"""
idade = int(input("Insira a idade do nadador: "))

if 5 <= idade <= 7:
    print('O nadador é da categoria "Infantil A"')
elif 8 <= idade <= 10:
    print('O nadador é da categoria "Infantil B"')
elif 11 <= idade <= 13:
    print('O nadador é da categoria "Juvenil A"')
elif 14 <= idade <= 17:
    print('O nadador é da categoria "Juvenil B"')
elif idade >= 18:
    print('O nadador é da categoria "Sênior"')
else:
    print("A idade mínima é 5")
"""
# 28. Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das seguintes médias de
# acordo com um valor numérico digitado pelo usuário:
"""
import math

num1 = int(input("Insira o primeiro número inteiro: "))
num2 = int(input("Insira o segundo número inteiro: "))
num3 = int(input("Insira o terceiro número inteiro: "))

media = 0 

tipo_media = int(input("Digite 1 para média geométrica, 2 para média ponderada, "
                       "3 para média harmônica ou 4 para média aritmética: "))

if tipo_media == 1:
    # média geométrica: raiz cúbica do produto dos números
    media = math.pow(num1 * num2 * num3, 1 / 3)
elif tipo_media == 2:
    # média ponderada: soma dos produtos dos números pelos seus pesos, dividido pela soma dos pesos
    peso1 = int(input("Digite o peso do primeiro número: "))
    peso2 = int(input("Digite o peso do segundo número: "))
    peso3 = int(input("Digite o peso do terceiro número: "))
    media = (num1 * peso1 + num2 * peso2 + num3 * peso3) / (peso1 + peso2 + peso3)
elif tipo_media == 3:
    # média harmônica: inverso da média aritmética dos inversos dos números
    media = 3 / (1/num1 + 1/num2 + 1/num3)
elif tipo_media == 4:
    # média aritmética: soma dos números dividido por 3
    media = (num1 + num2 + num3) / 3
else:
    print("Tipo de média inválido")

print(f"A média calculada é: {media}")
"""
# 29. Faça uma prova de matemática para crianças que estão aprendendo a somar números inteiros menores do que 100.
# Escolha números aleatórios entre e 100, e mostre na tela a pergunta: qual é a soma de a + b, onde a e b são os
# números aleatórios. Peça a resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
# corretas, além de quantas vezes o aluno acertou.
"""
import random

acertos = 0

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    resposta = int(input(f"Qual é a soma de {a} + {b}? "))
    if resposta == a + b:
        print("Parabéns! Você acertou.")
        acertos += 1
    else:
        print(f"Ops, a resposta correta é {a + b}.")

print(f"Você acertou {acertos} de 5 perguntas.")
"""
# 30. Faça um programa que receba três números e mostre-os em ordem crescente.
"""
num_1 = float(input("Insira o primeiro número: "))
num_2 = float(input("Insira o segundo número: "))
num_3 = float(input("Insira o terceiro número: "))

numeros = [num_1, num_2, num_3]
ordem = sorted(numeros)

print(f"Os números em ordem crescente são: {ordem}")
"""
# 31. Faça um programa que receba a altura e o peso de uma pessoa. De acordo com a tabela a seguir, verifique e
# mostra qual a classificação dessa pessoa.
"""
altura = float(input("Insira a sua altura: "))
peso = float(input("Insira o seu peso: "))

if altura < 1.20:
  if peso < 60:
    print("Classificação: A")
  elif peso >= 60 and peso < 90:
    print("Classificação: D")
  elif peso >= 90:
    print("Classificação: G")
elif altura > 1.20 and altura < 1.70:
  if peso < 60:
    print("Classificação: B")
  elif peso >= 60 and peso < 90:
    print("Classificação: E")
  elif peso >= 90:
    print("Classificação: H")
elif altura >= 1.70:
  if peso < 60:
    print("Classificação: C")
  elif peso >= 60 and peso < 90:
    print("Classificação: F")
  elif peso >= 90:
    print("Classificação: I")
else:
  print("Insira um valor válido")
"""
# 32. Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
# O vograma deve calcular 0 valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado
# um pedido. O cardápio da lanchonete segue o padrão abaixo:
"""
cardapio = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.70, 105: 2.20, 106: 1.00}

codigo = int(input("Digite o código do produto: "))
quantidade = int(input("Digite a quantidade: "))
valor = cardapio[codigo] * quantidade

print(f"Total a pagar: R$ {valor:.2f}")
"""
# 33. Um produto vai sofrer aumento de acordo com a tabela abaixo. Leia o preço antigo, calcule e escreva o preço
# novo, e escreva uma mensagem em função do preço novo (deacordo com a segunda tabela).
"""
preco_antigo = float(input("Digite o preço antigo do produto: "))

if preco_antigo < 50:
  aumento = preco_antigo * 0.05
elif preco_antigo >= 50 and preco_antigo < 100:
  aumento = preco_antigo * 0.1
elif preco_antigo > 100:
  aumento = preco_antigo * 0.15

preco_novo = preco_antigo + aumento

if preco_novo < 80:
  print(f"O produto era {preco_antigo} e agora está por {preco_novo}, preço é: Barato")
elif preco_novo >= 80 and preco_novo < 120:
  print(f"O produto era {preco_antigo} e agora está por {preco_novo}, preço é: Normal")
elif preco_novo >= 120 and preco_novo <= 200:
  print(f"O produto era {preco_antigo} e agora está por {preco_novo}, preço é: Caro")
elif preco_novo > 200:
  print(f"O produto era {preco_antigo} e agora está por {preco_novo}, preço é: Muito Caro")
"""
# 34. Leia a nota e o número de faltas de um aluno, e escreva seu conceito. De acordo com a tabela abaixo,
# quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.
"""
nota = float(input("Digite a sua nota: "))
faltas = float(input("Digite as suas faltas: "))

if nota == 0 and nota <= 3.9:
  if faltas <= 20:
    print("O seu conceito final é: E")
  else:
    print("O seu conceito final é: E")
elif nota >= 4 and nota <= 4.9:
  if faltas <= 20:
    print("O seu conceito final é: D")
  else:
    print("O seu conceito final é: E")
elif nota >= 5 and nota <= 7.4:
  if faltas <= 20:
    print("O seu conceito final é: C")
  else:
    print("O seu conceito final é: D")
elif nota >= 7.5 and nota <= 8.9:
  if faltas <= 20:
    print("O seu conceito final é: B")
  else:
    print("O seu conceito final é: C")
elif nota >= 9 and nota <= 10:
  if faltas <= 20:
    print("O seu conceito final é: A")
  else:
    print("O seu conceito final é: B")
else:
  print("Digite um valor válido")
"""
# 35. Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12, e se o dia existe
# naquele mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 dias em anos não bissextos.
"""
data = input("Digite uma data no formato DD/MM/AAAA: ")

dia, mes, ano = data.split("/")

dia = int(dia)
mes = int(mes)
ano = int(ano)

if mes < 1 or mes > 12:
    print("Data inválida!")
  
elif dia < 1 or dia > 31:
    print("Data inválida!")
    
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
    if dia > 30:
        print("Data inválida!")

elif mes == 2:
    if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
        if dia > 29:
            print("Data inválida!")
    else:
        if dia > 28:
            print("Data inválida!")

else:
    print("Data válida!")
"""
# 36. Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser ao vendedor.
# Para calcular a comissão, considere a tabela abaixo:
"""
venda = float(input("Digite o valor da venda: "))

if venda >= 100000:
    comissao = 700 + 0.16 * venda
elif venda >= 80000:
    comissao = 650 + 0.14 * venda
elif venda >= 60000:
    comissao = 600 + 0.14 * venda
elif venda >= 40000:
    comissao = 550 + 0.14 * venda
elif venda >= 20000:
    comissao = 500 + 0.14 * venda
else:
    comissao = 400 + 0.14 * venda

print("A comissão a ser paga é de R${:.2f}".format(comissao))
"""
# 37. As tarifas de certo parque de estacionamento são as seguintes:
# • 1ª e 2ª hora- R$ 1,00 cada
# • 3ª e 4ª hora - R$ 1,40 cada
# • 5ª hora e seguintes - R$ 2,00 cada
# O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos
# pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque
# e partida deste são apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12
# 50 representará "dez para a uma da tarde". Pretende-se criar um programa que, lidos pelo teclado os momentos de
# chegada e de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se
# dão com intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não
# é uma situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.
"""
import math

# Leitura dos horários de chegada e partida
hora_chegada, min_chegada = map(
  int,
  input("Digite o horário de chegada (hh mm): ").split())
hora_partida, min_partida = map(
  int,
  input("Digite o horário de partida (hh mm): ").split())

# Cálculo das horas de estacionamento
horas_estacionamento = hora_partida - hora_chegada
if min_partida < min_chegada:
    horas_estacionamento -= 1
horas_estacionamento = max(horas_estacionamento, 1)

# Cálculo do valor a pagar
if horas_estacionamento <= 2:
    valor_pagar = horas_estacionamento
elif horas_estacionamento <= 4:
    valor_pagar = 2 + (horas_estacionamento - 2) * 1.4
else:
    valor_pagar = 4.8 + (horas_estacionamento - 4) * 2

# Arredondamento por excesso e exibição do valor a pagar
valor_pagar = math.ceil(valor_pagar)
print(f"O valor a pagar pelo estacionamento é: R${valor_pagar:.2f}")
"""
# 38. Leia uma data de nascimento de uma pessoa fornecida através de três números inteiros: Dia, Mês e Ano.
# Teste a validade desta data para saber se esta é uma data válida. Teste se o dia fornecido é um dia válido: dia > 0,
# dia 28 para o mês de fevereiro (29 se o ano for bissexto), dia 30 em abril, junho, setembro e novembro, dia 31
# nos outros meses. Teste a validade do mês: mês > 0 e mês < 13. Teste a validade do ano: ano < ano atual
# (use uma constante definida com o valor igual a 2008).
# Imprimir: "data válida" ou "data inválida" no final da execução do programa.
"""
import datetime

ano_atual = datetime.date.today().year
dia = int(input("Digite o dia de nascimento: "))
mes = int(input("Digite o mês de nascimento: "))
ano = int(input("Digite o ano de nascimento: "))

data_valida = True

if dia <= 0 or (dia > 28 and mes == 2 and not (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0))) \
        or (dia > 29 and mes == 2) or (dia > 30 and (mes == 4 or mes == 6 or mes == 9 or mes == 11)) or dia > 31:
    data_valida = False
elif mes <= 0 or mes > 12:
    data_valida = False
elif ano >= ano_atual or ano < 1900:
    data_valida = False

if data_valida:
    print("Data de nascimento válida!")
else:
    print("Data de nascimento inválida!")
"""
# 39. Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela que considera o salário atual
# e o tempo de serviço de cada funcionário. Os funcionários com menor salário terão um aumento proporcionalmente maior
# do que os funcionários com um salário maior, e conforme o tempo de serviço na empresa, cada funcionário irá receber
# um bônus adicional de salário. Faça um programa que leia:
# • o valor do salário atual do funcionário;
# • o tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa). Use as tabelas abaixo
# para calcular o salário reajustado deste funcionário e imprima o valor do salário final reajustado, ou uma mensagem
# caso o funcionário não tenha direito a nenhum aumento.
"""
salario_atual = float(input("Digite o salário atual do funcionário: "))
tempo_servico = int(input("Digite o tempo de serviço do funcionário (em anos): "))

if salario_atual <= 500:
    reajuste = 2.5
elif salario_atual <= 1000:
    reajuste = 2.0
elif salario_atual <= 1500:
    reajuste = 1.5
elif salario_atual <= 2000:
    reajuste = 0
else:
    reajuste = 0

if tempo_servico < 1:
    bonus = 0
elif tempo_servico <= 3:
    bonus = 100
elif tempo_servico <= 6:
    bonus = 200
elif tempo_servico <= 10:
    bonus = 300
else:
    bonus = 500

salario_reajustado = salario_atual * (1 + reajuste/100) + bonus

if reajuste == 0 and bonus == 0:
    print("O funcionário não tem direito a nenhum aumento.")
else:
    print(f"O salário final reajustado é de R${salario_reajustado:.2f}")
"""
# 40. O custo ao consumidor de um carro novo é a soma do custo de fábrica, da comissão do distribuidor, e dos impostos.
# A comissão e os impostos são calculados sobre o custo de fábrica, de acordo com a tabela abaixo. Leia o custo de
# fábrica e escreva o custo ao consumidor.
"""
custo_fabrica = float(input("Insira o custo de fábrica do carro: R$"))

if custo_fabrica <= 12000:
    distribuidor = custo_fabrica * 0.05
    impostos = 0
elif custo_fabrica <= 25000:
    distribuidor = custo_fabrica * 0.1
    impostos = custo_fabrica * 0.15
else:
    distribuidor = custo_fabrica * 0.15
    impostos = custo_fabrica * 0.2

custo_consumidor = custo_fabrica + distribuidor + impostos

print(f"O custo de consumidor do carro é: R${custo_consumidor:.2f}")
"""
# 41. Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação de acordo com a tabela abaixo:

altura = float(input("Insira a sua Altura: "))
peso = float(input("Insira o seu Peso: "))

imc = peso / (altura**2)

if not altura and not peso:
    print("Por favor, insira valores válidos para altura e peso")

if imc < 18.5:
    mensagem = "Você está magro!"
elif imc < 25:
    mensagem = "Você está com o peso normal!"
elif imc < 30:
    mensagem = "Cuidado você está com sobrepeso!"
elif imc < 35:
    mensagem = "Cuidado você está com Obesidade Grau I"
elif imc < 40:
    mensagem = "Cuidado você está com Obesidade Grau II"
else:
    mensagem = "Cuidado você está com Obesidade Grau III"

print(f"Seu IMC é: {imc:.2f}\n{mensagem}")
