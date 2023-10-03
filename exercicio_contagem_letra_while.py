frase = 'O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

i = 0
maior = 0
letra_maior = ''

while i < len(frase):
    
    letra_atual = frase[i]
    quantas_vezes_apareceu = frase.count(letra_atual)

    # if letra_atual != ' ':
    #     if quantas_vezes_apareceu > maior:
    #         maior = quantas_vezes_apareceu
    #         letra_maior = letra_atual

    # i += 1

    if letra_atual == " ":
        i += 1
        continue

    if quantas_vezes_apareceu > maior:
        maior = quantas_vezes_apareceu
        letra_maior = letra_atual
    
    i += 1

print(f'A letra {letra_maior} apareceu {maior} vezes.')