while True:

    cpf_entrada = input('Forneça um número de CPF: ')
    cpf_inteiro = 0
    try:
        cpf_inteiro = int(cpf_entrada)
    except:
        print('O CPF deve conter apenas números!')

    if len(cpf_entrada) > 11:
        print('CPF inválido! Digite apenas 11 números!')
        continue

    lista_cpf = []
    for numero in cpf_entrada:
        lista_cpf.append(int(numero))
    
    lista_multiplicadores = []
    i = 10
    while i > 1:
        lista_multiplicadores.append(i)
        i -= 1
    
    lista_multiplicados = []
    for j in range(9):
        lista_multiplicados.append(lista_cpf[j] * lista_multiplicadores[j])
    
    resultado = ((sum(lista_multiplicados)) * 10) % 11
    penultimo_digito = 0
    if resultado <= 9:
        penultimo_digito = resultado
    
    print(f'O penúltimo digito do CPF é {penultimo_digito}.')