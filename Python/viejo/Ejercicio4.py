#Ejercicio etapas de la vida segun edad
edad = int(input("Ingrese su edad: "))
if edad >= 0 and edad <= 9:
    print(f'Tu edad es {edad}, la infancia es increible y bella')
elif edad >= 10 and edad <= 19:
    print(f'Tu edad es {edad}, tienes muchos cambios, mucho que estudiar')
elif edad >= 20 and edad <= 29:
    print(f'Tu edad es {edad}, amor y comienza el trabajo')
elif edad >= 30 and edad <= 39:
    print(f'Tu edad es {edad}, boca')
elif edad >= 40 and edad <= 49:
    print(f'Tu edad es {edad}, boca 2')
elif edad >= 50 and edad <= 59:
    print(f'Tu edad es {edad}, boca 3')
elif edad >= 60 and edad <= 69:
    print(f'Tu edad es {edad}, boca 4')
elif edad >= 70 and edad <= 79:
    print(f'Tu edad es {edad}, boca 5')
elif edad >= 80 and edad <= 89:
    print(f'Tu edad es {edad}, boca 6')
elif edad >= 90 and edad <= 99:
    print(f'Tu edad es {edad}, Mirtaaaaaaa')
else:
    print(f'El valor {edad}, no es valido para una edad')