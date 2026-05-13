# nota = int(input("Ensira uma nota: "))
# if nota < 5:
#     print("Conceito D")
# elif nota <7:
#     print("conceito C")
# elif nota <9:
#     print ("conceito B")
# elif nota >=9:
#     print("Conceito A")
######################################
# nota = int(input("Ensira um número: "))
# if nota < 5:
#     print("Conceito D")
# elif nota >=5 and nota <7:
#     print("Conceito C")
# elif nota >= 7 and nota < 9:
#     print("Conceito B")
# elif nota >=9:
#     print("Conceito A")
#*****************************************************
valor_compra = float(input("Qual o valor da sua compra: "))
desconto_vip = 0.2
desconto_normal = 0.1

if valor_compra >=100:
    vip =input("a loja possui desconto para clientes VIP, você possui VIP: ")
    if vip == "s":
        desconto = valor_compra * desconto_vip
        valor_final = valor_compra - desconto
        print(f"O valor da compra {valor_compra} teve um desconto de {desconto}, valor final {valor_final}")
    elif vip == "n":
        desconto = valor_compra * desconto_normal/100
        valor_final = valor_compra - desconto 
        print(f"O valor da compra {valor_compra} teve um desconto de {desconto}, valor final {valor_final}")
else:
    print(f"não há desconto, valor da compra {valor_compra}")

    
    