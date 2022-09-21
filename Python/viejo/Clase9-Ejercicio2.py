#Calcular la suma de N primeros numeros
N_elementos = int(input("Digite la cantidad de numeros a sumarse"))
suma = 0
iterador = 0
for iterador in range(N_elementos):
    suma = suma + iterador
    print(suma)