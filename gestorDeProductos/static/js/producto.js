$ (function()
{   
    let numeros = '1234567890';
	let letras  = 'qwertyuiopasdfghjklñzxcvbnm' +
				'QWERTYUIOPASDFGHJKLÑZXCVBNM' +
                'ÁÉÍÓÚáéíóú- ';
    let digito = '123456789Kk';
    
    
    $('.btnGrabar').click(function()//evento que se ejecuta al hacer click en el boton indicado(en este caso es btnEnviar del formularo en login.html)
    {  
        //alert('Click realizado');
  
        if($('.cmbMarca').val()=="")//validación de input vacío
        {
            alert('No especificó Marca');
            $('.cmbMarca').focus();//focus al input mail luego del mensaje
            return false;//para que deje de ejecutar el codigo luego del mensaje
        }

         //Expresion regular para validar correo, si empieza con letra o numero, luego arroba y lego letra o numero, luego punto letra o numero
         let emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.([a-zA-Z]{2,4})+$/
         if(!emailRegex.test($('.txtMail').val()))
         {
             alert('Email no Válido');
             return false;
         }

        if($('.txtNombre').val()=="")//validación de input vacío
        {
            alert('No especificó la contraseña');
            $('.txtPass').focus();//focus al input contraseña luego del mensaje
            return false;//para que deje de ejecutar el codigo luego del mensaje
        }

        if($('.imagen').val()=="")//validación de input vacío
        {
            alert('Seleccione una imagen');

            return false;//para que deje de ejecutar el codigo luego del mensaje
        }
        
       
        
        

    });
    
})
      