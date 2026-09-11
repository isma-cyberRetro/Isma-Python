print("=================================")
print("      SISTEMA PARA BIBLIOTECA")
print("=================================")
print()

repeticoes = int(input("Quantas operações deseja realizar no menu? "))

saiu = False

for i in range(repeticoes):

    if saiu == False:

        print()
        print("=================================")
        print("      SISTEMA PARA BIBLIOTECA")
        print("=================================")
        print("1 - Cadastrar Livros")
        print("2 - Cadastrar Alunos")
        print("3 - Realizar Empréstimo")
        print("4 - Sair")
        print()

        opcao = input("Escolha uma opção: ")
        print()

        # ---------------- CADASTRO DE LIVROS ----------------
        if opcao == "1":
            qtd_livros = int(input("Quantos livros deseja cadastrar? "))
            print()

            for j in range(qtd_livros):
                print("----- LIVRO", j + 1, "-----")
                codigo = input("Código: ")
                titulo = input("Título: ")
                autor = input("Autor: ")
                ano = input("Ano: ")
                quantidade = input("Quantidade: ")
                print()

                titulo_valido = titulo != ""
                autor_valido = autor != ""
                ano_valido = ano.isdigit()
                quantidade_valida = quantidade.isdigit() and int(quantidade) > 0

                if titulo_valido and autor_valido and ano_valido and quantidade_valida:
                    print("Livro cadastrado com sucesso!")
                elif titulo_valido == False:
                    print("Erro: o título não pode ser vazio.")
                elif autor_valido == False:
                    print("Erro: o autor não pode ser vazio.")
                elif ano_valido == False:
                    print("Erro: o ano informado não é válido.")
                else:
                    print("Erro: a quantidade disponível deve ser maior que zero.")
                print()

        # ---------------- CADASTRO DE ALUNOS ----------------
        elif opcao == "2":
            qtd_alunos = int(input("Quantos alunos deseja cadastrar? "))
            print()

            for j in range(qtd_alunos):
                print("----- ALUNO", j + 1, "-----")
                matricula = input("Matrícula: ")
                nome = input("Nome: ")
                turma = input("Turma: ")
                print()

                matricula_valida = matricula.isdigit()
                nome_valido = nome != ""
                turma_valida = turma != ""

                if matricula_valida and nome_valido and turma_valida:
                    print("Aluno cadastrado com sucesso!")
                elif matricula_valida == False:
                    print("Erro: a matrícula deve ser informada corretamente.")
                elif nome_valido == False:
                    print("Erro: o nome não pode ser vazio.")
                else:
                    print("Erro: a turma não pode ser vazia.")
                print()

        # ---------------- REALIZAR EMPRÉSTIMO ----------------
        elif opcao == "3":
            print("----- EMPRÉSTIMO -----")
            print()

            codigo_livro = input("Código do livro: ")
            matricula_aluno = input("Matrícula do aluno: ")

            if codigo_livro == "" or matricula_aluno == "":
                print()
                print("Não é possível realizar o empréstimo.")
                print("Código do livro e matrícula são obrigatórios.")
            else:
                quantidade_disponivel = int(input("Quantidade disponível: "))
                print()

                if quantidade_disponivel > 0:
                    print("Empréstimo realizado com sucesso!")
                else:
                    print("Não é possível realizar o empréstimo.")
                    print("Não há exemplares disponíveis.")

        # ---------------- SAIR ----------------
        elif opcao == "4":
            print("Encerrando o sistema...")
            saiu = True

        # ---------------- OPÇÃO INVÁLIDA ----------------
        else:
            print("Opção inválida. Tente novamente.")

print()
print("Sistema encerrado.")
