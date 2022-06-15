import java.util.Scanner;

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
        
        var fraseChar = "programadores".charAt(4);
        System.out.println("fraseChar = " + fraseChar); 
        
        System.out.println("Digite un caracter: ");
        fraseChar = entrada.nextLine() .charAt(0);
        System.out.println("fraseChar = " + fraseChar);*/
        /*
        int num1 = 5, num2 = 4;
        var solucion = num1 + num2;
        System.out.println("solucion de la suma = " + solucion);
        
        solucion = num1 - num2;
        System.out.println("solucion de la resta = " + solucion);
        
        solucion = num1 * num2;
        System.out.println("solucion de la multiplicacion = " + solucion);
        
        solucion = num1 / num2;
        System.out.println("solucion de la division = " + solucion);
        
        var solucion2 = 3.4 / num2;
        System.out.println("solucion2 de la divicion 2 = " + solucion2);
        
        solucion = num1 % num2; // Guarda el residuo entero de la division
        System.out.println("solucion residuo de la division = " + solucion);
        
        if (num1 % 2 == 0)
            System.out.println("Es un numero Par");
        else
            System.out.println("Es un numero Impar");
        */
        /*
        int varNum1 = 1, varNum2 = 4;
        int varNum3 = varNum1 + 6 - varNum2;
        System.out.println("varNum3 = " + varNum3);
        
        // +=   -=  *=  /=  %=
        varNum1 += 1; // varNum1 = varNum1 + 1;
        System.out.println("varNum1 = " + varNum1);
        
        varNum2 -= 2;
        System.out.println("varNum2 = " + varNum2);
        varNum1 *= 5;
        System.out.println("varNum1 = " + varNum1);
        varNum3 /= 4;
        System.out.println("varNum3 = " + varNum3);
        varNum1 %= 6;
        System.out.println("varNum1 = " + varNum1);
        */
        /*
        //Operadores Unarios: Cambio de Signo
        var varA = 7;
        var varB = -varA;
        System.out.println("varA = " + varA);
        System.out.println("varB = " + varB);//El resultado sera un numero negativo
        
        //Operadores de Negacion
        var varC = true;//Esta literal por default en Java es de tipo boolean
        var varD = !varC; //Aqui esta invirtiendo el valor
        System.out.println("varC = " + varC);
        System.out.println("varD = " + varD);
        
        //Operadores Unarios de Incremento: Preincremento
        var varE = 9;//Se va a modificar su valor
        var varF = ++varE;//Simbolo antes de la variable
        //Primero se incrementa la variable y despues se usa su valor
        System.out.println("varE = " + varE);//Se incrementa en la unidad
        System.out.println("varF = " + varF);//Va a sumar uno
        
        //Postincremento (el simbolo va despues de la variable)
        var varG = 3;
        var varH = varG++;//Primero el valor de la variable, luego el incremento
        System.out.println("varG = " + varG);
        System.out.println("varH = " + varH);
        
        //Operadores Unarios de decremento
        var varI = 4;
        var varJ = --varI;
        System.out.println("varI = " + varI);//La variable ya esta con decremento
        System.out.println("varJ = " + varJ);
        
        //Postdecremento
        var varK = 8;
        var varL = varK--;//Primero el valor de la variable, luego queda el decremento
        System.out.println("varK = " + varK);
        System.out.println("varL = " + varL);
        */
        /*
        //Operadores de Igualdad y Relacionales
        var aNum = 5;
        var bNum = 4;
        var cNum = (aNum == bNum);
        System.out.println("cNum = " + cNum);
        
        var dNum = aNum != bNum;
        System.out.println("dNum = " + dNum);
        
        var cadenaA = "Hello";
        var cadenaB = "Hello";
        var cVar = cadenaA == cadenaB;
        System.out.println("cVar = " + cVar);
        
        var fVar = cadenaA.equals(cadenaB);
        System.out.println("fVar = " + fVar);
        
        var gVar = aNum >= bNum;//> >= < <= == !=
        System.out.println("gVar = " + gVar);
        
        if(aNum % 2 == 0)
            System.out.println("El numero es Par");
        else
            System.out.println("El numero es Impar");
        
        var edad = 30;
        var adulto = 18;
        if(edad >= adulto)
            System.out.println("Es mayor de edad");
        else
            System.out.println("Es menor de edad");
        */
        /*
        //Operadores condicionales And & Or
        var valorA = 7;
        var valorMinimo = 0;//Rango del 0 al 10
        var valorMaximo = 10;
        var respuesta = valorA >= 0 && valorA <= 10;
        
        if (respuesta)
            System.out.println("Esta dentro del rango establecido");
        else
            System.out.println("Esta fuera del rango establecido");
        
        var vacaciones = false;
        var diaLibre = false;
        if(vacaciones || diaLibre)
            System.out.println("Papa puede asistir al juego de su hijo");
        else
            System.out.println("Papa no puede asistir al juego de su hijo");
        */
        /*
        //Operador Ternario
        var resultadoT = (5 > 4) ? "Verdadero" : "Falso";
        System.out.println("resultadoT = " + resultadoT);
        
        var numeroT = 7;
        resultadoT = (numeroT % 2 == 0) ? "Par" : "Impar";
        System.out.println("resultadoT = " + resultadoT);
        */
        
        var x = 5;
        var y = 10;
        var z = ++x + y--;
        System.out.println("x = " + x);//6
        System.out.println("y = " + y);//9
        System.out.println("z = " + z);//16
        
        var solucionAritmetica = 4 + 5 * 6 / 3;
        System.out.println("solucionAritmetica = " + solucionAritmetica);
        
        solucionAritmetica = (4 + 5) * 6 / 3;
        
        
    }
}