#Suponga que se tiene un conjunto de calificaciones de un grupo de 10 alumnos.
#Realizar un algoritmo para calcular la calificacion promedio y calificacion mas baja de todo el grupo.
suma = 0
calificacion_baja = 999
for i in range(10):
    calificacion = int(input("Digite su calificacion: "))
    suma = suma + calificacion
    if calificacion < calificacion_baja:
        calificacion_baja = calificacion

calificacion_promedio = suma / 10
print("La calificacion promedio es: ", calificacion_promedio)
print("La calificacion mas baja es: ", calificacion_baja)