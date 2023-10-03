primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    resultado = f'{primeiro_valor} é maior do que {segundo_valor}.'
    print(resultado)
elif primeiro_valor == segundo_valor:
    print('Os valores fornecidos são iguais.')
else:
    resultado = f'{segundo_valor} é maior do que {primeiro_valor}.'
    print(resultado)    