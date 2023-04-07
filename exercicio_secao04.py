"""
Exercícios da Seção 4 do curso de Python da Geek University na Udemy

Exercícios básicos de lógica de programação em Python
"""
# 1) Faça um programa que leia um número inteiro e o imprima
"""
numero_inteiro = int(input('Insira um número: '))
print(numero_inteiro)
"""
# 2) Faça um programa que leia um número real e o imprima
"""
numero_real = float(input('Insira um número: '))
print(numero_real)
"""
# 3) Peça ao usuário digitar três valores inteiros e imprima a soma deles
"""
nome = input('Digite seu nome: ')

valor1 = int(input('Digite o 1º número inteiro: '))

valor2 = int(input('Digite o 2º número inteiro: '))

valor3 = int(input('Digite o 3º número inteiro: '))

resultado = valor1 + valor2 + valor3

print(f'{nome} a soma dos números inteiros é: {resultado}')
"""
# 4) Leia um número real e imprima o resultado do quadrado desse número
"""
numero = float(input('Insira um valor: '))
operacao = numero ** 2

print(f'Esse é o resultado ao quadrado: {operacao}')
"""
# 5) Leia um número real e imprima a quinta parte deste número
"""
numero = float(input('Insira um valor: '))
operacao = numero/5

print(f'Essa é a quinta parte desse número: {operacao}')
"""
# 6) Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
"""
temp_celsuis = float((input('Insira a temperatura: Cº')))
temp_fahrenheit = temp_celsuis * (9.0/5.0) + 32.0

print(f'A temperatura em Farenheit convertida é: Fº{temp_fahrenheit}')
"""
# 7) Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Fahrenheit.
"""
temp_fahrenheit = float(input('Insira a temperatura: Fº'))
temp_celsuis = 5.0 * (temp_fahrenheit - 32.0) / 9.0

print(f'A temperatura em Celsius convertida é: Cº{int(temp_celsuis)}')
"""
# 8) Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.
"""
temp_kelvin = float(input('Insira a temperatura: Kº'))
temp_celsuis = temp_kelvin - 273.15

print(f'A temperatura em graus Celsius convertida é: Cº{int(temp_celsuis)}')
"""
# 9) Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
"""
temp_celsius = int(input('Insira a temperatura: Cº'))
temp_kelvin = temp_celsius + 273.15

print(f'A temperatura em graus Celsius convertida é: Kº{temp_kelvin:.2f}')
"""
# 10) Leia uma velocidade em km/h e apresente-a convertida em m/s
"""
velocidade_km = float(input('Insira uma velocidade em km/h: '))
velocidade_ms = velocidade_km / 3.6

print(f'A velocidade convertida em m/s é: {velocidade_ms:.2f}')
"""
# 11) Leia uma velocidade em m/s e apresente-a convertida em km/h
"""
velocidade_ms = float(input('Insira uma velocidade em m/s: '))
velocidade_km = velocidade_ms * 3.6

print(f'A velocidade convertida em km/h é: {velocidade_km:.2f}')
"""
# 12) Leia uma distância em milhas e apresente-a convertida em quilômetros
"""
milhas = float(input('Insira um valor em Milhas: '))
quilometros = 1.61 * milhas

print(f'{milhas} convertida em quilômetros é: {quilometros}')
"""
# 13) Leia uma distância em milhas e apresente-a convertida em quilômetros
"""
quilometros = float(input('Insira um valor em Quilômetros: '))
milhas = quilometros / 1.61

print(f'{quilometros} convertida em quilômetros é: {milhas:.2f}')
"""
# 14) Leia um ângulo em graus e apresente-o convertido em radianos
"""
pi = 3.14
graus = float(input('Insira o valor de um ângulo em Graus: '))
radianos = graus * pi / 180

print(f'{graus} convertido em Radinos é: {radianos:.2f}')
"""
# 15) Leia um ângulo em radiano e apresente-o convertido em graus
"""
pi = 3.14
radianos = float(input('Insira o valor de um ângulo em Radianos: '))
graus = radianos * 180 / pi

print(f'{radianos} convertido em Graus é: {graus:.2f}')
"""
# 16) Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros
"""
polegadas = float(input("Digite um valor em polegadas: "))
centimetros = polegadas * 2.54

print(f"{polegadas} polegadas equivalem a {centimetros} centímetros.")
"""
# 17) Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas
"""
centimetros = float(input("Digite um valor em centímetros: "))
polegadas = centimetros / 2.54

print(f"{centimetros} centímetros equivalem a {polegadas:.2f} polegadas.")
"""
# 18) Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros
"""
cubicos = float(input('Digite um valor em m³ (Metros Cúbicos): '))
litros = 1000 * cubicos

print(f'{cubicos} m³ equivale a {litros} litros.')
"""
# 19) Leia um valor de volume em litros e apresente-o convertido em m³
"""
litros = float(input('Digite um valor em litros: '))
cubicos = litros / 1000

print(f'{litros} litros equivale a {cubicos} m³.')
"""
# 20) Leia um valor de massa em quilogramas e apresente-o convertido em libras
"""
quilogramas = float(input('Digite um valor em quilogramas: '))
libras = quilogramas / 0.45

print(f'{quilogramas} quilogramas equivale a {libras:.2f} libras.')
"""
# 21) Leia um valor de massa em quilogramas e apresente-o convertido em libras
"""
libras = float(input('Digite um valor em libras: '))
quilogramas = libras * 0.45

print(f'{libras} libras equivale a {int(quilogramas)} quilogramas.')
"""
# 22) Leia um valor de comprimento em jardas e apresente-o convertido em metros
"""
jardas = float(input('Digite um valor em jardas: '))
metros = 0.91 * jardas

print(f'{jardas} jardas equivale a {metros} metros.')
"""
# 23) Leia um valor de comprimento em metros e apresente-o convertido em jardas
"""
metros = float(input('Digite um valor em metros: '))
jardas = metros / 0.91

print(f'{metros} metros equivale a {jardas} jardas.')
"""
# 24. Leia um valor de área em metros quadrados m2 e apresente-o convertido em acres.
"""
metros = float(input('Digite um valor em metros quadrados: '))
acres = metros * 0.000247

print(f'{metros} metros quadrados equivale a {acres} acres.')
"""
# 25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m2.
"""
acres = float(input('Digite um valor em acres: '))
metros = acres * 4048.58

print(f'{acres} acres equivale a {metros} metros quadrados.')
"""
# 26. Leia um valor de área em metros quadrados m2 e apresente-o convertido em hectares.
"""
metros = float(input('Digite um valor em metros quadrados: '))
hectares = metros * 0.0001

print(f'{metros} metros quadrados equivale a {hectares} hectares.')
"""
# 27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2.
"""
hectares = float(input('Digite um valor em hectares: '))
metros = hectares * 10000

print(f'{hectares} hectares equivale a {metros} metros quadrados.')
"""
# 28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""
valor1 = float(input('Insira o primeiro valor: '))
valor2 = float(input('Insira o segundo valor: '))
valor3 = float(input('Insira o terceiro valor: '))

multiplica1 = valor1 ** 2
multiplica2 = valor2 ** 2
multiplica3 = valor3 ** 2

resultado = multiplica1 + multiplica2 + multiplica3

print(f'A soma dos quadrados dos três valores é: {resultado}')
"""
# 29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))
nota4 = float(input('Insira a quarta nota: '))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'A média aritmética das notas é: {media}')
"""
# 30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""
real = float(input("Digite o valor em reais: "))
cotacao = float(input("Digite a cotação do dólar: "))

dolar = real / cotacao

print(f'O valor correspondente em dólares é: {dolar:.2f}')
"""
# 31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
"""
num = int(input("Digite um número inteiro: "))
antecessor = num - 1
sucessor = num + 1

print(f"O antecessor de {num} é: {antecessor}, e o sucessor é: {sucessor}")
"""
# 32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""
num = int(input("Digite um número inteiro: "))
antecessor = (num * 2) - 1
sucessor = (num * 3) + 1
soma = antecessor + sucessor

print(f"A soma do sucessor de seu triplo com o antecessor de seu dobro é: {soma}")
"""
# 33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área.
"""
lado = float(input("Digite o tamanho do lado do quadrado: "))
area = lado ** 2

print(f"A área do quadrado é: {area}")
"""
# 34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente.
"""
pi = 3.141592
raio = float(input("Digite o valor do raio do Círculo: "))
area = pi * raio ** 2

print(f"O valor da Área é: {area}")
"""
# 35. Sejam A e B os catetos de um triângulo, onde a hipotenusa é obtida pela equação respectiva. Faça um programa
# que receba os valores de A e B e calcule o valor da hipotenusa atráves da equação. Imprima o resultado.
"""
a = float(input("Digite o valor do cateto A: "))
b = float(input("Digite o valor do cateto B: "))
hipotenusa = (a**2 + b**2)**0.5

print(f"A hipotenusa do triângulo é: {hipotenusa:.2f}")
"""
# 36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro.
# o volume de um cilindro circular é calculado por meio da seguinte fórmula: V = П * raio2 * altura
"""
pi = 3.141592
altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))
volume = pi * raio ** 2 * altura

print(f"O Volume do Cilíndro é: {volume}")
"""
# 37. Faça um programa que leia o valor de um produto e imprima o valor com desconto,
# tendo em vista que o desconto foi de 12%
"""
valor_real = float(input("Digite o valor real do produto: "))
desconto = valor_real * 0.12
valor_descontado = valor_real - desconto

print(f"O valor com desconto é: {valor_descontado}")
"""
# 38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário,
# sabendo que ele recebeu um aumento de 25%.
"""
salario = float(input("Digite o salário: "))
aumento = salario * 0.25
valor_aumentado = salario + aumento

print(f"O valor com aumento é: {valor_aumentado}")
"""
# 39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso sendo que
# da quantia total: O primeiro ganhador receberá 46%; O segundo receberá 32%; O terceiro receberá o restante;
# Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
premio_total = 780000.00
ganho_primeiro = premio_total * 0.46
ganho_segundo = premio_total * 0.32
ganho_terceiro = premio_total - ganho_primeiro - ganho_segundo

print(f"O primeiro ganhador receberá R$ {ganho_primeiro:.2f}")
print(f"O segundo ganhador receberá R$ {ganho_segundo:.2f}")
print(f"O terceiro ganhador receberá R$ {ganho_terceiro:.2f}")
"""
# 40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite o número
# de dias trabalhados pelo encanador e imprima a quantia liquida que devera ser paga, sabendo-se que são
# descontados 8% para imposto de renda.
"""
dia = 30
dias_trabalhados = int(input("Informe os dias trabalhados: "))

renda_liquida = 30 * dias_trabalhados - 0.8

print(f"A renda líquida é: {renda_liquida}")
"""
# 41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
# trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""
hora = float(input("Digite o valor da hora de trabalho em reais: "))
hora_mes = float(input("Insira o número de horas trabalhadas no mês: "))

renda = hora * hora_mes
adicional = renda * 0.1
salario = renda + adicional

print(f"O valor a ser pago com acréscimo de 10% é: {salario:.2f}")
"""
# 42. Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,
# sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
# ele paga 7% de imposto sobre o salário-base.
"""
salario_base = float(input("Digite o seu salário base: "))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07

salario_receber = salario_base + gratificacao - imposto

print(f"O salário que vai receber é: {salario_receber}")
"""
# 43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido,
# mostre: o total a pagar com desconto de 10%, o valor de cada parcela, no parcelamento em 3x sem juros;
# a comissão do vendedor, no caso da venda a ser vista (5% spbre o valor com desconto) a comissão do vendedor,
# no caso a venda parcelada (5% sobre o valor total)
"""
valor_venda = float(input("Digite o valor total da venda: "))

venda_descontada = valor_venda * 0.1 
print(f"\nTotal a pagar com desconto de 10%: R$ {venda_descontada:.2f}\n")

valor_parcela = valor_venda / 3
print(f"Valor de cada parcela (3x sem juros): R$ {valor_parcela:.2f}\n")

comissao_vista = venda_descontada * 0.05
print(f"Comissão do vendedor (venda à vista): R$ {comissao_vista:.2f}\n")

comissao_parcelada = valor_venda * 0.05
print(f"Comissão do vendedor (venda parcelada): R$ {comissao_parcelada:.2f}\n")
"""
# 44. Receba a altura do degrau de uma escada e a altura que o usuário deseja
# alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""
altura_degrau = float(input("Digite a altura do degrau da escada: "))
altura_meta = float(input("Digite a altura que deseja alcançar subindo a escada: "))

quantidade_degraus = int(altura_meta / altura_degrau)

print(f"Você precisará subir {quantidade_degraus} degraus para alcançar o objetivo.")
"""
# 45. Faça um programa para converter uma letra maiúscula em letra minúscula.
# Use a tabela ASCII para resolver o problema.
"""
letra_maiuscula = input("Digite uma letra maiúscula: ")
valor_ascii = ord(letra_maiuscula)
valor_ascii += 32  # Adiciona 32 para converter para a letra minúscula correspondente
letra_minuscula = chr(valor_ascii)
print(f"A letra minúscula correspondente é {letra_minuscula}")
"""
# 46. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
# Gere outro número formado pelos dígitos invertidos do número lido.
"""
num = int(input("Digite um número inteiro positivo de três dígitos: "))

digito_centena = num // 100  #Operador de divisão inteira
digito_dezena = (num % 100) // 10
digito_unidade = num % 10 # Operador de módulo para extrair
num_invertido = digito_unidade * 100 + digito_dezena * 10 + digito_centena

print("O número invertido é:", num_invertido)
"""
# 47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""
numero = input("Digite um número inteiro de 4 dígitos: ")

print(numero[0])
print(numero[1])
print(numero[2])
print(numero[3])
"""
# 48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
segundos = int(input("Digite um valor inteiro em segundos: "))
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas}h {minutos}min {segundos}s")
"""
# 49. Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração,
# em segundos, de uma experiência biológica. o programa deve resultar com o novo horário
# (hora, minuto e segundo) do termino da mesma.
"""
# Lê o horário de início
hora_inicio = int(input("Digite a hora de início (0-23): "))
minuto_inicio = int(input("Digite o minuto de início (0-59): "))
segundo_inicio = int(input("Digite o segundo de início (0-59): "))

# Lê a duração da experiência em segundos
duracao_segundos = int(input("Digite a duração da experiência em segundos: "))

# Converte o horário de início para segundos
total_segundos_inicio = hora_inicio * 3600 + minuto_inicio * 60 + segundo_inicio

# Calcula o horário de término em segundos
total_segundos_termino = total_segundos_inicio + duracao_segundos

# Converte o horário de término de segundos para horas, minutos e segundos
hora_termino = total_segundos_termino // 3600
minuto_termino = (total_segundos_termino % 3600) // 60
segundo_termino = total_segundos_termino % 60

# Exibe o horário de término na tela
print(f"O horário de término da experiência é: {hora_termino:02d}:{minuto_termino:02d}:{segundo_termino:02d}") 
# :02d = serve para formatar o valor em duas casas decimais com zero à esquerda, caso o valor seja menor que 10.
"""
# 50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.
"""
ano_atual = 2023
idade = int(input("Insira a sua idade: "))
data_nascimento = ano_atual - idade 

print(f"O seu ano de nascimento é: {data_nascimento}")
"""
# 51. Escreva um programa que leia as coordenadas x e y de pontos no R2 e calcule sua distância da origem (0,0).
"""
import math

x = float(input("Digite a coordenada x: "))
y = float(input("Digite a coordenada y: "))

#sqrt = Raiz Quadrada
distancia = math.sqrt(x**2 + y**2) # Fórmula d = √(x² + y²).

print(f"A distância da origem é: {distancia}")
"""
# 52. Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-porcionalmente
# ao valor que cada deu para a realização da aposta. Faça um programa que leia quanto cada apostador investiu,
# o valor do prêmio, e imprima quanto cada um ganharia do prêmio com base no valor investido.
"""
apostador1 = float(input("Digite o valor investido pelo primeiro apostador: "))
apostador2 = float(input("Digite o valor investido pelo segundo apostador: "))
apostador3 = float(input("Digite o valor investido pelo terceiro apostador: "))

valor_premio = float(input("Digite o valor total do prêmio: "))

total_apostado = apostador1 + apostador2 + apostador3

proporcao1 = apostador1 / total_apostado
proporcao2 = apostador2 / total_apostado
proporcao3 = apostador3 / total_apostado

premio_apostador1 = proporcao1 * valor_premio
premio_apostador2 = proporcao2 * valor_premio
premio_apostador3 = proporcao3 * valor_premio

print(f"O primeiro apostador ganhou: {premio_apostador1}")
print(f"O segundo apostador ganhou: {premio_apostador2}")
print(f"O terceiro apostador ganhou: {premio_apostador3}")
"""
# 53. Faça um programa para ler as dimensões de um terreno (comprimento с e largura l),
# bem como o preço do metro de tela р. Imprima o custo para cercar este mesmo terreno com tela.

comprimento = float(input("Digite o comprimento do terreno em metros: "))
largura = float(input("Digite a largura do terreno em metros: "))
preco_tela = float(input("Digite o preço por metro de tela em reais: "))

perimetro = 2 * (comprimento + largura)
custo_total = perimetro * preco_tela

print(
  f"O custo para cercar o terreno de {comprimento} m x {largura} m é de R${custo_total:.2f}."
)
