mes = int(input("Ingrese un mes del año: "))
if mes >= 1 and mes <= 3:
    print(f'En el mes {mes}, es Verano')
elif mes >= 4 and mes <= 6:
    print(f'En el mes {mes}, es Otoño')
elif mes >= 7 and mes <= 9:
    print(f'En el mes {mes}, es Invierno')
else:
    print(f'En el mes {mes}, es Primavera')