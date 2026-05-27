
# option =""

# while option != "0":
#     print("====== MENU DE CADASTRO ======\n")
#     print("1 - === Cadastrar cliente ===\n")
#     print("2 - === listar cliente ===\n")
#     print("3 - === Editar cliente ===\n")
#     print("4 - === Excluir cliente ===\n")
#     print("O - === Sair do Programa ===\n")

#     option = input("Escolha uma opção: ")

#     if option == "1":
#         print("|==Novo Cadastro==|\n")
#         nome_cadastro = input("Digite seu nome: ")
#         email_cadastro = input("E-mail: ")
#         senha_cadastro = input("senha: ")
#         print("Cadastro finalizado")
#     elif option == "2":
#      print("|===Lista de cliente existente===|\n")
#     elif option == "3":
#         edit_cliente = input("Ensira o nome do cliente que deseja editar:")
        
#     elif option == "4":
#         print("|===Deseja excluir um cadastro de cliente? Sim/Não===|")
#         excluir = input(" ").lower().strip()
#         if excluir == "sim":
#             print("usuário excluido")
#         else:
#             print("Acão cancelada")
#     elif option == "0":
#         print("|===Fim do programa===|")

#     else:
#         print("|===Opção Invalida. Tente novamente===|\n")
        # break


####################################################################
# Sistema simples de cadastro de cliente
# Variáveis do cliente (inicialmente vazias)
nome_clientes = []
telefone_cadastrado = []

opcao = ""

while True:
    print("\n===== MENU CLIENTE =====")
    print("1 - Cadastrar cliente")
    print("2 - Listar cliente")
    print("3 - Editar cliente")
    print("4 - Excluir cliente")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n--- Cadastro de Cliente ---")
        nome = input("Digite o nome do cliente: ")
        Telefone = input("Digite o telefone: ")
        if nome == "":
            print("Inválido, espaço nome não pode ser vazio")
        else:
            nome_clientes.append(nome)
            telefone_cadastrado.append(Telefone)
            print("Cadastro concluido")
    elif opcao == "2":
        print("\n--- Listar Cliente ---")
        if len(nome_clientes) == 0:
            print("Nenhum nome cadastrado")
        else:
            for i in range(len(nome_clientes)):
                print(f" {i}Nome: {nome_clientes[i]} \n | Telefone: {telefone_cadastrado[i]}")    
    elif opcao == "3":
        print("\n--- Editar Cliente ---")
        if len(nome_clientes) ==0:
            print("Sem registro de cadastro para ser editado")
        else:
            for i in range(len(nome_clientes)):
                print(f"{i} - {nome_clientes[i]}")

            try:
                indice = int(input("Digite o número do cliente que deseja editar"))
                if indice < 0 or indice >= len(nome_clientes):
                    print("indice Inválido")
                else:
                    novo_nome = input("Novo Nome(Enter para manter: ")
                    novo_tel = input("Novo telefone(Enter para manter): ")

                    if novo_nome != "":
                        nome_clientes[indice] = novo_nome
                    if novo_tel != "":
                        telefone_cadastrado[indice] = novo_tel
                    print(" Cliente atualizado com sucesso!")
            except ValueError:
                print("Digite um número válido")
    elif opcao == "4":
        print("\n--- Excluir Cliente ---")
        if len((nome_clientes) == 0):
            print("Nenhum clientr para excluir")
        else:
            for i in range(len(nome_clientes)):
                    print(f"{i} - {nome_clientes[i]}")
            try:
                indice = int(input("Digite o npumeo do cliente que deseja excluir"))
                if indice < 0 or indice >= len(nome_clientes):
                    print("Indice inválido")
                else:
                    nome_clientes.pop(indice)
                    telefone_cadastrado.pop(indice)
                    print("Cliente excluído con sucesso")
            except ValueError:
                print("Digite um numero válido")

    elif opcao == "0":
        print("\nEncerrando o programa...")

    else:
        print("\n! Opção inválida. Tente novamente.")

    break



