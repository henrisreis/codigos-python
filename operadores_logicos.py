# entrada = input('[E]ntrar [S]air: ')
# senha_digitada = input('Senha: ')

# senha_permitida = '123456'

# if (entrada == 'E' or entrada == 'e') and senha_digitada == '123456':
#     print('Entrar')
# else:
#     print('Sair')

# Avaliação de curto-circuito
print(True and False and True)
print(0 or False or 0 or 'abc' or 'def')
senha = input('Senha: ') or 'Sem senha'
print(senha)