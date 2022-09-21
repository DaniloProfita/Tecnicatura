import java.util.Scanner;
public class Ejercicio03 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 3: Leer numeros hasta que se introduzca un cero, e indicar si es par o impar.

        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0) {
            if(numero % 2 == 0)
                System.out.println("El numero "+numero+" es par");
            else
                System.out.println("El numero "+numero+" es impar");
        
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado porque ingreso 0");
    }
}
