import javax.swing.JOptionPane;
public class Ciclos04 {
    public static void main(String[] args) {
        //Ejercicio 4: Pedir numeros hasta ingresar un negativo, y mostrar cuantos numeros se han introducido.

        int numero, contador = 0;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero >= 0) {
            JOptionPane.showMessageDialog(null, "El numero "+numero+" es positivo");
            contador++; 
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        }
        System.out.println("El programa a finalizado porque ingreso un numero negativo y la catidad de numeros positivos que ingreso fue: "+contador);
    }
}
