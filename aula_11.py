cliente = []
cadastro_cliente = []
while True:
    resposta = input("Deseja cadastrar um cliente? (S/N): ")
    if resposta == "N":
     break
    cliente.append(input("Digite o nome do cliente: "))
    cliente.append(int(input("Digite a idade do cliente: ")))
    cliente.append(input("Digite o telefone do cliente: "))
    cadastro_cliente.append(cliente[:])
    cliente.clear()
listar = input("Deseja listar os clientes cadastrados? (S/N): ")
if listar == "S":
    cadastro_cliente.sort()
    for cliente in cadastro_cliente:
        print("*"*20)
        print(f"Nome: {cliente[0]}")
        print(f"Telefone: {cliente[2]}")
        #################################################################################################
        produto = []
cadastro_produto = []
while True:
    resposta = input("Deseja cadastrar um produto (S/N): ")
    if resposta == "N":
        break
    print("Bem vindo a revender.com! por favor preencha as informações a seguir")
    produto.append(input("Nome do vendedor: "))
    produto.append(input("Nome do produto: "))
    produto.append(input("Classificação do produto: "))
    cadastro_produto.append(produto[:])
    produto.clear()
catalogo = input("Deseja exibir a lista de produtos? (S/N): ")
if catalogo == "S":
    cadastro_produto.sort()
    for produto in cadastro_produto:
        print("*"*20)
        print(f"Vendedor: {produto[0]} \n Produto: {produto[1]}\n Categoria {produto[2]}")