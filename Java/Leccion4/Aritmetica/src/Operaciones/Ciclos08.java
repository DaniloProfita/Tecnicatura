package Operaciones;
import javax.swing.JOptionPane;
public class Ciclos08 {
    public static void main(String[] args) {
        //Ejercicio 8: Pedir numero N, y mostrar todos los numeros del 1 al N.

        int n;
        n = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        for(var i = 0; i <= n; i++){
            System.out.println(i);
        }
    }
}
