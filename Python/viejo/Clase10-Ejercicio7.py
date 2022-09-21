#Dadas las horas trabajadas de 5 personas y la tarifa de pago. Calcular el salario y la sumatoria de todos los salarios.

salario = 0
suma = 0
i = 1
for i in range(5):
    i += 1
    print("Salaraio del empleado ", i ,":")
    horas = int(input("Ingrese las horas trabajadas: "))
    tarifa = int(input("Digite la tarifa por hora: "))
    salario = horas * tarifa
    print("El salario es: $", salario)
    suma = suma + salario

print("La suma de todos los salarios es: ", suma)