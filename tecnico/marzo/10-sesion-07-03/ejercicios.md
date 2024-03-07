## escribir si el numero digitado es par o impar

### python

```py
while num == 0:
    try:
        num = float(input("Ingrese un número: "))
        if num % 2 == 0:
            print("El número ingresado es par")
        else:
            print("El número ingresado es impar")
    except ValueError:
        num = 0
        print("Error: Solo se pueden ingresar números")
        print("Por favor intentelo de nuevo")
```
