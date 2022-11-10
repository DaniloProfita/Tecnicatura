//Ejercicio para encontrar numeros pares
let numero = 7;
if(numero % 2 == 0){
    console.log("Es un numero par");
} else {
    console.log("Es un numero impar");
}

//Ejercicio: es mayor de edad
let edad = 10;
if(edad > 18){
    console.log("Es mayor de edad");
} else {
    console.log("Es menor de edad");
}

//Ejercicio: dentro de un rango
let dentroRango = 5; //Aqui vamos ir cambiando el valor
let valMin = 0, valMax = 10;
if(dentroRango >= valMin && dentroRango <= valMax){
    console.log('Esta dentro del rango establecido')
}
else{
    console.log('Esta fuera del rango')
}