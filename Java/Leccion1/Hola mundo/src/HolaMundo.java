// import java.util.Scanner;

public class HolaMundo {
    public static void main(String[] args) {
        //DECLARACION DE VARIABLES INT Y STRING
        /*System.out.println("Hola mundo desde Java");
        
        int variable = 10;
        System.out.println(variable);
        variable = 5;
        System.out.println(variable);
        
        //Tipo String
        String miVariableCadena = "Bienvenidos";
        System.out.println(miVariableCadena);
        miVariableCadena = "Sigamos adelante";
        System.out.println(miVariableCadena); */
     
        //Var - inferencia de tipos en Java
        /*var miVariableEntera2 = 10;
        var miVariableCadena2 = "Seguimos estudiando";
        System.out.println("miVariableEntera2 = "+ miVariableEntera2);
        System.out.println("miVariableCadena2 = "+ miVariableCadena2);
        //soutV + TAB y declara un print con la variable
        //Para ejecutar Shift + F6*/
        
        //Reglas para definir una variable en Java
        /*var usuario = "Osvaldo";
        var titulo = "Ingeniero";
        var union = titulo +" "+ usuario;
        System.out.println("union = " + union);
        
        var a = 8;
        var b = 4;
        //Suma porque la primer variable es un entero
        System.out.println(a + b);
        //En esta concatena porque la primer variable es un String
        System.out.println(usuario + a + b);
        //En este ejemplo no concatena porque da prioridad a los ()
        System.out.println(usuario + (a + b));
        
        
        //Ejercicio: Caracteres especiales con Java
        var nombre = "Natalia";
        System.out.println("Nueva linea: \n"+ nombre); 
        // \n   Es un salto de linea
        System.out.println("Tabulador: \t"+ nombre);
        // \t Tabulador
        System.out.println("Retroceso: \b"+ nombre);
        // \b Retroceso|Tambien puede borrar 
        System.out.println("Comillas simples: \'"+nombre+"\'");
        // \' Comillas simples, hay que concatenar
        System.out.println("Comillas dobles: \""+nombre+"\"");
        // \" Comillas dobles, hay que concatenar*/
        
        
        //Clase Scanner
        //Para importar la agregamos en la lampara de la izquierda
        /*Scanner entrada = new Scanner (System.in);
        System.out.println("Digite su nombre: ");
        var usuario2 = entrada.nextLine();
        System.out.println("usuario2 = " + usuario2);
        System.out.println("Escriba el titulo: ");
        var titulo2 = entrada.nextLine();
        System.out.println("Resultado: "+ titulo2 +" "+ usuario2);*/
        
        //Valores maximos y minimos que permiten los distintos tipos de variables
        /*byte numEnteroByte = 127;
        System.out.println("numEnteroByte = " + numEnteroByte);
        System.out.println("Valor minimo del Byte: " + Byte.MIN_VALUE);
        System.out.println("Valor maximo del Byte: " + Byte.MAX_VALUE);
        
        short numEnteroShort = 32767;
        System.out.println("numEnteroShort = " + numEnteroShort);
        System.out.println("Valor minimo del Short: " + Short.MIN_VALUE);
        System.out.println("Valor maximo del Short: " + Short.MAX_VALUE);
        
        int numEnteroInt = 2147483647;
        System.out.println("numEnteroInt = " + numEnteroInt);
        System.out.println("Valor minimo del Int: " + Integer.MIN_VALUE);
        System.out.println("Valor maximo del Int: " + Integer.MAX_VALUE);
        
        long numEnteroLong = 9223372036854775807L;
        System.out.println("numEnteroLong = " + numEnteroLong);
        System.out.println("Valor minimo del Long: " + Long.MIN_VALUE);
        System.out.println("Valor minimo del Long: " + Long.MAX_VALUE);*/
        
        /*float numFloat = 3.4028235E38F; //Tambien se puede (float)10.0;
        System.out.println("numFloat = " + numFloat);
        System.out.println("Valor minimo del Float: " + Float.MIN_VALUE);
        System.out.println("Valor maximo del Float: " + Float.MAX_VALUE);
        
        double numDouble = 1.7976931348623157E308D;
        System.out.println("numDouble = " + numDouble);
        System.out.println("El valor minimo de Double: " + Double.MIN_VALUE);
        System.out.println("El valor maximo de Double: " + Double.MAX_VALUE);*/
        
        //Inferencia de tipos var y tipos primitivos
        /*var numEntero = 20; //Las literales sin punto automaticamente son de tipos int
        System.out.println("numEntero = " + numEntero);
        var numFloat = 10.0F; //Automaticamente con el punto se transorma en un tipo double
        System.out.println("numFloat = " + numFloat);
        var numDouble = 10.0;
        System.out.println("numDouble = " + numDouble);*/
        
        /*//Tipos primitivos char
        char miVariableChar = 'a';
        System.out.println("miVariableChar = " + miVariableChar);
        
        char varCaracter = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter);
        char varCaracterDecimal = 36; //Valor decimal del juego de caracteres unicode
        System.out.println("varCaracterDecimal = " + varCaracterDecimal);
        char varCaracterSimbolo = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo);
        
        var varCaracter2 = '\u0024'; //Indicamos a Java la asignacion con el codigo unicode
        System.out.println("varCaracter = " + varCaracter2);
        var varCaracterDecimal2 = 36; //Valor entero y le asigna un tipo int
        System.out.println("varCaracterDecimal = " + varCaracterDecimal2);
        var varCaracterDecimal21 = (char)36; //
        System.out.println("varCaracterDecimal = " + varCaracterDecimal2);
        var varCaracterSimbolo2 = '$'; //Un caracter especial, podemos copiar y pegar desde unicode
        System.out.println("varCaracterSimbolo = " + varCaracterSimbolo2);
        
        int varEnteroChar = '$';
        System.out.println("varEnteroChar = " + varEnteroChar);
        int caracterChar = 'b';
        System.out.println("caracterChar = " + caracterChar);*/
        
        /*
        //Tipos primitivos tipos booleanos
        boolean varBool = true;
        System.out.println("varBool = " + varBool);
        if (varBool){
            System.out.println("La bandera es verde");
        }else {
            System.out.println("La bandera es roja");   
        }
        
        //Algoritmo: es mayor de edad?
        var edad = 30;//Literal, tener presente la inferencia de tipos
        //var adulto = edad >= 18;//Esta es una expresion booleana
        if (edad >= 18) {
            System.out.println("Eres mayor de edad");
        }else {
            System.out.println("Eres menor de edad");
        }*/
        
        /*//Conversion de tipos primitivos
        var edad = Integer.parseInt("20");
        System.out.println("edad = " + (edad+1));
        //var edad2 = "20";
        //System.out.println("edad2 = " + edad2);
        var valorPI = Double.parseDouble("3.1416");
        System.out.println("edad = " + edad);
        
        //Pedir un valor 
        var entrada = new Scanner (System.in);
        System.out.println("Digite su edad");
        edad = Integer.parseInt( entrada.nextLine() );
        System.out.println("edad= " + edad);*/
        
        /*//Conversion de tipos primitivos en Java Parte 2
        var edadTexto = String.valueOf(10);
        System.out.println("edadTexto = " + edadTexto);
        
        var fraseChar = "programadores".charAt(0);*/
        
        //var a = "A";
        //System.out.println(a);
        //a = "B";
        //System.out.println(b);
        
        
    }
}