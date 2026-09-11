#1

print("=====  SUPORTE TÉCNICO - DEADSEC  =====")

nome_usuario = input("Digite seu nome de usuário: ")
print("1 - Indisponibilidade do Sistema.")
print("2 - Sistema funcionando, mas com lentidão ou erros.")
print("3 - Problemas que não impedem o trabalho.")
print("4 - Outros Problemas.")
tipo_problema = int(input("Descreva o problema encontrado: "))
tempo_problema = input("A quanto tempo você está com este problema em meses?: ")
if tipo_problema == 1:
    print("Nível do Problema: Critico!")
    descricao_problema = "Indisponibilidade do Sistema"
    nivel_problema = "Critico!"
elif tipo_problema == 2:
    print("Nível do Problema: Alto!")
    descricao_problema = "Sistema funcionando, mas com lentidão ou erros"
    nivel_problema = "Alto!"
elif tipo_problema == 3:
    print("Nível do Problema: Médio!")
    descricao_problema = "Problemas que não impedem o trabalho"
    nivel_problema = "Médio!"
elif tipo_problema == 4:
    print("Nível do Problema: Baixo!")
    descricao_problema = "Outros Problemas"
    nivel_problema = "Baixo!"
else:
    print ("Opção Inválida!")

print(f"{nome_usuario}, seu computador apresenta o tipo de problema {tipo_problema}, e recebe a descrição ''{descricao_problema}'', com nível de problema ''{nivel_problema}''. ")

#2
print("=====  LOJA DE INFORMÁTICA - DEADSEC  =====")

nome_produto = input("Qual ítem você procura?: ")
print("0 unidades - Prduto esgotado.")
print("1 a 5 unidades - Estoque crítico.")
print("6 a 20 unidades - Estoque Baixo.")
print("+20 unidades - Estoque Normal.")
quantidade_produto = int(input("Quantos ítens em estoque?: "))