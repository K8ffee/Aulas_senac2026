
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
#         break

#definir senha com 3 tentativas
senha = "Admin123" 
num_tentativas = 0

while num_tentativas < 3:
    senha = input("Senha: ")
    if senha == "Admin123":
     print("entrada permitida")
    elif senha != "Admin123":
        print("tente novamente")
    num_tentativas = num_tentativas +1
else:
    print("SEM MAIS TENTATIVAS")
