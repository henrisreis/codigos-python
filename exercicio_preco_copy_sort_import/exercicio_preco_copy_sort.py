# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy

from dados import produtos

# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

def criar_copia_profunda(lista):
    return copy.deepcopy(lista)

def ordena_preco(produto):
    return produto['preco']

novos_produtos = criar_copia_profunda(produtos)

novos_produtos = [
    {**novo_produto, 'preco': round(novo_produto['preco'] * 1.10, 2)}
    for novo_produto in novos_produtos
]

print(
    'A lista de produtos com o preço atualizado: ',
    *novos_produtos,
    sep='\n'
)

print()

produtos_ordenados_por_nome = criar_copia_profunda(produtos)
produtos_ordenados_por_nome.sort(
    key=lambda produto: produto['nome'], 
    reverse=True
)

print(
    'A lista de produtos com seus nomes ordenados de maneira descrescente: ',
    *produtos_ordenados_por_nome,
    sep='\n'
)

print()

produtos_ordenados_por_preco = criar_copia_profunda(produtos)
produtos_ordenados_por_preco.sort(key=ordena_preco)

print(
    'A lista de produtos com seus preços ordenados de maneira crescente: ',
    *produtos_ordenados_por_preco,
    sep='\n'
)