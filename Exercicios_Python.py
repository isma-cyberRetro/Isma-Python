#1
nome_usuario = input("Digite seu nome de usuário: ")
print("1 - Indisponibilidade do Sistema.")
print("2 - Sistema funcionando, mas com lentidão ou erros.")
print("3 - Problemas que não impedem o trabalho.")
print("4 - Outros Problemas.")
tipo_problema = int(input("Descreva o problema encontrado: "))
tempo_problema = input("A quanto tempo você está com este problema em meses?: ")
if tipo_problema == 1:
    print("Nível do Problema: Critico!")
elif tipo_problema == 2:
    print("Nível do Problema: Alto!")
elif tipo_problema == 3:
    print("Nível do Problema: Médio!")
elif tipo_problema == 4:
    print("Nível do Problema: Baixo!")
else:
    print ("Opção Inválida!")