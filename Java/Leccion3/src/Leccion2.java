public class Leccion2 {
    public static void main(String[] args) {
        /*
        var condicion = false;
        if (condicion){
            System.out.println("Condicion verdadera");//Condicional simple
        }
        else{
            System.out.println("Condicion falsa");//Condicional doble
        }

        var numero = 2;
        var numeroTexto = "Numero desconocido";
        if (numero == 1){
            numeroTexto = "Numero uno";
        }
        else if (numero == 2){
            numeroTexto = "Numero dos";
        }
        else if (numero == 3){
            numeroTexto = "Numero tres";
        }
        else if (numero == 4){
            numeroTexto = "Numero cuatro";
        }
        else{
            numeroTexto = "Numero no encontrado";
        }

        System.out.println("numeroTexto = "+ numeroTexto);
        */

        var numero = 2;
        var numeroTexto = "Valor desconocido";
        switch(numero){
        case 1:
            numeroTexto = "Numero uno";
            break;
        case 2:
            numeroTexto = "Numero dos";
            break;
        case 3:
            numeroTexto = "Numero tres";
            break;
        case 4:
            numeroTexto = "Numero cuatro";
            break;
        default:
            numeroTexto = "Caso no encontrado";
        }

        System.out.println("numeroTexto = "+ numeroTexto);
        
    }
}
