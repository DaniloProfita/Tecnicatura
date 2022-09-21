import javax.swing.JOptionPane;
public class Ciclos03 {
    public static void main(String[] args) {
        //Ejercicio 3: Leer numeros hasta que se introduzca un cero, e indicar si es par o impar.

        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0) {
            if(numero % 2 == 0)
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es par");
            else
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es impar");
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        System.out.println("El programa a finalizado porque ingreso 0");
    }
}
