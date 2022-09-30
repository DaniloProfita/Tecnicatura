#Ejercicio 5: Convertidor de temperaturas
#Realizar dos funciones para convertir de grados celsius a fahrenheit y viseversa.
#Formular: (1 °C × 9/5) + 32 = 33.8 °F
def celsius_a_fahrenheit(celsius):
    return celsius * 5 / 9 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

celsius = float(input("Ingrese una temperatura en celsius: "))
fahrenheit = float(input("Ingrese una temperatura en fahrenheit: "))
resultado = celsius_a_fahrenheit(celsius)
resultado2 = fahrenheit_a_celsius(fahrenheit)
print(f'{celsius}°C son => {resultado:.2f}°F')
print(f'{resultado:.2f}°F son => {celsius}°C')