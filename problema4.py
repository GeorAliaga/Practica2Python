lista_alumnos = []
n_alumnos = int(input("Ingrese la cantidad de alumnos: "))

for _ in range(n_alumnos):
    nombre_alumno = input("Ingrese el nombre del alumno: ")

    calificaciones = []

    for i in range(3):
        calificacion = float(input(f"Ingrese la calificación {i + 1} para {nombre_alumno}: "))
        calificaciones.append(calificacion)

    alumno = {
        "Alumno": nombre_alumno,
        "Notas": calificaciones
    }

    lista_alumnos.append(alumno)



print("\nListado completo de alumnos:")
for alumno in lista_alumnos:
    print(alumno)
