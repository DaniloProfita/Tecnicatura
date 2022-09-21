#Calcular el factorial de un numero mayor o igual a 0.
i = 0
fact = 1

num = int(input("Ingrese un numero mayor a 0: "))
if (num >= 0):
    for i in range(1, num+1):
        fact *= i
        
    print("El factorial de ", num, " es: ",fact)
else:
    print('El numero es menor a 0')
