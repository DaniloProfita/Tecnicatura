package Operaciones;
public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10;//variable locales
        int b = 7;
        miMetodo();//llamamos al metodo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        aritmetica1.sumarNumeros();
        //int a = 10, se denomina memoria stack
        //Para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("Resultado con retorno= "+resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado con argumento= "+resultado);


        System.out.println("aritmetica 1 a:"+aritmetica1.a);
        System.out.println("aritmetica 1 b:"+aritmetica1.b);
        
        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica 2 a:"+aritmetica2.a);
        System.out.println("aritmetica 2 b:"+aritmetica2.b);
        // aritmetica1 = null; Nunca utilizar esto, no se debe hacer
        // System.gc();Metodo para limpiar residuos, no utilizar
    }
    public static void miMetodo() {
        //a = 10; la variable esta limitada
        System.out.println("Desde mi metodo");
    }
}
