"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

numero = input('Digite um número inteiro e saiba se é par ou ímpar: ')

if numero.isdigit(): # Método que verifica se a string é composta apenas de dígitos (números). Útil para saber se o usuário forneceu um número inteiro.

    numero = int(numero)
    numero_par = numero % 2 == 0

    if numero_par:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')

else:

    print('Você não digitou um número inteiro.')