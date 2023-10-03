import os

lista_numeros = []

while True:

    resultado = 0

    def multiplicacao(*args):
        total = 1
        for numero in args:
            total *= numero
        return total

    opcao = input('Selecione a opção:\n[d]igitar um número\n[l]ista de números\n[r]esultado da multiplicação\n').lower()

    if opcao not in 'dlr':
        os.system('cls')
        print('Opção inválida!')
        continue

    if opcao == 'd':
        os.system('cls')
        numero = input('Digite um número: ')
        numero_float = 0

        try:
            numero_float = float(numero)
            lista_numeros.append(numero_float)
        except ValueError:
            print('Digite um número válido!')

    if opcao == 'l':
        os.system('cls')
        print(lista_numeros)
        continue
    
    if opcao == 'r':
        os.system('cls')

        if len(lista_numeros) <= 1:
            print('IMPOSSÍVEL MULTIPLICAR! A lista possui SOMENTE UM ou NENHUM VALOR!')
            continue

        else:
            resultado = multiplicacao(*lista_numeros)
            print(f'O resultado da multiplicação é {resultado}.')
            continue
