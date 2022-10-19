class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this en otros lenguajes
        print(f'La clase persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Dano', 'Profita', 31431445, 21)
#print(persona1.nombre)
#print(persona1.apellido)
#print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad} anios')

persona2 = Persona('Osvaldo', 'Giordanini', 23345245, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido}, su edad es: {persona2.edad} anios')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
persona1.edad = 40
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido}, su edad es: {persona1.edad} anios')

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle()#La referencia se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1)#Debemos pasar una referencia

persona1.telefono = '33344455'
print(persona1.telefono)

# print(persona2.telefono) no se puede porque no existe la persona 2 el atributo telefono

persona3 = Persona('Rogelio', 'Romero', 35789456, 22, 'Teléfono', '2614445557', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo=2021)
persona3.mostrar_detalle()
#print(persona3._dni)#Es una mala practica, no se debe utilizar
#persona3.__nombre #Esta totalmente encapsulado