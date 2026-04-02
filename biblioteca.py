# dicionario que armazena os livros com o id como chave
biblioteca = {}

# função responsavel por adiciovar os livros ao dicionario
def adicionar_livro(biblioteca, livro_id, titulo, autor):

    # verifica se o id ja existe para evitar duplicidade
    if livro_id in biblioteca:
        print('Esse livro já existe!')

    # adicona o livro ao dicionario
    else:
        biblioteca[livro_id] ={
            "titulo": titulo,
            "autor": autor
    }
        print('Livro adicionado com sucesso! :)')


# função que busca o livro pelo id
def buscar_livro(biblioteca, livro_id):

    # verifica se o livro existe no dicionario 
    if livro_id in biblioteca:

        # recupera os dados do livro
        livro = biblioteca[livro_id]


        # exibe as informações formatadas
        print('=~' *12)
        print(f'ID: {livro_id}')
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print('=~' *12)
    else:
        print('Teu livro não foi encontrado! :(')


# funcao responsavel por listar todos os livros cadastrados
def listar_livros(biblioteca):
    # verifica se a biblioteca ta vazia
    if not biblioteca:
        print('=~' *14)
        print('Nenhum livro foi cadastrado')
        print('=~' *14)
    else:
        # percorre todos os livros e exibe suas informacoes
        for livro_id, livro in biblioteca.items():
            print(f"{livro_id} - {livro['titulo,']} {livro['autor']}")
