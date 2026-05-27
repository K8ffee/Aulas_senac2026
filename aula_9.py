# import time 
# for count in range(1,6):
#     print(f"{count} mississippi")
#     count +=1
#     time.sleep(1)
# # print("Ready or not, here I come!")
# import time
# for count in range(1,21):
#     print(f"repetiu {count} vezes")
#     time.sleep(0.5)
# print("Fim do programa de loops com for")
# import time
# for i in range(100,-1,-1):
#     time.sleep(0.10)
#     print(f"repetiu {i} vezes ")
# for count in range(1,5):
#     input(f"Informe a {count}º nota: ")

# while True:
#     password = input("youre stuck in a loop: ")
#     if password == "chupacabra":
#         break
# print("You've successfully left the loop.")
# import time 
# for i in range(1,11):
#     tabuada = 3 * i
#     time.sleep(1)
#     print(f"3 X {i} = {tabuada}")
# print("Adição")
# number = int(input("Escolha a tabuada de um número: "))
# for i in range(1, 11):
#     adc = number + i 
#     print(f"tabuada de {number} + {i} = {adc}")

# print ("subtração")
# number = int(input("Escolha a tabuada de um número: "))
# for i in range(1, 11):
#     sub = number - i 
#     print(f"tabuada de {number} - {i} = {sub}")
# print("divisão")
# number = int(input("Escolha um numero: "))
# for i in range(1, 11):
#     adc = number / i 
#     print(f"tabuada de {number} / {i} = {adc}")
# print("multiplicação")
# number = int(input("Escolha um numero: "))
# for i in range(1, 11):
#     adc = number * i 
#     print(f"tabuada de {number} * {i} = {adc}")

operador =""

import time 
while operador != "0":
    print("====== Tabuadas matemáticas ======\n")
    print("+  === Adição ===\n")
    print("-  === Subtração ===\n")
    print("*  === multiplicação ===\n")
    print("/  === Divisão ===\n")
    print("O  === Sair do Programa ===\n")

    operador = input("Digite um operador matemático: " )

    if operador == "+":

        print("Adição")
        number = int(input("Escolha a tabuada de um número: "))
        for i in range(1, 11):
            adc = number + i 
            print(f"tabuada de {number} + {i} = {adc}")
            time.sleep(.5)
    elif operador == "-":

        print ("subtração selecionado ")
        number = int(input("Escolha a tabuada de um número: "))
        for i in range(1, 11):
            sub = number - i
            print(f"tabuada de {number} - {i} = {sub}")
            time.sleep(.5)
    elif operador == "*":

        print("multiplicação selecionado")
        number = int(input("Escolha um numero: "))
        for i in range(1, 11):
            mult = number * i 
            print(f"tabuada de {number} * {i} = {mult}")
            time.sleep(.5)
    elif operador == "/":

        print("divisão")
        number = int(input("Escolha um numero: "))
        for i in range(1, 11):
            div = number / i 
            print(f"tabuada de {number} / {i} = {div:.2f}")
            time.sleep(.5)
    else:
        break
print("Fim do programa")

