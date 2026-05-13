#Definição das variaveis
print("_"*20)
altura = float(input("sua altura: "))
peso = float(input("seu peso: "))
imc = peso / (altura * altura)
print(f"Seu imc é: {imc:.2f}")
#tabela de classificação de massa corporal
if imc < 18.5:
    print("A baixo do peso normal")
elif imc < 24.9:
    print("peso ideal")
elif imc < 25.0:
    print("Excesso de peso")
elif imc < 30.0:
    print("Obesidade classe I")
elif imc < 39.9:
    print('Obesidade Classe II')
# elif imc < 40:
#     print("Obesidade Classe III ")
else:
    print("obesidade classe III")
