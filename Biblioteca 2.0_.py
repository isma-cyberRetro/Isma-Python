print("=================================")
print("        CADASTRAR LIVROS        ")
print("=================================")
print()

livros = []

while True:
    print("1 - Cadastrar livros")
    print("2 - Listar livros")
    print("3 - Pesquisar livro")
    print("4 - Excluir livro")
    print("5 - Quantidade de livros")
    print("6 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")

        