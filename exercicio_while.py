nome = input('Digite o seu nome: ')

i = 0
novo_nome = '*'

while i < len(nome):
    novo_nome += nome[i] + '*'
    i += 1

print(novo_nome)