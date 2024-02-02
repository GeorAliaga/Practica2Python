n = []

while True:
    respuesta = input("¿Desea ingresar un numero? (Escriba SI o NO): ").upper()

    if respuesta != "SI":
        break  

    try:
        numero = int(input("Ingrese el numero: "))
        n.append(numero)
    except ValueError:
        print("Error, ingrese un numero valido.")


print("Numeros ingresados:", n)

cantidad_pares = sum(1 for num in n if num % 2 == 0)
cantidad_impares = len(n) - cantidad_pares

print("Cantidad de números pares:", cantidad_pares)
print("Cantidad de números impares:", cantidad_impares)