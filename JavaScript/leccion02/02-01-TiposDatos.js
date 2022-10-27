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

//Tipo de dato undefined
var x;
console.log(x);

x = undefined;
console.log(typeof x);

//null: significa ausencia de valor
var y = null;//null no es un tipo de dato, pero su origen es tipo object
console.log(typeof y);

//Tipo de dato array y Empty String
var autos = ['Citroen', 'Audi', 'BMW', 'Ford']
console.log(autos);
console.log(typeof autos);

var z = '';
console.log(z);//Cadena vacia
console.log(typeof z);//Cadena vacia
