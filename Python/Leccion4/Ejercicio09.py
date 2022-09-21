#Ejercicio 9: Mostrar una frase sin espacios y contar su longitud
#Ejemplo:       frase: vivir por siempre en paz
#               frase final = vivirporsiempreenpaz
#               N° de caracteres = 20

frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\n Frase final: {frase1}')
print(f'\n N° de caracteres: {len(frase1)}')