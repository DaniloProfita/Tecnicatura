package test;

import dominio.Persona;

public class PersonaPrueba {
    public static void main(String[] args) {
        Persona persona1 = new Persona("Osvaldo", 57000, false);
        System.out.println("persona1 = " + persona1);
        System.out.println("persona1 su nombre es: "+persona1.getNombre());
        
        //Modificar a traves de los metodos
        persona1.setNombre("Juan Ignacio");
        //persona1.nombre = "Juan Ignacio" //Ya no se puede utilizar
        //System.out.println("Nombre es: "+persona1.nombre);//Error
        System.out.println("persona1 su nombre modificado es: "+persona1.getNombre());
        System.out.println("persona1 el resultado para el sueldo: "+persona1.getSueldo());
        System.out.println("persona1 para obtener el boolean: "+persona1.isEliminado());
        
        //Crear otro objeto de tipo Persona, asignar valores de manera inicial e imprimir
        //luego modificar sus valores y volver a imprimir
        Persona persona2 = new Persona("Danilo", 20000, false);
        System.out.println("valores de la persona2: "+persona2.getNombre()+" "+persona2.getSueldo()+" "+persona2.isEliminado());
        persona2.setNombre("Dano");
        persona2.setSueldo(90000);
        persona2.setEliminado(true);
        System.out.println("persona2 su nombre modificado es: "+persona2.getNombre());
        System.out.println("persona2 su sueldo modificado es: "+persona2.getSueldo());
        System.out.println("persona2 su boolean modificado es: "+persona2.isEliminado());
        
        System.out.println("persona1: "+persona1);
    }
}
