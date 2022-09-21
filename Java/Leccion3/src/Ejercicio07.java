import java.util.Scanner;

public class Ejercicio07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 7: Pedir numero hasta que se introduzca uno negativo y calcular la media.

        int numero, contador = 0, media = 0, acumulador = 0;
        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            contador ++;
            acumulador = acumulador + numero;
        }while(numero >= 0);
        media = acumulador / contador;
        System.out.println("La media es: "+media);
    }
}
