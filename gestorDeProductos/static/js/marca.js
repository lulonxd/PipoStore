$ (function()
{   
    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú- ';
    let digito = '123456789Kk';
    
    //validacion solo letras en nombre
    $('.txtId').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })
    
})
      