package Operaciones;

import javax.swing.JOptionPane;
/*
Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con JOptionPane y Scanner
*/

public class Ciclos12 {
    public static void main(String[] args) {
        int numero = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero mayor a 0: "));
        }while(numero <= 0);
        
        int factorial = 1;
        for(int i = numero; i > 0; i--){
            factorial *= i;
        }
            
        JOptionPane.showMessageDialog(null, "El factorial de "+numero+" es: "+factorial);
    }
}