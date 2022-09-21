import javax.swing.JOptionPane;
public class Ciclos07 {
    public static void main(String[] args) {
        //Ejercicio 7: Pedir numero hasta que se introduzca uno negativo y calcular la media.

        int numero, contador = 0, media = 0, acumulador = 0;
        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            contador ++;
            acumulador = acumulador + numero;
        }while(numero >= 0);
        media = acumulador / contador;
        JOptionPane.showMessageDialog(null, "La media es: "+media);
    }
}
