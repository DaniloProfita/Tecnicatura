class Rectangulo:
    """
    Crear una clase llamada Rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular_area utilizando la formula:
    area = base * altura. Pero la base y la altura deben ser ingresadas por el usuario y los objetos deben ser tres.
    """

    def __init__(self, altura, base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.altura * self.base


altura = int(input('\n Ingrese la altura => '))
base = int(input('\n Ingrese la base => '))
rectangulo = Rectangulo(altura, base)
print(f'\n El area del rectangulo es: {rectangulo.calcular_area()}')