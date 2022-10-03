package Operaciones;

import java.util.Scanner;

public class Ejercicio10 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int suma = 0, numeros = 0;
        for(var i = 0; i < 10; i++){
            System.out.println("Digite un numero: ");
            numeros = Integer.parseInt(entrada.nextLine());
            suma = numeros + suma;
        }
        System.out.println("La suma de los diez numeros es: "+suma);
    }
}
