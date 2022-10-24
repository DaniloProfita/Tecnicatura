package Operaciones;

import javax.swing.JOptionPane;
/*
Ejercicio 11: Diseñar un programa que muestre el producto de los 10 primeros numeros impares
Hacerlo con JOptionPane
*/

public class Ciclos11 {
    public static void main(String[] args) {
        int producto = 1;
        for(int i = 1; i <= 20; i+=2){
            producto *= i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los primeros 10 numeros impares es: "+producto);
    }
}
