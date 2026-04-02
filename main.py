# importa as funções e o dicionário principal do sistema
from biblioteca import adicionar_livro, buscar_livro, listar_livros, biblioteca

# nome do sistema 
nome_biblioteca = 'Universo dos Livros'

# loop principal do programa(menu interativo)
while True:
    print(f'\n === {nome_biblioteca} ===')
    print('\n1 - ADICIONAR LIVRO')
    print('2 - BUSCAR LIVRO')
    print('3 - SAIR')
    print('4 - LISTAR LIVROS')

    # tratamento de erro para assegurar que o usuario vai digitar um número
    try:
        opcao = int(input('Escolhe uma opção: '))
    except ValueError:
        print('Informe um número válido!')
        continue


    # opcao 1: adiciona um novo livro
    if opcao == 1:
        livro_id = int(input('Informe o ID do livro: '))
        titulo = input('Informe o título: ')
        autor = input('Informe o autor: ')    

        adicionar_livro(biblioteca, livro_id, titulo, autor)

    # opcao 2: busca um livro pelo id
    elif opcao == 2:
        livro_id = int(input('Informe o ID do livro: '))
        buscar_livro(biblioteca, livro_id)

    # encerra o programa
    elif opcao == 3:
        print('Saindo do sistema...')    
        break
    
    # lista todos os livros
    elif opcao == 4:
        listar_livros(biblioteca)