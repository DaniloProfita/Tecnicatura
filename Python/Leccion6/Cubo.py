class Cubo:
    """
    Crear la clase Cubo con los atributos, ancho, alto y profundidad,
    con un metodo calcular_volumen que tendra la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores.
    """

    def __init__(self, altura, ancho, profundidad):
        self.altura = altura
        self.ancho = ancho
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.altura * self.ancho * self.profundidad


altura = int(input('Ingrese la altura => '))
ancho = int(input('Ingrese la base => '))
profundidad = int(input('Ingrese la profundidad => '))
cubo = Cubo(altura, ancho, profundidad)
print(f'El area del cubo es: {cubo.calcular_volumen()}')
