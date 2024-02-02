def omitir_vocales(cadena):
    resultado = ""

    for caracter in cadena:
        if caracter.lower() not in ['a', 'e', 'i', 'o', 'u']:
            resultado += caracter

    return resultado

texto_ingresado = input("Ingrese una cadena de texto: ")

resultado_omitir_vocales = omitir_vocales(texto_ingresado)
print(f"Texto con vocales omitidas: {resultado_omitir_vocales}")
