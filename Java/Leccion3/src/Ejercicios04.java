import java.util.Scanner;
public class Ejercicios04 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 4: Pedir numeros hasta ingresar un negativo, y mostrar cuantos numeros se han introducido.

        int numero, contador = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero >= 0) {
        System.out.println("El numero "+numero+" es positivo");
        contador ++;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado porque ingreso un numero negativo y la catidad de numeros positivos que ingreso fue: "+contador);
    }
}
