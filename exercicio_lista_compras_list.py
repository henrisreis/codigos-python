import os

lista = []

while True:

    opcao = input('Selecione uma opção:\n[i]nserir [a]pagar [l]istar: ').lower()

    if len(opcao) > 1:
        os.system('cls')
        print('Digite apenas uma letra!')        
        continue

    if opcao not in 'ial':
        os.system('cls')
        print('Opção inválida!')
        continue

    if opcao == 'i':
        os.system('cls')
        item = input('Item: ')
        lista.append(item)
        continue

    if opcao == 'a':
        os.system('cls')

        if lista == []:
            os.system('cls')
            print('Não há nada para apagar!')
            continue

        indice = input('Índice do item a ser apagado: ')

        indice_int = 0

        try:
            indice_int = int(indice)
            lista.pop(indice_int)
        except TypeError:
            print('Digite um valor válido!')
        except ValueError:
            print('Digite um número inteiro!')    
        except IndexError:
            print('Índice não existe na lista!')
        except Exception:
            print('Erro desconhecido!')

    if opcao == 'l':
        os.system('cls')

        if lista == []:
            os.system('cls')
            print('Nada para listar!')
            continue

        print('ÍNDICE ITEM')
        
        for indice_listar, item_listar in enumerate(lista):
            print(indice_listar, item_listar)
        continue