package Operaciones;
public class PruebaAritmetica {
    public static void main(String[] args) {
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();

        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("Resultado con retorno= "+resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado con argumento= "+resultado);
    }
}
