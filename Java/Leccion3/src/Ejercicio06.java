import java.util.Scanner;

public class Ejercicio06 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 6: Pedir numero hasta que se teclee un 0, mostrar la suma de todos los numeros introducidos.

        int numero, suma = 0;
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            suma = suma + numero;
        }while(numero != 0);
        System.out.println("La suma de todos los numeros ingresados es: "+suma);
    }
}
