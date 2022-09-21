#Leer 10 numero e imprimir cuantos son positivos, cuantos negativos y cuantos neutross.
conteo_positivo = 0
conteo_negativo = 0
conteo_neutro = 0
i = 1
for i in range (10):
    num = int(input("Ingrese un numero: "))
    if num == 0:
        conteo_neutro = conteo_neutro + 1
    elif num > 0:
        conteo_positivo = conteo_positivo + 1
    elif num < 0:
        conteo_negativo = conteo_negativo + 1

print("La cantidad de numeros positivos es: ", conteo_positivo)
print("La cantidad de numeros negativos es: ", conteo_negativo)
print("La cantidad de numeros neutros es: ", conteo_neutro)