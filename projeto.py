#1.
'''
Crie uma variavel para armazenar o nome e a quantidade de experiência (XP) de um heróio, depois
utilize uma estrutura de decisão para apresentar alguma das mensagens abaixo

Se XP for menor ou igual que 1.000 = Ferro
Se XP for entre 1.001 e 2.000 = Bronze
Se XP for entre 2.001 e 5.000 = Prata
Se XP for entre 6.001 e 7.000 = Ouro
Se XP for entre 7.001 e 8.000 = Platina
Se XP for entre 8.001 e 9.000 = Ascendente
Se XP for entre 9.001 e 10.000 = Imortal
Se XP for maior ou igual a 10.001 = Radiante

Ao final deve se exibir uma mensagem:
"O Herói de nome {nome_heroi} está no nível de {nível_heróio}
'''
#R1

nome_heroi = input('Qual o nome do seu personagem? ')
nivel_heroi = int(input(f'Qual o nível atual de {nome_heroi}? '))

if nivel_heroi <= 1000:
    elo = 'Ferro'
elif nivel_heroi <= 2000:
    elo = 'Bronze'
elif nivel_heroi <= 5000:
    elo = 'Prata'
elif nivel_heroi <= 7000:
    elo = 'Ouro'
elif nivel_heroi <= 8000:
    elo = 'Platina'
elif nivel_heroi <= 9000:
    elo = 'Ascendente'
elif nivel_heroi <= 10000:
    elo = 'Imortal'
elif nivel_heroi >= 10001:
    elo = 'Radiante'

print(f'O Herói de nome {nome_heroi} está no nível de {elo}')

#-------------------------------------------------------------------

#2
'''
Faça um algoritmo que leia os valores de A, B, C e em seguida 
imprima na tela a soma entre A e B, e mostre se a soma é menor que C.
'''
#R2

a = int(input('Qual o primeiro número? '))
b = int(input('Qual o segundo número? '))
c = int(input('Qual o terceiro número? '))

if a+b < c:
    print(f'A + B = {a+b}. Soma sendo menor que C.')
else:
    print(f'A + B = {a+b}.')

#-------------------------------------------------------------------

#3
'''
Faça um algoritmo para receber um número qualquer e imprimir na 
tela se o número é par ou ímpar, positivo ou negativo.
'''
#R3

x = int(input('Escreva um número: '))

if x % 2 == 0 and x >= 0:
    print('O número é par, e positivo')
elif x % 2 == 0 and x < 0:
    print('O número é par, e negativo')
elif x % 2 != 0 and x >= 0:
    print('O número é impar, e positivo')
elif x % 2 != 0 and x < 0:
    print('O número é impar, e negativo')

#-------------------------------------------------------------------

#4
'''
Faça um algoritmo que leia dois valores inteiros A e B, se os
valores de A e B forem iguais, deverá somar os dois valores,
caso contrário devera multiplicar A por B. Ao final de qualquer
um dos cálculos deve-se atribuir o resultado a uma variável C e

imprimir seu valor na tela.
'''
#R4

a = int(input('Insira o valor de "A": '))
b = int(input('Insira o valor de "B": '))

if a == b:
    c = a+b
    print(f'C = {c}')
else:
    c = a*b
    print(f'C = {c}')

#-------------------------------------------------------------------

#5
'''
Faça um algoritmo que leia o valor do salário mínimo e o valor do
salário de um usuário, calcule quantos salários mínimos esse 
usuário ganha e imprima na tela o resultado. (Base para o Salário mínimo R$ 1.293,20).
'''
#R5

SalarioMinimo = 1293.20
SalarioUsuario = float(input('Qual o valor do seu salário? '))

x = int(SalarioUsuario / SalarioMinimo)

print(f'O seu salário equivale a {x} vezes do salário mínimo')