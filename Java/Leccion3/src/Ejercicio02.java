import java.util.Scanner;

public class Ejercicio02 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 2: Leer numero e indicar si es positivo o negativo. El proceso se repetira hasta que se introduzca 0.

        int numero;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while(numero > 0 || numero < 0) {
            if(numero > 0)
                System.out.println("El numero "+numero+" es positivo");
            else
                System.out.println("El numero "+numero+" es negativo");
        
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa a finalizado porque ingreso 0");
    }
}
