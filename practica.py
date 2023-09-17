'''Lista de alumnos y sus promedio de notas'''
def calcular_promedio(notas):
    total = sum(notas)
    promedio = total / len(notas)
    return promedio
datos = "Juan,98,87,89,90|Jose,90,43,20,40|Pedro,70,80,89,90|Alvaro,90,87,67,66|Anibal,88,76,90,45"
estudiantes = datos.split("|")
promedios = {}
for estudiante_info in estudiantes:
    estudiante_datos = estudiante_info.split(",")
    nombre = estudiante_datos[0]
    notas = [int(nota) for nota in estudiante_datos[1:]]
    promedio = calcular_promedio(notas)
    promedios[nombre] = promedio
with open("Promedio de notas.txt", "w") as archivo:
    archivo.write("Notas de los alumnos\n")
    archivo.write("-----------------------------------\n")
    for nombre, promedio in promedios.items():
        archivo.write(f"Alumno: {nombre}\n")
        archivo.write(f"Promedio: {promedio:.2f}\n")
        archivo.write("\n")
print("Notas de Promedios de los alumnos")
print("Quedaran guardados en el archivos de texto")
for nombre, promedio in promedios.items():
    print(f"alumnos: {nombre}")
    print(f"Promedio: {promedio:.2f}")