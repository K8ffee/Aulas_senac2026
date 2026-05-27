# nomes = ["Ana","Carlos","Mariana","João"]
# print(f"Primeiro cliente foi {nomes[3]}")
# nomes.append("lucas")
# print(nomes)
# nomes[1] = "pedro"
# print(nomes)
# nomes.pop(3)
# print(nomes)
# produtors =["arroz",'feijãao',"macarrão" ]
# tarefas = ["estudar pythom","fazer exercicios","revisar aulas"]
# print(produtors[1])
# produtors.append("Açucar")
# print(produtors)
# produtors.insert(2,"Café")
# print(produtors)
# atividades = produtors + tarefas
# produtors.extend(tarefas)
# print("produtos:", produtors)
# print("tarefas:", tarefas)
# atividades.clear()
# print(atividades)

# import time
# from random import randint
# numbers = []
# for num in range(6):
#     numbers.append(randint(1,21))
#     print(numbers)
#     for num in numbers:
#      print(f"numero aleatorio {num}")

#     for num in range(len(numbers)):
#      print(f"{num+1}º numero aleatorio : {numbers[num]}")
    
# print(sum(numbers))
# print(f"A soma dos numeros: {sum(numbers)}")
# print(f"O maior numero: {max(numbers)}")
# print(f"O menor numero:{min(numbers)}")

# cliente = []
# print("informe o nome e telefone:")
# for clientes in range(2):
#     cliente.append(input())

# print(f"Cliente:{cliente[0]}")
# print(f"Telefone:{cliente[1]}")
# cadastro_clientes = []
# cadastro_clientes.append(clientes[:])
# print(f"Lista de cadastro de clientes:", cadastro_clientes)
# cliente.clear()
# print("informe o nome e telefone:")
# for clientes in range(2):
#     cliente.append(input())

# print(f"Cliente:{cliente[0]}")
# print(f"Telefone:{cliente[1]}")

# cadastro_clientes = []
# cadastro_clientes.append(cliente)
# print(f"Lista de cadastro de clientes:", cadastro_clientes)



#exemplo 2 com copy
clientes = []
print("Informe seu nome e telefone")
for cliente in range(2):
    clientes.append(input())

print(f"Cliente: {clientes[0]}")
print(f"telefone: {clientes[1]}")
print("Ação 1 - Lista de clientes:", clientes)
cadastro_clientes = []
cadastro_clientes = clientes.copy()
print(f"Lista Cadastro de CLiente:",cadastro_clientes)
print(f"Ação 2 - Lista Clientes {clientes}")
print("informe nome e telefone")
