package Operaciones;
import javax.swing.JOptionPane;
public class Ciclos09 {
    public static void main(String[] args) {
        //Ejercicio 9: Pedir el dia, mes y año de una fecha e indicar si la fecha es correcta. Suponiendo que todos los meses son de 30 dias.

        int dia = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int mes = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int anio = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        if((dia >= 0)&&(dia <= 30)){
            if((mes >= 0)&&(mes <= 12)){
                if((anio >= 0)&&(anio <= 2022)){
                    System.out.println("La fecha ingresada es: "+dia+"/"+mes+"/"+anio);
                }else{
                    System.out.println("Fecha incorrecta, año incorrecto");
                }
            }else {
                System.out.println("Fecha incorrecta, año incorrecto");
            }
        }else{
            System.out.println("Fecha incorrecta, año incorrecto");
        }
    }
}
