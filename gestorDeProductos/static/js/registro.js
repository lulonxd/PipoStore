$ (function()
{   
    //Esto se ejecuta al cargar la pagina
    // $ = selector para indicar el elemento que esta en la pagina
    // .val = obtener el valor que esta en la caja de texto
    // let = se utiliza para declarar variables 

    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú- ';
    let digito = '123456789Kk';
    

    //validacion solo letras en nombre
    $('.txtNombre').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)//compara tecla presionada(guardada en variable 'e' la cual se guarda en variable caracter) con caracteres en variable letras si no está no deja escribir caracteres
            return false; //indexOf compara y si no lo encuentra devuelve -1 por lo que al escribir un numero será menor a 0 por lo que retorna false por lo que no se dibuja en el input
    })
    

    //validacion solo letras en apellido
    $('.txtApellido').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(letras.indexOf(caracter) < 0)//compara tecla presionada(guardada en variable 'e' la cual se guarda en variable caracter) con caracteres en variable letras si no está no deja escribir caracteres
            return false; //indexOf compara y si no lo encuentra devuelve -1 por lo que al escribir un numero será menor a 0 por lo que retorna false por lo que no se dibuja en el input
    })





    $('.btnRegistrarse').click(function()//evento que se ejecuta al hacer click en el boton indicado(en este caso es btnEnviar del formularo en register.html)
    {  
        //Expresion regular para validar correo, si empieza con letra o numero, luego arroba y lego letra o numero, luego punto letra o numero
        let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/
        if(!emailRegex.test($('.txtCorreo').val()))
        {
            alert('Correo no Válido');
            $('.txtCorreo').focus();
            return;
        }

        //alerta usuario registrado
        alert("Usuario Registrado Correctamente");
    });
    
})