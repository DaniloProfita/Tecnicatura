import java.util.Scanner;
public class Ejercicio05 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        //Ejercicio 5: Generar un numero aleatorio entre 0 y 100, luego ir pidiendo numeros indicando "es mayor" o "es menor", termina cuando se acierta y mostramos el numero de intentos.

        int numero, contador = 0, aleatorio;
        aleatorio = (int) (Math.random()*100);

        do{
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            contador ++;
            if(aleatorio > numero){
                System.out.println("Es mayor que "+numero);
            }else if(aleatorio < numero){                
                System.out.println("Es menor que "+numero);
            }else{
                System.out.println("Felicidades, adivinaste el numero!!");
            }
        }while(numero != aleatorio);
        System.out.println("Adivinaste el numero en: "+contador+" intentos");
    }
}
