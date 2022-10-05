//Tipos de datos en JS
/*Otro tipo de comentarios, pero de multiple lineas*/
var nombre = 'Arial';//Tipo Str
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.3;
console.log(typeof nombre);


var numero = 3000; //Tipo numero
console.log(numero);

var objeto = {
    nombre: "Ariel",
    apellido: "Bentacud",
    telefono: "123456"
};
console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(bandera);


//Tipo de dato funcion
function miFuncion(){}
console.log(typeof miFuncion)


//Tipo de dato symbol
var simbolo = Symbol("Mi símbolo");
console.log(typeof simbolo);

//Tipo de dato calse
class Persona{
    constructor(nombre, apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);