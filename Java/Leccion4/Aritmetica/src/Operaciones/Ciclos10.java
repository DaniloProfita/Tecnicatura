package Operaciones;

import javax.swing.JOptionPane;

public class Ciclos10 {
    public static void main(String[] args) {
        int suma = 0;
        for(var i = 0; i < 10; i++){
            int numeros = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma = numeros + suma;
        }
        JOptionPane.showMessageDialog(null, "La suma de los diez numeros es: "+suma);
    }
}
