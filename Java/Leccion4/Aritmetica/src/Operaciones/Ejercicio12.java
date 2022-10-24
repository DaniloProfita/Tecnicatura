package Operaciones;

import java.util.Scanner;
/*
Ejercicio 12: Pedir un numero y calcular su factorial
Hacerlo con JOptionPane y Scanner
*/

public class Ejercicio12 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero = 0;
        do{
            System.out.println("Digite un numero mayor a 0: ");
            numero = Integer.parseInt(entrada.nextLine());
        }while(numero <= 0);
        
        int factorial = 1;
        for(int i = numero; i > 0; i--){
            factorial *= i;
        }
            
        System.out.println("El factorial de "+numero+" es: "+factorial);
    }
}