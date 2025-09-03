# ex001: Imprima Hello, World!
print("Hello, World!")


# ex002: Leia 2 valores inteiros e armazene-os nas variáveis A e B. Efetue a soma de A e B atribuindo o seu resultado na variável soma. Imprima soma.
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
soma = a + b

print(f'A soma entre {a} e {b} é {soma}')


# ex003: Leia 2 valores de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno. A seguir, calcule a média do aluno. Assuma que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

print(f'A média é de {media}')


# ex004: Leia 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno. A seguir, calcule a média do aluno. Considere que cada nota pode ir de 0 até 10.0, sempre com uma casa decimal.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1 + n2 + n3) / 3

print(f'A média é de {media}')


# ex005: Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))
d = int(input('Digite o quarto valor: '))

diferenca = (a * b - c * d)
print(diferenca)


# ex006: Faça um programa que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas para ela
nome = input('Digite o seu nome: ')
print(f'Prazer, {nome}!')


# ex007: Desenvolva um algoritmo que leia dois números inteiros e mostre o somatório entre eles.
x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))

soma = x + y
print(f'A soma entre os dois números é {soma}')


# ex008: Faça um programa que leia as duas notas de um aluno em uma matéria e mostre na tela a sua média na disciplina.
n1 = float(input('Digite a primeira nota do(a) aluno(a): '))
n2 = float(input('Digite a segunda nota do(a) aluno(a): '))

media = (n1 + n2) / 2
print(f'A média do aluno é {media}')


# ex009: Crie um algoritmo que leia um número real e mostre na tela o seu dobro e a sua terça parte.
numero = float(input('Digite um número real: '))

print(f'O dobro de seu número é {numero * 2}')
print(f'A terça parte do seu número é {numero / 3}')


# ex010: Desenvolva um programa que leia uma distância em metros e mostre os valores relativos em outras medidas.
metros = float(input('Digite uma distância em metros: '))
print(f'{metros / 1000}Km')
print(f'{metros / 100}Hm')
print(f'{metros / 10}Dam')
print(f'{metros * 10}dm')
print(f'{metros * 100}cm')
print(f'{metros * 1000}mm')


# ex011: Faça um algoritmo que leia quanto dinheiro uma pessoa tem na carteira (em R$) e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$6.
reais = int(input('Quantos reais você tem? '))
dolares = reais / 6

print(f'Você pode comprar {round(dolares, 2)} doláres.')


# ex012: Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2m².
largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))

area = largura * altura
tinta = area / 2

print(f'A área da parede é de {area}m²')
print(f'A tinta necessária é {tinta} litros de tinta')


# ex013: Crie um programa que leia o preço de um produto, calcule e mostre o seu PREÇO PROMOCIONAL, com 5% de desconto.
produto = float(input('Digite o preço do produto: '))
desconto = produto * 0.05
preco = produto - desconto

print(f'O preço do produto com um desconto de 5% é de {preco}')


# ex014: Faça um algoritmo que leia o salário de um funcionário, calcule e mostre o seu novo salário, com 15% de aumento.
salario = float(input('Digite o seu salário: '))
aumento = salario * 0.15
salario += aumento

print(f'O seu novo salário com 15% de aumento é {salario}')


# ex015: A locadora de carros precisa da sua ajuda para cobrar seus serviços. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço total a pagar, sabendo que o carro custa R$90 por dia e R$0,20 por Km rodado.
km = float(input('Digite a quantidade de Kms percorridos: '))
dias = int(input('Digite a quantidade de dias que o carro foi alugado: '))

total = 0
total += (dias * 90) + (km * 0.20)

print(f'O total a se pagar é {total}')


# ex016: Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25 por hora trabalhada.
dias = int(input('Quantos dias em um mês você trabalha? '))
horas = 8
lucro_hora = 25

salario = (lucro_hora * horas) * dias

print(f'O salário do funcionário é de {salario}')


# ex017: [DESAFIO] Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dias e quantos anos ele já fumou. Considere que um fumante perde 10 min de vida a cada cigarro. Calcule quantos dias de vida um fumante perderá e exiba o total em dias.
cigarros_dia = int(input('Quantos cigarros fuma por dia? '))
anos = int(input('Quantos anos fuma? '))

total_cigarros = cigarros_dia * 365 * anos
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 60 / 24

print(f'Dias perdidos: {dias_perdidos}')


# ex018: Leia 2 valores com uma casa decimal (x e y), que devem representar as coordenadas de um ponto em um plano. A seguir, determine qual o quadrante ao qual pertence o ponto, ou se está sobre um dos eixos cartesianos ou na origem (x = y = 0).
x = float(input("Qual a posição de x? "))
y = float(input("Qual a posição de y? "))

if x > 0 and y > 0:
    print('Q1')
elif x > 0 and y < 0:
    print('Q4')
elif x < 0 and y < 0:
    print('Q3')
elif x < 0 and y > 0:
    print('Q2')
else:
    print('Origem')


# ex019: Escreva um programa que pergunte a velocidade de um carro. Caso ultrapasse 80Km/h, exiba uma mensagem dizendo que o usuário foi multado. Nesse caso, exiba o valor da multa, cobrando R$5 por cada Km acima da velocidade permitida.
velocidade = int(input('Digite a velocidade do carro: '))
valor_multa = 0
if velocidade > 80:
    valor_multa = (velocidade - 80) * 5
    print(f'Sua multa é de R${valor_multa} reais por ultrapassar o limite estabelecido!')
else:
    print('Parabéns pela sua velocidade!')


# ex020: Crie um algoritmo que leia o nome e as duas notas de um aluno, calcule a sua média e mostre na tela. No final, analise a média e mostre se o aluno teve ou não um bom aproveitamento (se ficou acima da média 7.0).
nome = input('Digite o seu nome: ').strip().title()
n1 = float(input(f'{nome}, Digite a primeira nota: '))
n2 = float(input(f'{nome}, Digite a segunda nota: '))

media = (n1 + n2) / 2

if media > 7.0:
    print('Você está aprovado')
elif media > 5.0:
    print('Você está em recuperação')
else:
    print('Você está reprovado')


# ex021: Desenvolva um programa que leia um número inteiro e mostre se ele é PAR ou ÍMPAR.
numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print("Par")
else:
    print("Ímpar")


# ex022: Faça um algoritmo que leia um determinado ano e mostre se ele é ou não BISSEXTO. (formula básica)
ano = int(input('Digite um ano qualquer: '))

if ano % 4 == 0 and ano % 100 != 0:
    print('Ano é Bissexto')
else:
    print('Ano não é Bissexto')


# ex023: Faça um algoritmo que pergunte a distância que um passageiro deseja percorrer em Km. Calcule o preço da passagem, cobrando R$0.50 por Km para viagens até 200Km e R$0.45 para viagens mais longas.
distancia = int(input('Quantos Kms deseja percorrer? '))

if distancia < 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45

print(f'O preço final é de R${preco} reais')


# ex024: Desenvolva um programa que leia o nome de um funcionário, seu salário, quantos anos ele trabalha na empresa e mostre seu novo salário, reajustado de acordo com a tabela a seguir:
# - Até 3 anos de empresa: aumento de 3%
# - entre 3 e 10 anos: aumento de 12.5%
# - 10 anos ou mais: aumento de 20%
funcionario = input('Digite o nome do funcionário: ')
salario = int(input('Digite o salário do funcionário: '))
anos = int(input('Quantos anos trabalha na empresa? '))


if anos < 3:
    aumento = salario * 0.03
elif anos > 3 and anos < 10:
    aumento = salario * 12.5
elif anos >= 10:
    aumento = salario * 0.20
print(f'O novo salário de {funcionario} agora é de {salario + aumento}')


# ex025: O Índice de Massa Corpórea (IMC) é um valor calculado baseado na altura e no peso de uma pessoa. De acordo com o valor do IMC, podemos classificar o indivíduo dentro de certas faixas.
# - abaixo de 18.5: Abaixo do peso
# - entre 18.5 e 25: Peso ideal
# - entre 25 e 30: Sobrepeso
# - entre 30 e 40: Obesidade
# - acima de 40: Obseidade mórbida
# Obs: O IMC é calculado pela expressão peso/altura2 (peso dividido pelo quadrado da altura)

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura em cm: '))

IMC = peso / altura ** 2

print(f'Seu IMC é: {round(IMC, 4)}')

if IMC < 18.5:
    print("Abaixo do peso")
elif IMC < 25:
    print("Peso normal")
elif IMC < 30:
    print("Sobrepeso")
elif IMC < 40:
    print("Obesidade")
else:
    print('Obesidade mórbida')


# ex026: Uma empresa de aluguel de carros precisa cobrar pelos seus serviços. O aluguel de um carro custa R$90 por dia para carro popular e R$150 por dia para carro de luxo. Além disso, o cliente paga por Km percorrido. Faça um programa que leia o tipo de carro alugado (popular ou luxo), quantos dias de aluguel e quantos Km foram percorridos. No final mostre o preço a ser pago de acordo com a tabela a seguir:
# - Carros populares (aluguel de R$90 por dia)
# - Até 100Km percorridos: R$0,20 por Km
# - Acima de 100Km percorridos: R$0,10 por Km
# - Carros de luxo (aluguel de R$150 por dia)
# - Até 200Km percorridos: R$0,30 por Km
# - Acima de 200Km percorridos: R$0,25 por Km

carro = input('Qual o tipo de carro? [popular/luxo]: ').strip().lower()
dias = int(input('Quantos dias? '))
kms = float(input('Quantos kms percorridos? '))

if carro == 'popular':
    aluguel = dias * 90
    if kms > 100:
        aluguel += kms * 0.10
    else:
        aluguel += kms * 0.20
elif carro == 'luxo':
    aluguel = dias * 150 
    if kms > 200:
        aluguel += kms * 0.25
    else:
        aluguel += kms * 0.30
else:
    print('Carro não encontrado.')

print(f'O aluguel do carro está com o preço de R${aluguel:.2f}')


# ex027: Um programa de vida saudável quer dar pontos de atividades físicas que podem ser trocados por dinheiro. O sistema funciona assim:
# - Cada hora de atividade física no mês vale pontos
# - até 10h de atividade no mês: ganha 2 pontos por hora
# - de 10h até 20h de atividade no mês: ganha 5 pontos por hora
# - acima de 20h de atividade no mês: ganha 10 pontos por hora
# - A cada ponto ganho, o cliente fatura R$0,05 (5 centavos)
# Faça um programa que leia quantas horas de atividade uma pessoa teve por mês, calcule e mostre quantos pontos ela teve e quanto dinheiro ela conseguiu ganhar.

horas = int(input('Quantas horas de atividade você teve no mês? '))
pontos = 0

if horas <= 10:
    pontos = horas * 2
elif horas <= 20:
    pontos = 10 * 2 + (horas - 10) * 5
else:
    pontos = 10 * 2 + 10 * 5 + (horas - 20) * 10
    
dinheiro = pontos * 0.05

print(f'Parabéns! Você teve {pontos} pontos e obteve R${dinheiro} reais!')


# ex028: # Crie um programa que calcule e mostre na tela o resultado da soma entre 6 + 8 + 10 + 12 + 14 + ... + 98 + 100.
soma = 0
for i in range(6, 101, 2):
    soma += i
print(f'A soma dos números de 6 a 100 pulando em 2 em 2 é {soma}')


# ex029: # Desenvolva um aplicativo que mostre na tela o resultado da expressão 500 + 450 + 400 + 350 + 300 + ... + 50 + 0
soma = 0
for i in range(500, 0, -50):
    soma += i

print(f'O resultado da expressão é {soma}')


# ex030: Crie um algoritmo que leia o valor inicial da contagem, o valor final e o incremento, mostrando em seguida todos os valores no intervalo:
# Ex: Digite o primeiro Valor: 3
# Digite o último Valor: 10
# Digite o incremento: 2
# Contagem: 3 5 7 9 Acabou!
inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

for i in range(inicio, fim+1, passos):
    print(i)


# ex031: Faça um programa que leia 7 números inteiros e no final mostre o somatório entre eles.
soma = 0
for i in range(7):
    numero = int(input(f'Digite o número {i+1}: '))
    soma += numero

print(f'A soma dos números digitados foi {soma}')


# ex032: Crie um programa que tenha um procedimento Gerador() que, quando chamado, mostre a mensagem "Olá, Mundo!" com algum componente visual (linhas)
# Ex: Ao chamar Gerador() aparece:
# +-------=======------+
# Olá, Mundo!
# +-------=======------+

def Gerador():
    print('-' * 35)
    print('Olá Mundo!'.center(35, ' '))
    print('-' * 35)

Gerador()


# ex033: Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre uma mensagem personalizada, passada como parâmetro.
# Ex: Ao chamar Gerador("Aprendendo Python") aparece:
# +-------=======------+
# Aprendendo Python
# +-------=======------+

def Gerador(texto):
    print('-' * 40)
    print(texto.center(40, ' '))
    print('-' * 40)

Gerador('Aprendendo Python com Guanabara')
Gerador('Guanabara -> O melhor professor de tecnologia')


# ex034: A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159. Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π.
from math import pi

raio = float(input('Digite o valor do raio: '))
area = (raio ** 2) * pi

print(f'A área do círculo é {round(area, 4)}')


# ex035: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Somador() que vai calcular e mostrar a soma entre eles.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def soma(n1, n2):
    print(f'A soma é de {n1 + n2}')


soma(n1, n2)


# ex036: Faça um programa que leia a largura e o comprimento de um terreno retangular, calculando e mostrando a sua área em m2. O programa também deve mostrar a classificação desse terreno, de acordo com a lista abaixo:
# - Abaixo de 100m2 = TERRENO POPULAR
# - Entre 100m2 e 500m2 = TERRENO MASTER
# - Acima de 500m2 = TERRENO VIP

largura = float(input('Digite a largura do terreno: '))
comprimento = float(input('Digite o comprimento do terreno: '))

area = largura * comprimento

if area > 500:
    print('Terreno VIP')
elif area < 500 and area > 100:
    print('Terreno MASTER')
elif area < 100:
    print('Terreno POPULAR')


# ex037: Desenvolva um algoritmo que mostre uma contagem regressiva de 30 até 1, marcando os números que forem divisíveis por 4, exatamente como mostrado abaixo:
# 30 29 [28] 27 26 25 [24] 23 22 21 [20] 19 18 17 [16]...

i = 30
while i >= 0:
    if i % 4 == 0:
        print([i])
    else:
        print(i)
    i -= 1


# ex038: Faça um programa que possua uma função chamada Potencia(), que vai receber dois parâmetros numéricos (base e expoente) e vai calcular o resultado da exponenciação.
# Ex: Potencia(5,2) vai calcular 5² = 25

def Potencia(base, expoente):
    return base ** expoente

print(Potencia(5, 2))
print(Potencia(6, 5))
print(Potencia(8, 2))
print(Potencia(5, 3))


# ex039: Faça um programa que leia 5 valores inteiros. Conte quantos destes valores digitados são pares e mostre esta informação.
pares = 0
for i in range(5):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += 1

print(f'Ao total são {pares} números pares')


# ex040: Numa promoção exclusiva para o Dia da Mulher, uma loja quer dar descontos para todos, mas especialmente para mulheres. Faça um programa que leia nome, genero e o valor das compras do cliente e calcule o preço com desconto. Sabendo que:
# - Homens ganham 5% de desconto
# - Mulheres ganham 13% de desconto

nome = input('Digite o seu nome: ').strip().title()
genero = input(f'{nome}, Digite o seu genero [M/F]: ').strip().upper()
while genero not in ['M', 'F']:
    genero = input(f'{nome}, Digite corretamente [M/F]: ').strip().upper()
valor = float(input('Qual foi o valor das compras? '))

if genero == 'M':
    desconto = valor * 0.05
    preco = valor - desconto
    print(f'Como você é homem, o preço final da compra com desconto será de R${preco} reais')
elif genero == 'F':
    desconto = valor * 0.13
    preco = valor - desconto
    print(f'Como você é mulher terá um super desconto de 13%, então sua compra agora custa R${preco} reais!')


# ex041: Uma empresa precisa reajustar o salário dos seus funcionários, dando um aumento de acordo com alguns fatores. Faça um programa que leia o salário atual, o gênero do funcionário e há quantos anos esse funcionário trabalha na empresa. No final, mostre o seu novo salário, baseado na tabela a seguir:
# - Mulheres
# - menos de 15 anos de empresa: +5%
# - de 15 até 20 anos de empresa: +12%
# - mais de 20 anos de empresa: +23%
# - Homens
# - menos de 20 anos de empresa: +3%
# - de 20 até 30 anos de empresa: +13%
# - mais de 30 anos de empresa: +25%

salario = float(input('Digite o salário: '))
genero = input('Digite o gênero [M/F]: ').strip().upper()

while genero not in ['M', 'F']:
    genero = input('Digite corretamente [M/F]: ').strip().upper()

anos = int(input('Quantos anos trabalha na empresa? '))

if genero == 'F':
    if anos < 15:
        aumento = salario * 0.05
    elif anos >= 15 and anos < 20:
        aumento = salario * 0.12
    elif anos >= 20:
        aumento = salario * 0.23
elif genero == 'M':
    if anos < 20:
        aumento = salario * 0.03
    elif anos >= 20 and anos < 30:
        aumento = salario * 0.13
    elif anos >= 30:
        aumento = salario * 0.25
salario += aumento

print(f'Seu novo salário reajustado é de R${salario} reais')


# ex042: O exercicio 79 vai ter um problema quando digitarmos o primeiro valor maior que o último. Resolva esse problema com um código que funcione em qualquer situação.

inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

if inicio < fim:
    for i in range(inicio, fim+1, passos):
        print(i)
else:
    for i in range(inicio, fim-1, -passos):
        print(i)


# ex043: Crie um programa que leia 6 números inteiros e no final mostre quantos deles são pares e quantos são ímpares.
pares = 0
impares = 0

for i in range(6):
    numero = int(input(f'Digite o número {i+1}: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f'Foram {pares} pares digitados e {impares} ímpares digitados.')


# ex044: Faça um programa que leia 7 nomes de pessoas e guarde-os em um vetor. No final, mostre uma listagem com todos os nomes informados, na ordem inversa daquela em que eles foram informados.

vetor = [[], [], [], [], [], [], []]

for i in range(7):
    pessoa = input('Digite o nome da pessoa: ')
    vetor[i] = pessoa

vetor.reverse()
print(vetor)


# ex045: Crie um programa que tenha uma função Media(), que vai receber as 2 notas de um aluno e retornar a sua média para o programa principal.

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

def Media(n1, n2):
    media = (n1 + n2) / 2
    return media


print('Média:', Media(n1, n2))


# ex046: Crie um programa que melhore o procedimento Gerador() da questão anterior para que mostre a mensagem repetida varias vezes
# Ex: Ao chamar Gerador("Aprendendo Portugol", 4) aparece:
# +-------=======------+
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# Aprendendo Portugol
# +-------=======------+

def Gerador(texto, quantidade=1):
    print('-' * 35)
    for _ in range(quantidade):
        print(texto)
    print('-' * 35)


Gerador("Aprendendo Python com Guanabara", 7)


# ex047: Desenvolva um algoritmo que leia dois valores pelo teclado e passe esses valores para um procedimento Maior() que vai verificar qual deles é o maior e mostrá-lo na tela. Caso os dois valores sejam iguais, mostrar uma mensagem informando essa característica.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

def Maior(n1, n2):
    if n1 > n2:
        print('O primeiro número é maior que o segundo número')
    elif n1 < n2:
        print('O primeiro número é menor que o segundo número')
    else:
        print('Ambos são iguais')
Maior(n1, n2)


# ex048: Crie uma lógica que leia um número inteiro e passe para um procedimento ParOuImpar() que vai verificar e mostrar na tela se o valor passado como parâmetro é PAR ou ÍMPAR.

numero = int(input('Digite um número: '))

def ParOuImpar(numero):
    print('PAR' if numero % 2 == 0 else 'ÍMPAR')


ParOuImpar(numero)


# ex049: Crie uma função que retorne o número de pontos baseado na vitória, no empate e na derrota de um time de futebol. Sabendo que: vitória = 3 pontos, empate = 1 ponto e derrota = 0 pontos
def retorna_numero_pontos(vitoria, empate, derrota):
    pontos_vitoria = vitoria * 3
    pontos_empate = empate * 1
    pontos_derrota = 0

    total = pontos_vitoria + pontos_empate + pontos_derrota
    return f"Os pontos totais são de {total}"


if __name__ == "__main__":
    print(retorna_numero_pontos(15, 2, 5))  # Os pontos totais são de 47
    print(retorna_numero_pontos(23, 12, 8))  # Os pontos totais são de 81
    print(retorna_numero_pontos(3, 3, 54))  # Os pontos totais são de 12


# ex050: Crie uma função que retorne o quadrado de um número
def retorna_quadrado(numero: int):
    if numero.is_integer():
        quadrado = numero ** 2
        return f"O quadrado de {numero} é {quadrado}"


if __name__ == "__main__":
    print(retorna_quadrado(15))
    print(retorna_quadrado(23))
    print(retorna_quadrado(0))
    print(retorna_quadrado(-4))


# ex051: Escreva uma função que tem como argumento minutos e converta para segundos
def converte_minutos_para_segundos(minutos: int):
    if minutos.is_integer():
        segundos = minutos * 60
        return f"O total de segundos é {segundos}"

    return "Os minutos devem ser inteiros."


if __name__ == "__main__":
    print(converte_minutos_para_segundos(5))
    print(converte_minutos_para_segundos(12))
    print(converte_minutos_para_segundos(10))


# ex052: Crie uma função que recebe um número e imprima seu sucessor e seu antecessor
def sucessor_antecessor(numero: int):
    if numero < 1 or numero > 10000000:
        return "O número deve estar entre 1 e 10mi."

    sucessor = numero + 1
    antecessor = numero - 1

    return f"O número sucessor é {sucessor} e o número antecessor é {antecessor}"


if __name__ == "__main__":
    print(sucessor_antecessor(15))
    print(sucessor_antecessor(23))
    print(sucessor_antecessor(1))
    print(sucessor_antecessor(9999999))


# ex053: Crie uma função que recebe um número e imprima o seu dobro.
def dobro(numero: int):
    if numero < 1 or numero > 10000000:
        return "O número deve estar entre 1 e 10mi."
    dobro = numero * 2
    return f"O dobro de {numero} é {dobro}"


if __name__ == "__main__":
    print(dobro(15))
    print(dobro(25))


# ex054: Crie um programa que tem a possibilidade de converter reais para doláres e vice-versa. Considere que: 1 dolár = R$6
def conversor(tipo: str, quantidade: float):
    if tipo.lower() == 'doláres':
        conversao = round(quantidade * 6, 2)
        return f'Você tem R${conversao} reais'
    elif tipo.lower() == 'reais':
        conversao = round(quantidade / 6, 2)
        return f'Você tem ${conversao} doláres'

    return 'Algo de errado. Tente novamente'


if __name__ == "__main__":
    print(conversor('doláres', 5))
    print(conversor('reais', 5))
    print(conversor('doláres', 12000))
    print(conversor('reais', 55600))
    print(conversor('reais', 65.90))


# ex055: Crie uma função que retorna um número, baseado numa string
strings = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
def retorna_numero(string: str):
    if string in strings:
      posicao_string = strings.index(string)
      return f"O número é: {posicao_string}"

    return "Este número não está na string."


if __name__ == "__main__":
    print(retorna_numero('mil'))  # Este número não está na string.
    print(retorna_numero('nove'))  # O número é: 9
    print(retorna_numero('zero'))  # O numero é: 0


# ex056: Crie uma função que simule a chance de ser impostor no Among Us. Considere a fórmula: (numero_impostores / quantidade_jogadores) * 100
def chance_impostor_AmongUs(impostores: int, jogadores: int):
    chance = round((impostores / jogadores) * 100)
    return f"A chance de você ser impostor é de {chance}%"


if __name__ == "__main__":
    print(chance_impostor_AmongUs(2, 16))  # A chance de você ser impostor é de 12%
    print(chance_impostor_AmongUs(1, 10))  # A chance de você ser impostor é de 10%
    print(chance_impostor_AmongUs(2, 5))  # A chance de você ser impostor é de 40%


# ex057: Faça uma função que recebe a idade de uma pessoa em anos, meses e dias e retorna essa idade expressa em dias.
def retorna_dias_pessoa(anos: int, meses: int, dias: int):
    if meses > 12 or meses < 1 or dias < 1 or dias > 31 or anos < 1 or anos > 120:
        return "Cadastro inválido. Por favor, verifique os valores."

    dias += anos * 365
    dias += meses * 30

    return f"Dias totais: {dias}"


if __name__ == "__main__":
    print(retorna_dias_pessoa(15, 2, 10))  # Dias totais: 5545
    print(retorna_dias_pessoa(25, 8, 31))  # Dias totais: 9396
    print(retorna_dias_pessoa(120, 12, 31))  # Dias totais: 44191
    print(retorna_dias_pessoa(0, 45, 12))  # Cadastro inválido. Por favor, verifique os valores.


# ex058: Crie uma função que retorne todos os livros que uma pessoa leu. Cadastre pessoas
def livros(nome, *livros):
    return f"{nome} leu {", ".join(livros)}"

if __name__ == "__main__":
    print(livros("Maria", 'O poder dos Hábitos', 'Hábitos Atómicos'))  # Maria leu O poder dos Hábitos, Hábitos Atómicos
    print(livros("Pedro", 'Como fazer amigos e influenciar pessoas', 'As 48 leis do poder', 'A coragem de ser imperfeito'))  # Pedro leu Como fazer amigos e influenciar pessoas, As 48 leis do poder, A coragem de ser imperfeito
    print(livros("Lucas", 'Os segredos da mente milionária', 'Comece pelo porquê'))  # Lucas leu Os segredos da mente milionária, Comece pelo porquê


# ex059: Faça um Programa que leia um número e exiba o dia correspondente da semana
def dia_de_semana(numero: int):
    dias = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']

    if numero not in range(1, 8):
        return 'Não foi possível acessar o dia.'

    return dias[numero-1]


if __name__ == "__main__":
    print(dia_de_semana(1))  # Segunda
    print(dia_de_semana(6))  # Sábado
    print(dia_de_semana(7))  # Domingo
    print(dia_de_semana("Python"))  # Não foi possível acessar o dia.


# ex060: Faça um programa que tenha um procedimento chamado Contador() que recebe três valores como parâmetro: o início, o fim e o incremento de uma contagem. O programa principal deve solicitar a digitação desses valores e passá-los ao procedimento, que vai mostrar a contagem na tela.
# Ex: Para os valores de início (4), fim (20) e incremento(3) teremos Contador(4, 20, 3) vai mostrar na tela 4 >> 7 >> 10 >> 13 >> 16 >> 19 >> FIM


inicio = int(input('Digite o início: '))
fim = int(input('Digite o fim: '))
passos = int(input('Digite os passos: '))

def Contador(inicio, fim, passos):
    for i in range(inicio, fim+1, passos):
        print(f'{i} >> ', end='')
    print('FIM')


Contador(inicio, fim, passos)


# ex061: Crie uma função que verifica se um número é inteiro
def verify_integer_number(number):
    return number.is_integer()


if __name__ == "__main__":
    print(verify_integer_number(55))
    print(verify_integer_number(23.4))
    print(verify_integer_number(23.0))


# ex062: Crie um programa que leia o nome de várias pessoas e exiba a lista em ordem alfabética.
lista = []

while True:
    nome = input('Digite o nome da pessoa: ').strip().title()
    lista.append(nome)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

print(f'A lista com os nomes em ordem alfabética é {sorted(lista)}')


# ex063: Faça um aplicativo que leia o preço de 8 produtos. No final, mostre na tela qual foi o maior e qual foi o menor preço digitados.

maior = menor = 0
for i in range(8):
    preco = float(input(f'Digite o preço do produto {i+1}: '))

    if i == 0:
        maior = menor = preco
    else:
        if preco > maior:
            maior = preco
        elif preco < menor:
            menor = preco
print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')


""" # Outras maneiras de fazer o mesmo programa
Gostaria de colocar aqui outras maneiras de se fazer este mesmo
programa em especifico, porque ele pode ser escrito de diversas
formas até melhores que esta."""

# Maneira 1
# precos = []

# for i in range(8):
#     preco = float(input(f'Digite o preço do produto {i+1}: '))
#     precos.append(preco)

# maior = max(precos)
# menor = min(precos)

# print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')




# Maneira 2
# maior = menor = 0
# contador = 1

# while contador <= 8:
#     preco = float(input(f'Digite o preço do produto {contador}: '))
    
#     if contador == 1:
#         maior = menor = preco
#     else:
#         maior = max(maior, preco)
#         menor = min(menor, preco)
    
#     contador += 1

# print(f'O maior preço digitado foi {maior} e o menor preço digitado foi {menor}')

# print("\n" + "="*50 + "\n")


# ex064: # Crie um programa que leia vários números pelo teclado e mostre no final o somatório entre eles.
# Obs: O programa será interrompido quando o número 1111 for digitado

numeros = []
soma = 0
while True:
    numero = int(input('Digite um número: '))

    if numero == 1111:
        break

    numeros.append(numero)
    soma += numero

print(f'A soma dos números digitados é {soma}')


# ex065: Refaça o exercício 105, só que agora em forma de função Maior(), mas faça uma adaptação que vai receber TRÊS números como parâmetro e vai retornar qual foi o maior entre eles.

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

def Maior(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return 'O primeiro número é o maior número'
    elif n2 > n1 and n2 > n3:
        return 'O segundo número é o maior número'
    elif n3 > n1 and n3 > n2:
        return 'O terceiro número é o maior número'


print(Maior(n1, n2, n3))


# ex066: Crie um programa que tenha uma função SuperSomador(), que vai receber dois números como parâmetro e depois vai retornar a soma de todos os valores no intervalo entre os valores recebidos.
# Ex:
# SuperSomador(1, 6) vai somar 1 + 2 + 3 + 4 + 5 + 6 e vai retornar 21
# SuperSomador(15, 19) vai somar 15 + 16 + 17 + 18 + 19 e vai retornar 85

def SuperSomador(n1, n2):
    soma = 0
    for i in range(n1, n2+1):
        a = i
        soma += a
    return f'Soma: {soma}'


print(SuperSomador(1, 6))
print(SuperSomador(4, 10))
print(SuperSomador(3, 9))
print(SuperSomador(15, 19))
print(SuperSomador(7, 14))


# ex067: Melhore o exercício 73, criando além da função Media() uma outra função chamada Situacao(), que vai retornar para o programa principal se o aluno está APROVADO, em RECUPERAÇÃO ou REPROVADO. Essa nova função, vai receber como parâmetro o resultado retornado pela função Media().

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

def Media(n1, n2):
    global media
    media = (n1 + n2) / 2
    return media


def Situacao(media):
    if media >= 7:
        return 'APROVADO'
    elif media >= 5:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'


print(Media(n1, n2))
print(Situacao(media))


# ex068: Crie uma função que aceite kwargs e retorne a soma de todos os valores passados como argumentos.
def soma(*numeros):
    total = 0
    for numero in numeros:
        total += numero

    return f"O total é {total}"


print(soma(10, 20, 30, 40))  # O total é 100
print(soma(35, 78, 12, 38, 84, 437))  # O total é 684


# ex069: Crie uma função que recebe um texto e uma letra e verifica quantas vezes essa letra está presente no texto
def conta_letras(texto: str, letra: str):
    if len(letra) == 1:
        if letra in texto:
            contagem = texto.count(letra)
            return f"A letra aparece {contagem} vezes no texto."

        return "A letra não aparece no texto."

    return "A letra deve conter apenas um caractere."


if __name__ == "__main__":
    print(conta_letras("Python", "o"))  # A letra aparece 1 vez no texto.
    print(conta_letras("JavaScript", "a"))  # A letra aparece 2 vezes no texto.
    print(conta_letras("Branco", "Z"))  # A letra não aparece no texto.
    print(conta_letras("Amazônia", "ama"))  # A letra deve conter apenas um caractere.


# ex070: Exercício do FizzBuzz
def FizzBuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


FizzBuzz()


# ex071: Crie uma função que recebe um número e faz uma contagem regressiva desse número
def contagem_regressiva(contagem: int):
    for numero in range(contagem, 0, -1):
        print(numero)


if __name__ == "__main__":
    contagem_regressiva(15)
    contagem_regressiva(5)
    contagem_regressiva(23)


# ex072: Crie um jogo de JoKenPo (Pedra-Papel-Tesoura) com o computador
from random import randint
computador = randint(1, 3)
escolha = input('pedra, papel ou tesoura? ').strip().lower()

computador = 'pedra' if computador == 1 else 'papel' if computador == 2 else 'tesoura'
print(f'A máquina escolheu {computador}')   

empate = computador == escolha

vitoria = (computador == "pedra" and escolha == "papel") or (computador == "papel" and escolha == "tesoura") or (computador == "tesoura" and escolha == "pedra")

derrota = (computador == "pedra" and escolha == "tesoura") or (computador == "papel" and escolha == "pedra") or (computador == "tesoura" and escolha == "papel")

print('Empate' if empate else 'Você ganhou! A máquina perdeu' if vitoria else 'Você perdeu! A máquina ganhou' if derrota else 'Escolha inválida! Digite "pedra", "papel" ou "tesoura"')


# ex073: Crie uma função que recebe uma lista e um elemento, e verifique se aquele elemento está ou não presente na lista
def verifica_elemento_na_lista(lista: list, elemento):
    if elemento in lista:
        indice_elemento = lista.index(elemento)
        return f"O elemento está na lista, no índice {indice_elemento}"

    return f"O elemento ({elemento}) não está presente na lista ({lista})"


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5]
    print(verifica_elemento_na_lista(lista1, 2))  # O elemento está na lista, no índice 1

    lista2 = ["A", "B", "C", "D", "E"]
    print(verifica_elemento_na_lista(lista2, "Z"))  # O elemento (Z) não está presente na lista (['A', 'B', 'C', 'D', 'E'])

    lista3 = []
    print(verifica_elemento_na_lista(lista3, "A"))  # O elemento (A) não está presente na lista ([])


# ex074: Faça um programa que simule o lançamento de dois dados e exiba o resultado da soma.
from random import randint

def simulacao_dado():
    dado1 = randint(1, 6)
    dado2 = randint(1, 6)

    resultado = dado1 + dado2
    print(f'O resultado do dado 1 ({dado1}) com o dado 2 ({dado2}) é {resultado}')


simulacao_dado()


# ex075: Simule um caixa eletrônico, onde o usuário tem apenas 3 tentativas para digitar a senha correta. (senha="admin")
def caixa_eletronico():
    tentativas = 3

    while tentativas >= 1:
        senha = input("Olá, digite a sua senha:\n>>> ")

        if senha == "admin":
            print("Senha correta. Bem-vindo(a)!")
            tentativas = 0
        else:
            tentativas -= 1
            if tentativas != 0:
                print(f"Senha incorreta. Tentativas restantes: {tentativas}")
            else:
                print("Você excedeu o número máximo de tentativas. Tente novamente mais tarde.")


if __name__ == "__main__":
    caixa_eletronico()


# ex076: Faça um programa que leia o ano de nascimento de uma pessoa, calcule a idade dela e depois mostre se ela pode ou não votar.
from datetime import datetime
nascimento = int(input('Digite a sua data de nascimento: '))

ano = datetime.now().year
idade = ano - nascimento

if idade >= 18:
    print('Você pode votar')
else:
    print(f'Você não pode votar, pois tem {idade} anos')


# ex077: Crie um algoritmo que leia a idade de 10 pessoas, mostrando no final:
# a) Qual é a média de idade do grupo
# b) Quantas pessoas tem mais de 18 anos
# c) Quantas pessoas tem menos de 5 anos
# d) Qual foi a maior idade lida

idades = []
maior18 = menor5 = 0
for i in range(10):
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    while idade < 0 or idade > 120:
        idade = int(input(f'Digite a idade corretamente {i+1}: '))
        
    idades.append(idade)

    if idade > 18:
        maior18 += 1

    if idade < 5:
        menor5 += 1

media = sum(idades) / len(idades)
maior = max(idades)

print(f'A média das idades é de {media}')
print(f'Há {maior18} pessoas maiores de 18 anos')
print(f'Há {menor5} pessoas menores de 5 anos')
print(f'A maior idade foi {maior}')


# ex078: Faça um programa que leia a idade e o sexo de 5 pessoas, mostrando no final:
# a) Quantos homens foram cadastrados
# b) Quantas mulheres foram cadastradas
# c) A média de idade do grupo
# d) A média de idade dos homens
# e) Quantas mulheres tem mais de 20 anos

idades = []
grupo_homens = []
homens = mulheres = mulher_maior20 = 0
for i in range(5):
    idade = int(input(f'Digite a idade da pessoa {i+1}: '))
    sexo = input(f'Digite o sexo da pessoa {i+1} [M/F]: ').strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input(f'O sexo deve ser M ou F: ').strip().upper()

    idades.append(idade)
    
    if sexo == 'M':
        grupo_homens.append(idade)
        homens += 1
    elif sexo == 'F':
        mulheres += 1
        if idade > 20:
            mulher_maior20 += 1

media = sum(idades) / len(idades)
media_homens = sum(grupo_homens) / len(grupo_homens)

print(f'Foram cadastrados {homens} {"homem" if homens == 1 else "homens"}')
print(f'Foram cadastradas {mulheres} {"mulher" if mulheres == 1 else "mulheres"}')
print(f'A média das idades é {media}')
print(f'A média das idades dos homens é {media_homens}')
print(f'Há {mulher_maior20} {"mulher" if mulher_maior20 == 1 else "mulheres"} com mais de 20 anos')


# ex079: Desenvolva um aplicativo que leia o peso e a altura de 5 pessoas, mostrando no final:
# a) Qual foi a média de altura do grupo
# b) Quantas pessoas pesam mais de 90Kg
# c) Quantas pessoas que pesam menos de 50Kg e tem menos de 1.60m
# d) Quantas pessoas que medem mais de 1.90m e pesam mais de 100Kg.

alturas = []
mais90 = peso50_alt160 = peso100_alt190 = 0
for i in range(5):
    peso = float(input(f'Digite o peso da pessoa {i+1}: '))
    altura = float(input(f'Digite a altura da pessoa {i+1}: '))

    alturas.append(altura)

    if peso > 90:
        mais90 += 1
    
    if peso < 50 and altura < 1.60:
        peso50_alt160 += 1
    
    if peso > 100 and altura > 1.90:
        peso100_alt190 += 1


media = sum(alturas) / len(alturas) / 10

print(f'A média das alturas é de {media}')
print(f'Há {mais90} {"pessoa que pesa" if mais90 == 1 else "pessoas que pesam"} mais de 90 quilos')
print(f'Há {peso50_alt160} {"pessoa que pesa" if peso50_alt160 == 1 else "pessoas que pesam"}  menos de 50 quilos e tem menos de 1.60m')
print(f'Há {peso100_alt190} {"pessoa que pesa" if peso100_alt190 == 1 else "pessoas que pesam"} mais de 100 quilos e tem mais de 1.90m')


# ex080: Desenvolva um aplicativo que leia o salário e o sexo de vários funcionários. No final, mostre o total de salários pagos aos homens e o total pago às mulheres. O programa vai perguntar ao usuário se ele quer continuar ou não sempre que ler os dados de um funcionário.

salarios_homens = []
salarios_mulheres = []
while True:
    salario = float(input('Digite o salário: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()

    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    if sexo == 'M':
        salarios_homens.append(salario)
    elif sexo == 'F':
        salarios_mulheres.append(salario)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Digite corretamente [S/N]: ').strip().upper()
    if continuar == 'N':
        break 
    elif continuar == 'S':
        continue

homens = sum(salarios_homens)
mulheres = sum(salarios_mulheres)

print(f'O salário total dos homens é {homens}')
print(f'Já o salário total das mulheres é {mulheres}')


# ex081: Faça um algoritmo que leia a nota de vários alunos de uma turma. O programa vai parar quando for digitada a nota 999. No final, mostre quantos alunos existem na turma e qual é a média de notas do grupo.

notas = []
alunos = 0
while True:
    nota = int(input(f'Digite a nota do aluno [999 = sair]: '))
    while nota < 0 or nota > 10 and nota != 999:
        nota = int(input(f'Digite corretamente [999 = sair]: '))
    if nota == 999:
        break



    alunos += 1
    notas.append(nota)

if len(notas) > 1:
    media = sum(notas) / len(notas)
    print(f'Nessa turma, existem {alunos} alunos')
    print(f'A média de notas da turma é de {media}')


# ex082: Crie um programa que leia o sexo e a idade de várias pessoas. O programa vai perguntar se o usuário quer continuar ou não a cada pessoa. No final, mostre:
# a) qual é a maior idade lida
# b) quantos homens foram cadastrados
# c) qual é a idade da mulher mais jovem
# d) qual é a média de idade entre os homens

idades = []
idades_homens = []
idades_mulheres = []
while True:
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()
    
    idades.append(idade)

    if sexo == 'M':
        idades_homens.append(idade)
    elif sexo == 'F':
        idades_mulheres.append(idade)


    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue


maior = max(idades)
homens = len(idades_homens)
mulher_jovem = min(idades_mulheres)
media = sum(idades_homens) / len(idades_homens)

print(f'A maior idade é {maior}')
print(f'Foram cadastrados {homens} {"homem" if homens == 1 else "homens"}')
print(f'A idade da mulher mais jovem é {mulher_jovem}')
print(f'A média da idade dos homens é de {media}')


# ex083: Desenvolva um algoritmo que leia o nome, a idade e o sexo de várias pessoas. O programa vai perguntar se o usuário quer ou não continuar. No final, mostre:
# a) O nome da pessoa mais velha
# b) O nome da mulher mais jovem
# c) A média de idade do grupo
# d) Quantos homens tem mais de 30 anos
# e) Quantas mulheres tem menos de 18 anos

nomes = []
idades = []
homens30 = mulheres18 = 0
while True:
    nome = input('Digite o nome: ').strip().title()
    idade = int(input('Digite a idade: '))

    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    if sexo == 'M':
        if idade > 30:
            homens30 += 1
    elif sexo == 'F':
        if idade < 18:
            mulheres18 += 1
    nomes.append(nome)
    idades.append(idade)

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

velho = idades.index(max(idades))
jovem = idades.index(min(idades))
media = sum(idades) / len(idades)
print(f'O nome da pessoa mais velha é {nomes[velho]}, e tem {idades[velho]} anos')
print(f'A pessoa mais jovem é {nomes[jovem]}, e tem {idades[jovem]} anos')
print(f'A média das idades é de {media}')
print(f'Há {homens30} {"homem" if homens30 == 1 else "homens"} com mais de 30 anos')
print(f'Há {mulheres18} {"mulher" if mulheres18 == 1 else "mulheres"} com menos de 18 anos')


# ex084: Faça um programa usando a estrutura “faça enquanto” que leia a idade de várias pessoas. A cada laço, você deverá perguntar para o usuário se ele quer ou não continuar a digitar dados. No final, quando o usuário decidir parar, mostre na tela:
# a) Quantas idades foram digitadas
# b) Qual é a média entre as idades digitadas
# c) Quantas pessoas tem 21 anos ou mais.

idades = []
idade21 = 0
while True:
    idade = int(input('Digite a idade: '))

    idades.append(idade)

    if idade > 21:
        idade21 += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

media = sum(idades) / len(idades)
print(f'Há {len(idades)} idades cadastradas')
print(f'A média das idades é de {round(media, 2)}')
print(f'Há {idade21} {"pessoa" if len(idades) == 1 else "pessoas"} com mais de 21 anos.')


# ex085: Crie um programa usando a estrutura “faça enquanto” que leia vários números. A cada laço, pergunte se o usuário quer continuar ou não. No final, mostre na tela:
# a) O somatório entre todos os valores
# b) Qual foi o menor valor digitado
# c) A média entre todos os valores
# d) Quantos valores são pares

numeros = []
pares = 0
while True:
    numero = int(input('Digite um número: '))
    numeros.append(numero)

    pares += 1

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    while continuar not in ['S', 'N']:
        continuar = input('Deseja continuar? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    elif continuar == 'S':
        continue

media = sum(numeros) / len(numeros)
menor = numeros.index(min(numeros))

print(f'A soma de todos os valores é de {sum(numeros)}')
print(f'O menor número digitado foi {numeros[menor]}, e aparece na {numeros.index(numeros[menor])+1}ª posição')
print(f'A média dos números é de {round(media, 2)}')
print(f'Há {pares} números {"par" if pares == 1 else "pares"}')


# ex086: Crie um programa que leia sexo e peso de 8 pessoas, usando a estrutura “para”. No final, mostre na tela:
# a) Quantas mulheres foram cadastradas
# b) Quantos homens pesam mais de 100Kg
# c) A média de peso entre as mulheres
# d) O maior peso entre os homens

homem_peso100 = mulheres = 0
peso_homens = []
peso_mulheres = []
for i in range(8):
    sexo = input('Digite o sexo [M/F]: ').strip().upper()
    while sexo not in ['M', 'F']:
        sexo = input('Digite corretamente [M/F]: ').strip().upper()

    peso = float(input('Digite o peso: '))

    if sexo == 'F':
        peso_mulheres.append(peso)
        mulheres += 1
    if sexo == 'M':
        peso_homens.append(peso)
        if peso > 100:
            homem_peso100 += 1


maior = peso_homens.index(max(peso_homens))
media_mulheres = sum(peso_mulheres) / len(peso_mulheres)
print(f'Foram cadastradas {mulheres} {"mulher" if mulheres == 1 else "mulheres"}')
print(f'Há {homem_peso100} {"homem" if homem_peso100 == 1 else "homens"} com mais de 100Kg.')
print(f'A média de pesos entre as mulheres é de {media_mulheres}')
print(f'O maior peso entre os homens foi de {peso_homens[maior]}')


# ex087: Crie uma função que calcule a tabuada de 0 até o número que o usuário digitou.
def tabuada(numero_tabuada: int):
    if numero_tabuada < 1 or numero_tabuada > 1_000_000:
        print("O número deve estar entre 1 a 1 milhão.")
        return False

    for numero in range(0, 11):
        resultado = numero * numero_tabuada
        print(f"{numero_tabuada} * {numero} = {resultado}")


if __name__ == "__main__":
    tabuada(7)
    tabuada(45)
    tabuada(154)


# ex088: Smith criou uma loja de produtos. Ele tem uma conta especial para ele mesmo, com mais de 100 mil clientes em sua loja. Ele precisa que você crie uma função que retorne uma mensagem agradável se a senha for a de Smith. Caso contrário, retorne uma mensagem de boas-vindas ao Cliente.
def verifica_usuario(usuario, senha):
    if usuario == "admin" and senha == 'admin':
        return 'O Criador entrou!'

    return 'Olá, usuário!'


if __name__ == "__main__":
    print(verifica_usuario("SmithFan", "ILoveSmith"))  # Olá, usuário!
    print(verifica_usuario("admin", "admin"))  # O Criador entrou!
    print(verifica_usuario("Smith", "password"))  # Olá, usuário!


# ex089: Crie uma função que receba um número como parâmetro e retorne todos os números pares de 0 até este número.
def encontra_pares(numero: int):
    if numero < 1 or numero > 1_000_000:
        return "O número deve estar entre 1 a 1 milhão."

    pares = [par for par in range(numero+1) if par % 2 == 0]
    return f"Os números pares de 0 até {numero} são: {pares}"


if __name__ == "__main__":
    print(encontra_pares(12))  # Os números pares de 0 até 12 são: [0, 2, 4, 6, 8, 10, 12]
    print(encontra_pares(450))  # Os números pares de 0 até 450 são: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 102, 104, 106, 108, 110, 112, 114, 116, 118, 120, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144, 146, 148, 150, 152, 154, 156, 158, 160, 162, 164, 166, 168, 170, 172, 174, 176, 178, 180, 182, 184, 186, 188, 190, 192, 194, 196, 198, 200, 202, 204, 206, 208, 210, 212, 214, 216, 218, 220, 222, 224, 226, 228, 230, 232, 234, 236, 238, 240, 242, 244, 246, 248, 250, 252, 254, 256, 258, 260, 262, 264, 266, 268, 270, 272, 274, 276, 278, 280, 282, 284, 286, 288, 290, 292, 294, 296, 298, 300, 302, 304, 306, 308, 310, 312, 314, 316, 318, 320, 322, 324, 326, 328, 330, 332, 334, 336, 338, 340, 342, 344, 346, 348, 350, 352, 354, 356, 358, 360, 362, 364, 366, 368, 370, 372, 374, 376, 378, 380, 382, 384, 386, 388, 390, 392, 394, 396, 398, 400, 402, 404, 406, 408, 410, 412, 414, 416, 418, 420, 422, 424, 426, 428, 430, 432, 434, 436, 438, 440, 442, 444, 446, 448, 450]
    print(encontra_pares(1))  # Os números pares de 0 até 1 são: [0]


# ex090: Crie um programa que realiza a contagem regressiva de 5 segundos
from time import sleep

def contagem_regressiva():
    for i in range(5, 0, -1):
        print(i)
        sleep(1)


contagem_regressiva()


# ex091: Crie uma função que receba um número e imprima uma escada de estrelas (asteriscos)
def piramide_de_estrelas(quantidade: int):
    if quantidade < 1 or quantidade > 100:
        print("A quantidade deve estar entre 1 a 100.")
        return None

    for numero in range(1, quantidade+1):
        print("*" * numero)


quantidade = int(input("Digite a quantidade de 1 a 100:\n>>> "))
piramide_de_estrelas(quantidade)


# ex092: Inverta o exercício 11 - imprima uma escada de estrelas invertidas
def piramide_de_estrelas(quantidade: int):
    if quantidade < 1 or quantidade > 100:
        print("A quantidade deve estar entre 1 a 100.")
        return None

    for numero in range(quantidade, 0, -1):
        print("*" * numero)


quantidade = int(input("Digite a quantidade de 1 a 100:\n>>> "))
piramide_de_estrelas(quantidade)


# ex093: Crie uma função que retorne o primeiro elemento de uma lista
def retorna_primeiro_elemento(lista: list):
    if len(lista) > 0:
        return f"O primeiro elemento da lista é {lista[0]}"

    return "A lista deve possuir ao menos um elemento."

if __name__ == "__main__":
    lista1 = ["Maçã", "Banana", "Laranja", "Abacaxi"]
    print(retorna_primeiro_elemento(lista1))  # O primeiro elemento da lista é Maçã

    lista2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # O primeiro elemento da lista é 1
    print(retorna_primeiro_elemento(lista2))

    lista3 = []
    print(retorna_primeiro_elemento(lista3))  # A lista deve possuir ao menos um elemento.


# ex094: Ingressos de cinema: Um cinema cobra preços de ingressos diferentes, dependendo da idade da pessoa. Se a pessoa for menor de 3 anos, o ingresso é gratuito; se tiver entre 3 e 12 anos, o ingresso custa U$S10; e caso tenha mais de 12 anos, o ingresso custa US$15. Escreva um loop que pergunte a idade dos usuários e, em seguida, informe o preço do ingresso do cinema.
def ingressos_cinema(pessoas: int):
    if pessoas < 1 or pessoas > 50:
        return f"O limite de pessoas foi alcançado."

    preco = 0
    for i in range(pessoas):
        idade = int(input(f'Digite a idade da pessoa {i+1}: '))
        while idade < 1 or idade > 120:
            idade = int(input(f'A idade excedeu o limite.\nDigite a idade da pessoa {i+1}: '))

        if idade < 3: # Se idade for menor que 3, ingresso gratuito
            ingresso = 0
        elif idade >= 3 and idade <= 12: # Se idade estiver entre 3 e 12, ingresso custa 10 reais.
            ingresso = 10
        elif idade > 12: # Se idade for maior que 12, ingresso custa 15 reais
            ingresso = 15

        preco += ingresso

    return f"O preço total dos ingressos é de R${preco} reais."


if __name__ == "__main__":
    pessoas = int(input("Digite a quantidade de pessoas: "))
    print(ingressos_cinema(pessoas))


# ex095: Crie um programa que preencha automaticamente um vetor numérico com 7 números gerados aleatoriamente pelo computador e depois mostre os valores gerados na tela.
import random

vetor = [[], [], [], [], [], [], []]

for i in range(7):
    vetor[i] = random.randint(1, 10)

print(vetor)


# ex096: Crie uma uma função que retorne a maior palavra de uma string.
def biggest_word(text: str):
    if len(text) < 1 or len(text) > 10000:
        return "Texto inválido."

    words = text.split()

    lenghts = list(map(len, words))
    position = lenghts.index(max(lenghts))

    word = words[position]
    return word


if __name__ == "__main__":
    print(biggest_word(""))  # Texto inválido.
    print(biggest_word("# a b c d"))  # #
    print(biggest_word("Tor is the best anonymous and security browser")) # anonymous


# ex097: Crie um programa que receba o nome de um arquivo como parâmetro e retorne o conteúdo do arquivo
def retorna_conteudo_arquivo(arquivo: str):
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            f.seek(0)
            conteudo = f.read()

            return f"Conteúdo:\n---------------------------------------\n{conteudo}\n---------------------------------------"
    except FileNotFoundError as file_found_e:
        return f"Arquivo não encontrado: {file_found_e}"
    except OSError as os_e:
        return f"Erro de sistema: {os_e}"
    except SyntaxError as syntax_e:
        return f"Erro de sintaxe: {syntax_e}"
    except NameError as name_e:
        return f"Erro de nome: {name_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_conteudo_arquivo("arquivo.txt"))  # [conteúdo]
    print(retorna_conteudo_arquivo("read.md"))  # Arquivo não encontrado: [Errno 2] No such file or directory: 'read.md'
    print(retorna_conteudo_arquivo(7))  # Erro de sistema: [WinError 6] Identificador inválido


# ex098: Crie uma função que receba uma string como parâmetro e retorne a string sem a primeira letra
def retorna_sem_primeira_letra(string: str):
    try:
        return string[1:]
    except AttributeError as attr_e:
        return f"O argumento deve ser uma string. Erro: {attr_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_sem_primeira_letra("Olá, mundo!"))  # "lá, mundo!"
    print(retorna_sem_primeira_letra("Python"))  # "ython"
    print(retorna_sem_primeira_letra(""))  # ""
    print(retorna_sem_primeira_letra(23))  # Erro: 'int' object is not subscriptable


# ex099: Crie uma função que retorne o maior valor de dois números
def retorna_maior_valor(n1: int, n2: int):
    try:
        if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)):
            return "Valores inválidos."

        # Maneira 1
        # maior_valor = max(n1, n2)
        # return f"O maior valor é {maior_valor}"

        # Maneira 2
        if n1 > n2:
            return f"O maior valor é {n1}, no índice 0."
        elif n1 < n2:
            return f"O maior valor é {n2}, no índice 1."

        return "Ambos possuem o mesmo valor."
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_maior_valor(15, 24))  # O maior valor é 24
    print(retorna_maior_valor(12, 12))  # Ambos possuem o mesmo valor.
    print(retorna_maior_valor("Python", "JS"))  # Valores inválidos.
    print(retorna_maior_valor(True, False))  # O maior valor é True, no índice 0. (cry)


# ex100: Escreva um programa que leia o ano de nascimento de um rapaz e mostre a sua situação em relação ao alistamento militar.
# - Se estiver antes dos 18 anos, mostre em quantos anos faltam para o alistamento.
# - Se já tiver depois dos 18 anos, mostre quantos anos já se passaram do alistamento.

from datetime import datetime
nascimento = int(input('Digite a sua data de nascimento: '))

ano = datetime.now().year
idade = ano - nascimento

if idade < 18:
    falta = 18 - idade
    print(f'Faltam {falta} anos')
else:
    passou = idade - 18
    print(f'Já se passou {passou} anos')


# ex101: Crie um jogo onde o computador vai sortear um número entre 1 e 5 o jogador vai tentar descobrir qual foi o valor sorteado.
from random import randint

computador = randint(1, 5)
escolha = int(input('Tente adivinhar o número entre 1 a 5: '))

while escolha <= 0 or escolha > 5:
    escolha = int(input('Por favor, escolha um número entre 1 a 5: '))

print(f'Você acertou' if escolha == computador else f'Você errou, o número era {computador}')


# ex102: # Faça um aplicativo onde o computador deve sortear um número entre 1 e 10 e o jogador tem 4 tentativas para tentar acertar
from random import randint

computador = randint(1, 10)

for i in range(4):
    print(f'⏳Tentativa {i+1}/4⏳'.center(50, '-'))

    escolha = int(input('Tente adivinhar o número entre 1 a 10: '))
    while escolha <= 0 or escolha > 10:
        escolha = int(input('❓Por favor, escolha um número entre 1 a 10❓: '))
    
    if escolha == computador:
        print('🎇 Você acertou!🎇')
        break
    else:
        if i == 3:
            print(f'🎈O número era {computador}🎈')
        else:
            print('❌ Você errou. Tente novamente❌')


# ex103: Crie um programa que leia o nome e o salário de um funcionário, mostrando no final uma mensagem.
def salario_funcionario():
    try:
        funcionario = input('Digite o nome do funcionário: ')
        salario = float(input('Digite o salário do funcionário: '))
    except ValueError as value_e:
        return f"O salário deve ser um número. Erro: {value_e}"
    except Exception as e:
        return f"Ocorreu um erro: {e}"

    return f'O(a) funcionário(a) {funcionario} tem um salário de R${salario}.'


if __name__ == "__main__":
    print(salario_funcionario())
    # if salario_funcionario(salario="e") -> O salário deve ser um número. Erro: could not convert string to float: 'e'


# ex104: Conte quantas linhas tem um arquivo.

def conta_linhas_arquivo(arquivo: str):
    try:
        with open(arquivo, "r", encoding="utf-8") as arquivo:
            arquivo.seek(0)

            linhas = 0
            for _ in arquivo.readlines():
                linhas += 1
            arquivo.seek(0)

            return f"Quantidade de linhas encontradas: {linhas}"
    except FileNotFoundError:
        return "Erro: Arquivo não encontrado/não existe. Verifique o caminho do arquivo ou crie um."
    except Exception as erro:
        return f"Erro: {erro}"


print(conta_linhas_arquivo("arquivo.txt"))


# ex105: Faça um programa que leia um número menor que 1000 e imprima centenas, dezenas e unidades.

def decomposicao(numero: int) -> str:
    if numero < 1 or numero >= 1000:
        return "O número deve ser maior ou igual a 1 e menor que 1000"

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    return f"Centenas: {centenas} | Dezenas: {dezenas} | Unidades: {unidades}"


def main():
    try:
        numero = int(input("Digite um número entre 1 e 999: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return

    print(decomposicao(numero))


if __name__ == "__main__":
    main()


# ex106: Crie uma função que tem uma string como parâmetro e verifica se a string é um palíndromo.
def verifica_palindromo(string: str):
    try:
        if len(string) < 1:
            return "A string deve ter ao mínimo 1 caractere."

        if string[::-1].lower() == string.lower():
            return "A string é um palíndromo."
    except TypeError as type_e:
        return f"A string deve conter apenas letras. Erro: {type_e}"
    except Exception as e:
        return f"Erro: {e}"

    return "A string não é um palíndromo."


if __name__ == "__main__":
    print(verifica_palindromo("radar"))  # A string é um palíndromo.
    print(verifica_palindromo("Ana"))  # A string é um palíndromo.
    print(verifica_palindromo(""))  # A string deve ter ao mínimo 1 caractere.
    print(verifica_palindromo(12345))  # A string deve ter ao mínimo 1 caractere.


# ex107: Faça um programa que verifique se uma letra digitada é vogal ou consoante.
def verifica_vogal_consoante(letra: str):
    vogais = ['a', 'á', 'à', 'ã', 'â', 'e', 'é', 'è', 'ê', 'í', 'ì', 'î', 'i', 'o', 'ó', 'ò', 'ô', 'õ', 'ú', 'ù', 'û', 'u']

    try:
        if not letra.isalpha() or len(letra) != 1:
            return 'Por favor, digite uma letra válida'
    except AttributeError as attr_e:
        return f"A função aceita apenas letras. Erro: {attr_e}"
    except Exception as e:
        return f"Erro: {e}"

    if letra.lower() in vogais:
        return f'vogal'

    return f'consoante'


if __name__ == "__main__":
    print(verifica_vogal_consoante("a"))  # vogal
    print(verifica_vogal_consoante(6))  # A função aceita apenas letras. Erro: 'int' object has no attribute 'isalpha'
    print(verifica_vogal_consoante(""))  # Por favor, digite uma letra válida
    print(verifica_vogal_consoante("ABC"))  # Por favor, digite uma letra válida
    print(verifica_vogal_consoante("é"))  # vogal
    print(verifica_vogal_consoante("w"))  # consoante


# ex108: Crie uma função que receba um texto como parâmetro e retorne a quantidade de palavras no texto.
def retorna_quantidade_palavras(texto: str):
    try:
        palavras = texto.split()
        quantidade_palavras = len(palavras)

        return f"A quantidade de palavras é de {quantidade_palavras}"
    except TypeError as type_e:
        return f"A função aceita apenas strings. Erro: {type_e}"


if __name__ == "__main__":
    print(retorna_quantidade_palavras("Python foi criado por Guido van Rossum"))  # A quantidade de palavras é de 7
    print(retorna_quantidade_palavras("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Placeat illo aut eius totam quaerat ad expedita ducimus explicabo, asperiores eaque, doloremque labore fugiat consequuntur, voluptatum nobis veniam quae animi hic!"))  # A quantidade de palavras é de 30


# ex109: Desenvolva um programa que faça o sorteio de 20 números entre 0 e 10 e mostre na tela:
# a) Quais foram os números sorteados
# b) Quantos números estão acima de 5
# c) Quantos números são divisíveis por 3
from random import randint

numeros = []
acima5 = div3 = 0

for i in range(20):
    numero = randint(0, 10)
    numeros.append(numero)

    if numero > 5:
        acima5 += 1

    if numero % 3 == 0:
        div3 += 1

print(f'Os números sorteados foram {numeros}')
print(f'São {acima5} números sorteados acima de 5')
print(f'São {div3} números sorteados que são divisíveis por 3')


# ex110: Crie uma função que recebe uma lista como parâmetro e retorne quais elementos NÃO são repetidos
def verifica_nao_repetidos(lista: list):
    if len(lista) < 1:
        return "A lista deve possuir ao menos 1 elemento."

    nao_repetidos = []
    for elemento in lista:
        if lista.count(elemento) == 1:
            nao_repetidos.append(elemento)

    if len(nao_repetidos) > 0:
        return f"Os elementos não repetidos são: {nao_repetidos}"

    return "Todos os itens se repetem."


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Os elementos não repetidos são: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(verifica_nao_repetidos(lista1))

    lista2 = ["a", "b", "a", "c"]
    print(verifica_nao_repetidos(lista2))  # Os elementos não repetidos são: ['b', 'c']

    lista3 = []
    print(verifica_nao_repetidos(lista3))  # A lista deve possuir ao menos 1 elemento.

    lista4 = ["a"]
    print(verifica_nao_repetidos(lista4))  # Os elementos não repetidos são: ['a']

    lista5 = ["a", "a", "a"]
    print(verifica_nao_repetidos(lista5))  # Todos os itens se repetem.


# ex111: Um grupo de amigos decidiu criar uma sociedade secrta. O nome dessa sociedade será a primeira letra de cada nome do grupo de amigos. Crie uma função que receba uma lista de nomes e retorne o nome da sociedade secreta.
def nome_sociedade_secreta(membros: list):
    nome = ""

    if len(membros) < 2:
        return "A lista deve possuir ao menos dois membros."

    for membro in membros:
        primeira_letra = membro[0]
        nome += primeira_letra

    return f"Nome da sociedade: {nome}"


if __name__ == "__main__":
    print(nome_sociedade_secreta(["João", "Maria", "Pedro", "Ana"]))  # Nome da sociedade: JMPA
    print(nome_sociedade_secreta(["Pedro", "Gabriel", "Gustavo", "Renata", "Marcos", "José"]))  # Nome da sociedade: PGGRMJ
    print(nome_sociedade_secreta(["Marcos"]))  # A lista deve possuir ao menos dois membros.
    print(nome_sociedade_secreta(["Marcos", "Felipe"]))  # Nome da sociedade: MF


# ex112: Crie um programa que verifica em que posições há disjuntores ligados e desligados
def verifica_posicoes_disjuntores(disjuntores: list):
    lista_pos = []

    if isinstance(disjuntores, list):
        for pos, disjuntor in enumerate(disjuntores):
            if isinstance(disjuntor, bool) and disjuntor:
                lista_pos.append(pos)

    if len(lista_pos) == 0:
        return "Nenhuma posição."

    return f"Lista de posições: {lista_pos}"


if __name__ == "__main__":
    lista1 = [True, True, False, False, True, False, False, False, True]
    print(verifica_posicoes_disjuntores(lista1))  # Lista de posições: [0, 1, 4, 8]

    lista2 = [False, True, False, False, False, True, True]
    print(verifica_posicoes_disjuntores(lista2))  # Lista de posições: [1, 5, 6]

    lista3 = [True, False, False, True, True, False, False]
    print(verifica_posicoes_disjuntores(lista3))  # Lista de posições: [0, 3, 4]

    lista4 = [1, 4, 6, 7, "Python"]
    print(verifica_posicoes_disjuntores(lista4))  # Nenhuma posição.


# ex113: Crie uma função que retorne a soma de todos os valores de um número
def sum_numbers(number: int):
    if number < 1 or number > 10000000:
        return "O número deve estar entre 1 a 10.000.000"

    number_list = []

    for num in str(number):
        number_list.append(int(num))

    sum_numbers = sum(number_list)
    return sum_numbers


if __name__ == "__main__":
    print(sum_numbers(548))  # 5 + 4 + 8 = 17
    print(sum_numbers(77732))  # 7 + 7 + 7 + 3 + 2 = 26
    print(sum_numbers(301))  # 3 + 0 + 1 = 4


# ex114: Crie uma função que retorne a soma de todos os valores de uma lista
def soma_valores_lista(lista: list):
    if len(lista) > 1:
        try:
            soma = sum(lista)
            return f"A soma de todos os elementos da lista é de {soma}"
        except TypeError:
            return "A lista deve conter apenas números."
        except Exception as e:
            return f"Erro: {e}"

    return "A lista deve contér mais de um elemento."   


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(soma_valores_lista(lista1))  # A soma de todos os elementos da lista é de 55

    lista2 = [2, 2]
    print(soma_valores_lista(lista2))  # A soma de todos os elementos da lista é de 4

    lista3 = []
    print(soma_valores_lista(lista3))  # A lista deve contér mais de um elemento.

    lista4 = ["Python", "JavaScript", "HTML", "CSS"]
    print(soma_valores_lista(lista4))  # A lista deve conter apenas números.


# ex115: Faça uma função que conta o número de vogais em uma string.
def count_vowels(string: str):
    if len(string) < 1 or len(string) > 250:
        return "O tamanho da string deve estar entre 1 a 250."

    try:
        VOWELS = ["a", "e", "i", "o", "u"]

        count = 0
        for letter in string.lower():
            if letter in VOWELS:
                count += 1

        return count
    except ValueError as value_e:
        return f"Erro de valor: {value_e}"
    except KeyboardInterrupt as keyboard_e:
        return f"Erro de teclado: {keyboard_e}"
    except TypeError as type_e:
        return f"Erro de tipo: {type_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(count_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # 5
    print(count_vowels("Existe uma cobra chamada Python."))  # 11
    print(count_vowels("Eistein é o maior cientista de todos os tempos."))  # 18
    print(count_vowels(""))  # O tamanho da string deve estar entre 1 a 250.
    print(count_vowels("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Provident facilis sequi voluptas, veritatis quaerat id repellendus blanditiis quo corporis, quis tempore obcaecati amet? Error, qui! Quam quidem consectetur tempore inventore? Placeat, saepe atque natus recusandae neque porro vel repellendus inventore molestiae ut?"))  # O tamanho da string deve estar entre 1 a 250.


# ex116: Crie uma classe chamada User. Crie dois atributos chamados nome e sobrenome e diversos outros atributos que normalmente são armazenados em um perfil de usuário. Crie um método chamado describe_user() que exiba um resumo das informações do usuário. Crie outro método chamado greet_user que exiba um cumprimento personalizado ao usuário.
class User:
    def __init__(self, ID: int = None, nome: str = None, sobrenome: str = None, idade: int = None, nascimento: str = None):
        self.ID = ID
        self.nome = nome.title()
        self.sobrenome = sobrenome.title()
        self.idade = idade
        self.nascimento = nascimento

    def describe_user(self):
        print(f'ID: {self.ID}, nome: {self.nome}, sobrenome: {self.sobrenome}, idade: {self.idade}, nascimento: {self.nascimento}')
  
    def greet_user(self):
        print(f'Olá, {self.nome} {self.sobrenome}!')

    def login(self):
        senha = input('Digite a sua senha: ')
        tentativas = 1
        while True:
            senha = int(input('Digite corretamente: '))
            if senha == 123456:
                print(f"Olá, {self.nome}. Seja bem-vindo(a).")
                break
            else:
                tentativas += 1
                print(f'Senha incorreta! {tentativas} tentativas já foram feitas.')


pedro = User(4, 'Pedro', 'Feitosa', 16, '23/06/2009')
pedro.describe_user()
pedro.greet_user()
pedro.login()


# ex117: # Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório desses números na tela. Após exibir a soma, o programa deve mostrar também os números que o usuário digitou, um por linha.
def mostrar_soma_e_numeros():
    numeros = []
    total = 0

    try:
        for i in range(5):
            numero = int(input(f'Digite o número {i+1}: '))

            numeros.append(numero)
            total += numero
    except ValueError as value_e:
        return f"A lista pode conter apenas números. Erro: {value_e}"
    except Exception as e:
        return f"Erro: {e}"

    return (f'A soma dos números digitados é {total}\n'
            f'Os números digitados foram: {numeros}')


if __name__ == "__main__":
    print(mostrar_soma_e_numeros())


# ex118: Crie uma programa que pede ao usuário 10 números, e separe e armazene números pares e números ímpares em duas listas diferentes.
def separar_pares_impares():
    pares = []
    impares = []

    try:
        for numero in range(10):
            numero = int(input(f'Digite o número {numero+1}: '))
            if numero % 2 == 0:
                pares.append(numero)
            else:
                impares.append(numero)
    except ValueError as value_e:
        return f"A lista pode conter apenas números. Erro: {value_e}"
    except Exception as e:
        return f"Erro: {e}"

    return (
        f"Lista de números pares: {pares}\n"
        f"Lista de números ímpares: {impares}"
    )


if __name__ == "__main__":
    print(separar_pares_impares())


# ex119: Crie uma função que receba uma lista e retorne "Par", se existe mais números pares, caso contrário, retorne "Ímpar".
def verifica_pares_impares(lista: list):
    pares = 0
    impares = 0

    if len(lista) < 1:
        return "A lista deve ter a menos um número."

    try:
        for numero in lista:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

        if pares > impares:
            return "Par"
        elif impares > pares:
            return "Ímpar"

        return "Pares e Ímpares"
    except TypeError:
        return "A lista deve conter apenas números."
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    lista1 = [12, 13, 14, 15, 16, 17, 18, 19, 20]  # Par
    print(verifica_pares_impares(lista1))

    lista2 = [2, 4, 1, 3]
    print(verifica_pares_impares(lista2))  # Pares e Ímpares

    lista3 = ["Par", "Ímpar"]
    print(verifica_pares_impares(lista3))  # A lista deve conter apenas números.


# ex120: Crie uma função que receba uma lista de números como parâmetro e retorne a média de números daquela lista.
def retorna_media(lista: int):
    if len(lista) < 2:
        return "A lista deve ter ao menos 2 elementos."

    try:
        soma = sum(lista)
        media = soma / len(lista)

        return f"A média de números da lista é de: {media}"
    except TypeError as type_e:
        return f"A lista deve conter apenas números. Erro: {type_e}"
    except Exception as e:
        return f"Erro: {e}"


if __name__ == "__main__":
    print(retorna_media([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))  # A média de números da lista é de: 5.0
    print(retorna_media(["a", "b", "c"]))  # A lista deve conter apenas números. Erro: unsupported operand type(s) for +: 'int' and 'str'
    print(retorna_media([]))  # A lista deve ter ao menos 2 elementos.


# ex121: Crie um programa que simule um jogo de "cara ou coroa" com estatísticas de vitórias.
from random import randint


def cara_ou_coroa(quantidade: int):
    if quantidade > 100 or quantidade < 1:
        return "A quantidade de tentativas deve ser menor que 100 e maior que 1."

    resultados = []
    for _ in range(quantidade):
        moeda = randint(0, 1)

        if not moeda:
            resultados.append("Cara")
        else:
            resultados.append("Coroa")

    return (
        f"Resultados: {", ".join(resultados)}\n"
        f"Qntd. de vezes que caiu Cara: {resultados.count("Cara")}\n"
        f"Qntd. de vezes que caiu Coroa: {resultados.count("Coroa")}\n"
    )


quantidade = int(input("Quantas vezes deseja jogar?\n>>> "))
print(cara_ou_coroa(quantidade))


# ex122: Crie um programa em que pede ao usuário um número e o programa deve retornar se este número é uma raíz exata ou não.
import math

while True:
    try:
        numero = int(input("Digite um número inteiro:\n>>>"))

        def verifica_raiz_exata(numero: int):
            raiz = math.sqrt(numero)

            if raiz.is_integer():
                yield f"{numero} é uma raíz quadrada exata"
            else:
                yield f"{numero} não é uma raíz quadrada exata"

            yield f"Resultado da raíz: {raiz}"

        for i in verifica_raiz_exata(numero):
            print(i)

    except ValueError:
        print("Por favor, digite um número inteiro\n")
    else:
        break


# ex123: Faça um simulador de dado
from random import randint


def simular_dado(quantidade: int):
    if quantidade > 10000 or quantidade < 1:
        yield "A quantidade de tentativas deve ser menor que 10000 e maior que 0."
        return None

    resultados = []
    for _ in range(quantidade):
        dado = randint(1, 6)

        resultados.append(dado)

    for i in range(1, 7):
        yield f"Dado caiu em {i}: {resultados.count(i)} vezes."

    yield f"Resultados: {resultados}"


try:
    quantidade = int(input("Digite a quantidade de vezes para sortear o dado:\n>>> "))
except ValueError:
    print("Valor inválido. Digite um número!")
except Exception as erro:
    print(f"Erro: {erro}")
else:
    for item in simular_dado(quantidade):
        print(item)


# ex124: Crie uma função que conta quantas letras há numa string.
def count_letters(text):
    already_list = []

    for letter in text:
        if letter.isalpha():
            if letter not in already_list:
                already_list.append(letter)
                print(f"{letter}: {text.count(letter)}")

if __name__ == "__main__":
    count_letters("Contador de Letras com Python!")
    count_letters("JavaScript ou Python?")
    count_letters("AAA BBB CCC DDD EEE")


# ex125: Crie uma função que conta quantas palavras há numa string.
def count_words(text):
    splitted_text = text.split()
    already_list = []

    for element in splitted_text:
        if element not in already_list:
            already_list.append(element)
            print(f"{element}: {splitted_text.count(element)}")

if __name__ == "__main__":
    count_words("Hello world! Hello Python!")
    count_words("Olá mundo! Olá Python!")


# ex126: Crie uma função que: Verifica se um número é primo; Mostra a quantidade de divisores; e quais são eles.
def prime_number(number: int):
    if number < 1 or number > 100000:
        return "The number need to be in a range of 2 and 100000."

    if number == 2:
        return True

    primes = []
    counter = 0
    number_range = range(1, number+1)

    for num in number_range:
        if number % num == 0:
            counter += 1
            primes.append(num)

    return (
    "----------------------------------\n"
    f"Número: {number}\n"
    f"Primo: {counter == 2}\n"
    f"Quant. Divisores: {counter}\n"
    f"Divisores: {primes}"
    "\n----------------------------------\n"
    )

if __name__ == "__main__":
    print(prime_number(16))
    print(prime_number(25))
    print(prime_number(3301))  # Cidada3301!
    print(prime_number(2597))


# ex127: Crie uma função que remove itens duplicados de uma lista, sem usar set.
def remove_duplicate_items(any_list: list, ordered: bool = False):
    if len(any_list) < 1:
        return "Lista Inválida."

    new_list = []
    for element in any_list:
        if element not in new_list:
            new_list.append(element)

    if ordered:
        new_list.sort()

    return new_list


if __name__ == "__main__":
    list1 = ["Mario", "Maria", "Felipe", "Jorge", "Jorge", "Maria"]
    print(remove_duplicate_items(list1, False))  # ['Mario', 'Maria', 'Felipe', 'Jorge']

    list2 = []
    print(remove_duplicate_items(list2, False))  # Lista Inválida.

    list3 = [3, 9, 8, 3, 2, 0, 5, 2, 8, 1, 5, 3, 8, 4, 5, 2, 1, 0]
    print(remove_duplicate_items(list3, True))  # [0, 1, 2, 3, 4, 5, 8, 9]


# ex128: Crie uma agenda que armazena o nome da pessoa, ID da pessoa, número do telefone, idade. Sua agenda deve possibilitar:
# (1) – inserir um contato
# (2) – Remover um contato
# (3) – buscar um contato pelo Código.

def mostrar():
    print('Cadastrados'.center(50, '-'))
    for elemento in agenda:
        print(elemento)

agenda = []

while True:
    menu = int(input('Digite o menu:\n1: Inserir um contato\n2: Remover um contato\n3: Ver um contato\n4: Sair\n'))
    while menu < 0 or menu > 4:
        menu = int(input('Opção inválida. Digite novamente:\n1: Inserir um contato\n2: Remover um contato\n3: Ver um contato\n4: Sair\n'))

    if menu == 1:
        nome = input('Digite o nome da pessoa: ').strip().title()
        codigo = len(agenda) + 1

        for elemento in agenda:
            while elemento[1] == codigo:
                codigo = int(input('Este código já existe. Digite novamente: '))
        telefone = int(input('Digite o telefone da pessoa: '))
        idade = int(input('Digite a idade da pessoa: '))
        agenda.append([codigo, nome, telefone, idade])

    elif menu == 2:
        mostrar()

        remover = int(input('Digite o código que quer remover: '))
        for elemento in agenda:
            if elemento[0] == remover:
                print(f'Usuário {elemento[1]} com o ID de {elemento[0]} removido com sucesso.')
                agenda.remove(elemento)

    elif menu == 3:
        mostrar()

        buscar = int(input('Digite um contato pelo seu código (ID): '))
        for elemento in agenda:
            if elemento[0] == buscar:
                print(f"O nome da pessoa é {elemento[1]}, possui o ID {elemento[0]}, tem o telefone {elemento[2]} e tem {elemento[3]} anos.")
        else:
            if elemento[0] != buscar:
                print('Não foi possível identificar este usuário.')

    elif menu == 4:
        break


# ex129: Compactador RLE (Run-Length Encoding: "AAABBBCC" → "A3B3C2").

def compactador_RLE(string: str):
    if len(string) < 0:
        return "A frase deve ter mais de um caractere."

    if not string.isalpha():
        return "A frase deve conter somente letras do alfabeto, sem espaços."

    caracteres = []
    RLE = ""

    for letra in string:
        if letra not in caracteres:
            caracteres.append(letra)
            RLE += f"{letra}{string.count(letra)}"

    return f"Resultado do RLE: {RLE}"


print(compactador_RLE("compactadorRLE"))  # c2o2m1p1a2t1d1r1R1L1E1
print(compactador_RLE("Pyyyyyyyyyyyyython"))  # Resultado do RLE: P1y13t1h1o1n1
print(compactador_RLE("aaaaaaa"))  # Resultado do RLE: a7

