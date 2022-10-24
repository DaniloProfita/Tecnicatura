from Persona2 import Persona2
print('Creacion de objetos'.center(50, '-'))
#Esto es una comprobacion para saber de donde se esta ejecutando nuestro codigo
if __name__ == '__main__':
    persona5 = Persona2('Lionel', 'Messi', 35)
    persona5.mostrar_detalles()

    print(__name__)

print('Eliminacion de objetos'.center(50, '-'))#Centra el texto dentro de los caracteres que le pasamos, en este caso el (-)
del persona5