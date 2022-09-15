numero = int(input("Digite um número: "))

if (numero % 2 == 0) and (numero >= 100):
    print("Número par e maior que 100.")    
elif (numero % 2 == 0) and (numero < 100):
    print("Número par e menor que 100")
elif (numero % 2 != 0) and (numero < 100):
    print("Número impar e menor do que 100")
elif (numero % 2 != 0) and (numero >= 100):
    print("Número impar e maior do que 100.")