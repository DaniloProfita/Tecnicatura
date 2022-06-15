nota = int(input("Ingrese el valor de una nota (0 al 10): "))
if nota == 10 or nota == 9:
    print("La calificacion es A")
elif nota == 8:
    print("La calificacion es B")
elif nota == 7:
    print("La calificacion es C")
elif nota == 6:
    print("La calificacion es D")
elif nota <= 5 and nota >= 0:
    print("La calificacion es F")
else:
    print(f'El valor {nota}, no es valido para una nota')