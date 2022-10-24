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
        
        Persona persona = new Persona("Ariel", "Bentacud");
        System.out.println("persona = " + persona);
        System.out.println("Persona nombre: " + persona.nombre);
        System.out.println("Persona apellido: " + persona.apellido);
    }
    
    //Modularidad creamos un nuevo metodo
    public static void miMetodo() {
        //a = 10; la variable esta limitada
        System.out.println("Desde mi metodo");
    }
}

class Persona{
    String nombre;
    String apellido;
    
    Persona(String nombre, String apellido) { //Constructor
        super();//Llamada al constructor de la clase Padre Object
        Imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}

class Imprimir {
    public Imprimir() {
        super();//El constructor de la clase, para reservar memoria
    }
    
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: " + persona);
        System.out.println("Impresion del objeto actual (this):"+this);
    }
}