$(document).ready(function()
{

	$("#login").submit(function(event)
	{
		event.preventDefault();


		var usuari = $("#usuari").val();
		var password = $("#password").val();
		// Checking for blank fields.
		if( usuari =='' || password =='')
		{
			$('input[type="text"],input[type="password"]').css("border","2px solid red");
			$('input[type="text"],input[type="password"]').css("box-shadow","0 0 3px red");
			$('#error-login').show();
		}
		/*else
		{
			$.post("libraries_php/login.php", { usuari1: usuari, password1:password},

				function(data)
				{
					if(data == false)
					{
						$('#password').css({"border":"2px solid red","box-shadow":"0 0 3px red"});
						$('#usuari').css({"border":"2px solid red","box-shadow":"0 0 3px red"});
						$('#error-login').show();

					}
					else if(data == true)
					{
						$('input[type="text"],input[type="password"]').css({"border":"2px solid #00F5FF","box-shadow":"0 0 5px #00F5FF"});
						$('#login').attr('type', 'submit');
						//document.location.href = "libraries_php/as.php?login=" + usuari + "&pass=" + password + "&";
						$('#error-login').hide();
						$("#login").unbind('submit').submit();
					}
					else
					{
						$('#error-login').show();
					}

				});
		}*/
	});
});