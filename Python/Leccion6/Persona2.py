class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre;
        self._apellido = apellido;
        self._edad = edad;

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes: {self._nombre} {self._apellido} {self._edad}')

    @property  # decorador
    def nombre(self):  # Metodo Getter
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):  # Metodo setter
        self._nombre = nombre


    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Bentacud', 41)
    print(persona1.nombre)  # Llamamos al metodo getter
    persona1.nombre = 'Juan Pedro' #Llamamos al metodo setter
    print(persona1.nombre)#Otra vez con el metodo getter
    print(persona1.mostrar_detalles())#Llamamos el metodo mostrar_detalles

    #Atributo read-only seria cuando no tenemos el metodo set
    print(persona1.edad)

    #Crear tres objetos mas utilizando los metodos getter and setter para modificar y mostrar cambios
    persona2 = Persona2('Danilo', 'Profita', 80)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Dano'
    persona2.apellido = 'Profi'
    persona2.edad = 21
    print(persona2.mostrar_detalles())

    persona2 = Persona2('Daniel', 'Sam', 70)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Dani'
    persona2.apellido = 'S'
    persona2.edad = 30
    print(persona2.mostrar_detalles())

    persona2 = Persona2('Lautaro', 'Coutinho', 60)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Lau'
    persona2.apellido = 'Coity'
    persona2.edad = 40
    print(persona2.mostrar_detalles())

    print(__name__)