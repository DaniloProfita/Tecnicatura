import javax.swing.JOptionPane;
public class Ciclos06 {
    public static void main(String[] args) {
        //Ejercicio 6: Pedir numero hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos.

        int numero, acumulador = 0;

        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            acumulador = acumulador + numero;
        }while(numero != 0);
        JOptionPane.showMessageDialog(null, "La suma de todos los numeros ingresados es: "+acumulador);
    }
}
