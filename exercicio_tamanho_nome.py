nome = input('Digite o seu nome: ')

nome_curto = len(nome) <= 4
nome_curto_txt = 'Seu nome é curto.'
nome_normal = len(nome) >= 5 and len(nome) <= 6
nome_normal_txt = 'Seu nome é normal.'
nome_grande = len(nome) > 6
nome_grande_txt = 'Seu nome é grande.'

if nome_curto:
    print(nome_curto_txt)

if nome_normal:
    print(nome_normal_txt)

if nome_grande:
    print(nome_grande_txt)