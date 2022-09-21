import javax.swing.JOptionPane;
public class Ciclos05 {
    public static void main(String[] args) {
        //Ejercicio 5: Generar un numero aleatorio entre 0 y 100, luego ir pidiendo numeros indicando "es mayor" o "es menor", termina cuando se acierta y mostramos el numero de intentos.

        int numero, contador = 0, aleatorio;
        aleatorio = (int) (Math.random()*100);

        do{
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            contador ++;
            if(aleatorio > numero){
                JOptionPane.showMessageDialog(null, "Es mayor");
            }else if(aleatorio < numero){                
                JOptionPane.showMessageDialog(null, "Es menor");
            }else{
                JOptionPane.showMessageDialog(null, "Felicidades, adivinaste el numero!!");
            }
        }while(numero != aleatorio);
        JOptionPane.showMessageDialog(null, "Adivinaste el numero en: "+contador+" intentos");
    }
}
