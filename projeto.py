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