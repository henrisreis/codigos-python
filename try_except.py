numero = input('Digite um número a ser dobrado: ')
try:
    numero = float(numero)
    print(f'O dobro de {numero} é igual a {numero * 2: .2f}.')
except:
    print('Isso não é um número!')