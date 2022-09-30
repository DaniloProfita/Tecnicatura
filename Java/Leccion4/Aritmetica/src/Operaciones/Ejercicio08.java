package Operaciones;
import java.util.Scanner;

public class Ejercicio08 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 8: Pedir numero N, y mostrar todos los numeros del 1 al N.

        int n;
        System.out.println("Digite un numero: ");
        n = Integer.parseInt(entrada.nextLine());
        for(var i = 0; i <= n; i++){
            System.out.println(i);
        }
    }
}
