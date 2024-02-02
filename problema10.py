def convertir_fecha(fecha):
    meses = [
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    ]

    componentes = fecha.split()

    if len(componentes) == 3:  
        mes, dia, anio = componentes
    else:  
        mes, dia, anio = fecha.split('/')

    numero_mes = meses.index(mes) + 1


    fecha_formateada = f"{anio}-{numero_mes:02d}-{int(dia):02d}"

    return fecha_formateada

fecha_ingresada = input("Ingrese una fecha en formato mes-día-año: ")


fecha_convertida = convertir_fecha(fecha_ingresada)
print(f"Fecha convertida: {fecha_convertida}")
