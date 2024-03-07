# Si el segundo número es negativo y el primer es impar imprimir el mayor de lo contrario el menor
num1 = 0
num2 = 0
bandera = True
while bandera == True:
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        if num2 < 0 and num1 % 2 != 0:
            if num1 > num2:
                print("El mayor es:", num1)
            else:
                print("El mayor es:", num2)
        else:
            if num1 < num2:
                print("El menor es:", num1)
            else:
                print("El menor es:", num2)
        bandera = False
    except ValueError:
        print("Error: Solo se pueden ingresar números")
        print("Por favor intentelo de nuevo")
