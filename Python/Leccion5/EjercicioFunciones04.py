#Ejercicio 4: Calculadora de impuestos
# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcione el pago sin impuesto: 1000
# Proporcione el monto del impuesto: 21%
# Pago con impuesto: xxxx
def calcularImpuesto(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input("Ingrese el pago sin impuesto: "))
impuesto = float(input("Ingrese el monto del impuesto: "))
pago_con_impuesto = calcularImpuesto(pago_sin_impuesto, impuesto)
print(f'El pago con impuesto es: {pago_con_impuesto}')