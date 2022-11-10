/*
Uso de la palabra Final
Esta palabra tiene diferentes significados dependiendo donde se aplique:
    Variables: Evita cambiar el valor que almacena la variable
    metodos: Evita que se modifique la definicion o el comportamiento de un metodo desde subclase(hija)
    clases: evita que se creen clases hijas
Otra caracteristica es que normalmente, cuando trabajamos con variables se combina
con el modificador de acceso estatico para convertir una variable en constante,
es decir que no se puede modificar su valor, por ejemplo de esto es la clase Math
en la cual todos sus atributos son de tipo static y final, es por esto que la variable
pi* se conoce como una constante
 */
package test;

import domain.Persona;

public class TestFinal {
    public static void main(String[] args) {
        final int miDni = 45678543;
        System.out.println("miDni = " + miDni);
        //miDni = 536356;
        //Persona.CONSTANTE_AQUI = 9;//nO SE MODIFICA
        System.out.println("Mi atributo constante es: "+Persona.CONSTANTE_AQUI);
        
        final Persona persona1 = new Persona();
        //persona 1 = new Persona(); //No se puede asignar una nueva refenrencia
        persona1.setNombre("Ariel Bentacud");
        System.out.println("persona1 nombre = " + persona1.getNombre());
        persona1.setNombre("Daniel Sam");
        System.out.println("persona1 nombre = " + persona1.getNombre());
    }
}
