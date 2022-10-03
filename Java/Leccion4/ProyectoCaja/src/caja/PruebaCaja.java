package caja;
public class PruebaCaja {
    public static void main(String[] args) {
        Caja caja1 = new Caja();
        caja1.ancho = 3;
        caja1.alto = 2;
        caja1.produndidad = 6;
        int resultado = caja1.formulaVolumen();
        System.out.println("Volumen de caja 1: "+resultado);

        Caja caja2 = new Caja(2, 4, 6);
        System.out.println("Volumen de caja 2: "+caja2.formulaVolumen());
    }
    
}
