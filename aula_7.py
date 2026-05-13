###########################################################################################################################
###########################################################################################################################
# ano_atual = 2026
# print("ALISTAMENTO MILITAR")
# ano_nasc = int(input("Ano de nascimento:"))
# idade = ano_atual - ano_nasc
# anos_faltando = 18 % idade
# ano_alistamento = ano_nasc + 18
# atraso = ano_atual - ano_alistamento
# print(f"sua idade é {idade}") 
# if idade < 18:
#     print(f"faltam {anos_faltando}anos até o alistamento")
# elif idade == 18:
#     print("Alistamento esse anos")
# else:
#     print(f"Já passaram {atraso} anos desde o alistamento obrigatório, você deveria ter se alistado em {ano_alistamento} ")
#####################################################################################################################################

# print("Questionário CNH")
# ano_atual = 2026
# ano_nasc = int(input("Ano de nascimento:"))
# idade = ano_atual - ano_nasc
# anos_faltando = 18 % idade
# print(f"Você tem {idade} anos")
# if idade < 18:
#     print(f"Você ainda não tem idade para dirigir, faltam {anos_faltando} até atingir a idade minima")
# elif idade <= 20:
#     print("Você tem idade para tirar a habilitação do tipo A e B")
# else:
#     print("Você tem a idade minima para tirar a habilitação profissional tipo C e D e E\n")
#     habilitado = int(input("Caso já possuia uma habilitação, fazem quantos anos desde que possui carteira A ou B: "))
#     if habilitado >=1:
#         print("Você pode tirar a carteira tipo C")
###########################################################################################################################
# contador = 90
# while contador < 100:
#     print("repetiu", contador,"vezes")
#     contador += 1 # enquanto o contador foi menor que 101 ele vai continuar a contar
# ######################################################
# num = int(input("Digite um numero ou 0 para encerrar: "))
# while num != 0:
#     num = int(input("Digite um numero ou 0 para encerrar: ")) 
# #####################################################################
# resposta = "S"
# while resposta == "S":
#     num = int(input("Digite um número: "))
#     resposta = input("Deseja continuar? (S/N)").upper()[0]
# print("FIM")
###########################################################################################################################
# r = "sim"
# while r == "sim":
#     num = int(input("digite um numero: "))
#     r = input("Deseja continuar? (Sim/não)").lower().strip()
# print("fim do programa")
###########################################################################################################################
# qtd_aluno = 0
# while qtd_aluno < 3:
#     qtd_aluno = qtd_aluno + 1
#     c = 1
#     frequencia = 75
#     soma = 0
#     while c<=4:
#         nota = float(input(f"Digite a {c} nota: "))
#         c = c+1
#         soma = soma + nota
#         media = soma/4       
#     print(f"a soma final é igual a {soma} e a media é {media:.2f}")

#     if media < 80:
#         print("recuperação")
#     elif media <=60:
#         print("intervenção")
#     else: 
#         print("aprovado")
# print("não há mais notas a serem emitidas")

while True:
    count = 1
    soma = 0
    while count<=4:
        nota = float(input(f"Digite a {count} nota: "))
        count = count+1
        soma = soma + nota
        media = soma/4       
    print(f"a soma final é igual a {soma} e a media é {media:.2f}")

    if media < 80:
        print("recuperação")
    elif media <=60:
        print("intervenção")
    else: 
        print("aprovado")
    ans = "sim"
    while ans == "sim":
     ans = input("Deseja continuar? (Sim/não)").lower().strip()
     break
print("não há mais notas a serem emitidas")
        