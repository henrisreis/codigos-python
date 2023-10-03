import os

print('Tente adivinhar a palavra secreta!')
palavra = 'amor'
print(f'A palavra secreta tem {len(palavra)} letras.')
tentativas = 0
letras_acertadas = ''

while True:

    letra = input('Digite uma letra para tentar adivinhar a palavra: ').lower()
    tentativas += 1

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    if letra == ' ':
        print('Digite um caracter válido!')
        continue

    if letra.isdigit():
        print('Forneça apenas letras!')
        continue

    if letra in palavra:
        letras_acertadas += letra

    palavra_formada = ''

    for l in palavra:
        if l in letras_acertadas:
            palavra_formada += l
        else:
            palavra_formada += '*'

    print(f'Palavra secreta: {palavra_formada}.')

    if palavra_formada == palavra:
        os.system('clear')
        print('PARABÉNS! Você ganhou!')
        print(f'A palavra era {palavra}.')
        print(f'Foram feitas {tentativas} tentativas.')
        letras_acertadas = ''
        tentativas = 0
        break

    sair = input('Deseja sair? [s]im [n]ão: ').lower().startswith('s')

    if sair:
        break