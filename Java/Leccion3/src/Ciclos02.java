import javax.swing.JOptionPane;

public class Ciclos02 {
    public static void main(String[] args) {
        //Ejercicio 2: Leer numero e indicar si es positivo o negativo. El proceso se repetira hasta que se introduzca 0.

        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero > 0 || numero < 0) {
            if(numero > 0)
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es positivo");
            else
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es negativo");
        
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        System.out.println("El programa a finalizado porque ingreso 0");
    }
}
