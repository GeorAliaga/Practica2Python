def contar_digitos(numero, digito):
    numero_str = str(numero)

    cantidad = numero_str.count(str(digito))
    return cantidad


numero_ingresado = int(input("Numero ingresado: "))
digito_ingresado = int(input("Digito: "))



cantidad_veces = contar_digitos(numero_ingresado, digito_ingresado)
print(f"Cantidad de veces {digito_ingresado} en el numero: {cantidad_veces}")
