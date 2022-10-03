/*
    Proyecto caja:
    Ejercicio 1: Crear un proyecto segun las especificaciones mostradas a continuacion.
    La formular es: volumen=ancho * alto * profundidad
 */
package caja;
public class Caja {
    int ancho;
    int alto;
    int produndidad;

    public Caja(){}

    public Caja(int ancho, int alto, int produndidad){
        this.ancho = ancho;
        this.alto = alto;
        this.produndidad = produndidad;
    }

    public int formulaVolumen(){
        return ancho * alto * produndidad;
    }
}
