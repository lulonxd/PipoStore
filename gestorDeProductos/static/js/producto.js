$ (function()
{   
    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú- ';
    let digito = '123456789Kk';
    
    $('.txtId').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })

    $('.txtStock').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })

    $('.txtPrecioCosto').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })

    $('.txtPrecioVenta').keypress(function(e)
    {
        let caracter = String.fromCharCode(e.which);
        if(numeros.indexOf(caracter) < 0)
            return false;
    })

    $('.btnGrabar').click(function()//evento que se ejecuta al hacer click en el boton indicado(en este caso es btnEnviar del formularo en login.html)
    {  


        if($('.imagen').val()=="")
        {
            alert('Seleccione una imagen');

            return false;//para que deje de ejecutar el codigo luego del mensaje
        }
        
       
        
        

    });
    
})
      