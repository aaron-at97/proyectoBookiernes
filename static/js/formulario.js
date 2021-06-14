$(document).ready(function () {
    var usrtrue = false;
    var mailtrue = false;
    var cptrue = false;

    $("#comprobar_todo").click(function () {
        comprobar_nombre();
        comprobar_contraseña();
        comprobar_apellido();
        comprobar_direccion();
        comprobar_cp();
        comprobar_telefono();
        comprobar_dni();
        comprobar_usuario();
        comprobar_correo();
        if (comprobar_nombre() && comprobar_contraseña() && comprobar_apellido() && comprobar_direccion() && comprobar_telefono() && comprobar_dni() && usrtrue && mailtrue && cptrue) {
            return true;
        } else {

            document.getElementById("register-error").innerHTML = "Datos mal introducidos, compruebe sus datos";
            return false;
        }
    });

//Miramos si el usuario existe en la base de datos y si esta correctamente rellenado.
    function comprobar_usuario() {
        usuario_existente = true;
        usuario = document.getElementById("register-user").value;
        var xmlhttp = null;
        if (usuario.length < 3) {
            document.getElementById("register-user-error").innerHTML = "Debe contener mínimo 3 caracteres";
            $("#register-user").css("border-color", "red");
            usrtrue = false;
            return false;
        } else {
            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            } else {
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.onreadystatechange = function () {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    usuario_existente = xmlhttp.responseText;
                    if (usuario_existente == true) {
                        document.getElementById("register-user-error").innerHTML = "Este nombre de usuario ya existe";
                        $("#register-user").css("border-color", "red");
                        usrtrue = false;
                        return false;
                    } else {
                        document.getElementById("register-user-error").innerHTML = "";
                        $("#register-user").css("border-color", "green");
                        usrtrue = true;
                        return true;
                    }
                }
            }
            xmlhttp.open('POST', "libraries_php/comprobarUsuario.php", true);
            xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xmlhttp.send("usuario=" + usuario);
        }
    }

//Comprobamos el correo
    function comprobar_correo() {
        correo_existe = true;
        correoRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
        correo = document.getElementById("register-email").value;
        var xmlhttp = null;
        if ((correoRegex.test(correo) == false)) {
            document.getElementById("register-email-error").innerHTML = "Email incorrecto, formato no válido";
            $("#register-email").css("border-color", "red");
            mailtrue = false;
            return false;
        } else {
            if (window.XMLHttpRequest) {
                xmlhttp = new XMLHttpRequest();
            } else {
                xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
            }
            xmlhttp.onreadystatechange = function () {
                if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
                    correo_existe = xmlhttp.responseText;
                    if (correo_existe == true) {
                        document.getElementById("register-email-error").innerHTML = "Este email ya esta registrado";
                        $("#register-email").css("border-color", "red");
                        mailtrue = false;
                        return false;
                    } else {
                        document.getElementById("register-email-error").innerHTML = "";
                        $("#register-email").css("border-color", "green");
                        mailtrue = true;
                        return true;
                    }
                }
            }
            xmlhttp.open('POST', "libraries_php/comprobarCorreo.php", true);
            xmlhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
            xmlhttp.send("correo=" + correo);
        }
    }

//Comprobamos que ambas contraseñas coincidan
    function comprobar_contraseña() {
        passwd = document.getElementById("register-password").value;
        passwd1 = document.getElementById("register-password-repeat").value;
        if (passwd != passwd1) {
            document.getElementById("register-password-error").innerHTML = "Contraseñas no coinciden.";
            $("#register-password-repeat").css("border-color", "red");
            $("#register-password").css("border-color", "red");
            return false;
        } else if (passwd.length < 8) {
            document.getElementById("register-password-error").innerHTML = "La contraseña tiene que contener mínimo 8 caracteres.";
            $("#register-password-repeat").css("border-color", "red");
            $("#register-password").css("border-color", "red");
        } else {
            document.getElementById("register-password-error").innerHTML = "";
            $("#register-password-repeat").css("border-color", "green");
            $("#register-password").css("border-color", "green");
            return true;
        }
    }

//Comprobamos nombre
    function comprobar_nombre() {
        nombre = document.getElementById("register-first-name").value;
        if (nombre.length == 0) {
            document.getElementById("register-first-name-error").innerHTML = "¿Cómo te llamas?";
            $("#register-first-name").css("border-color", "red");
            return false;
        } else {
            document.getElementById("register-first-name-error").innerHTML = "";
            $("#register-first-name").css("border-color", "green");
            return true;
        }
    }

//Comprobamos apellido
    function comprobar_apellido() {
        apellido = document.getElementById("register-last-name").value;
        if (apellido.length == 0) {
            document.getElementById("register-last-name-error").innerHTML = "Escriba su apellido";
            $("#register-last-name").css("border-color", "red");
            return false;
        } else {
            document.getElementById("register-last-name-error").innerHTML = "";
            $("#register-last-name").css("border-color", "green");
            return true;
        }
    }

//Comprobamos telefono
    function comprobar_telefono() {
        telefono = document.getElementById("register-tlf").value;
        if (telefono.length == 0) {
            document.getElementById("register-tlf-error").innerHTML = "Escriba su número de teléfono";
            $("#register-tlf").css("border-color", "red");
            return false;
        } else if (telefono.length < 9 || telefono.length > 11) {
            document.getElementById("register-tlf-error").innerHTML = "Debe contener entre 9 dígitos y 11 dígitos";
            $("#register-tlf").css("border-color", "red");
            return false;
        } else {
            document.getElementById("register-tlf-error").innerHTML = "";
            $("#register-tlf").css("border-color", "green");
            return true;
        }
    }

//Comprobamos DNI
    function comprobar_dni() {
        dni = document.getElementById("register-dni").value;
        dni = dni.toString().toUpperCase();
        nifRegex = /^[0-9]{8}[TRWAGMYFPDXBNJZSQVHLCKET]{1}$/i;
        nieRegex = /^[XYZ]{1}[0-9]{7}[TRWAGMYFPDXBNJZSQVHLCKET]{1}$/i;
        if ((nifRegex.test(dni) == false) && (nieRegex.test(dni) == false)) {
            document.getElementById("register-dni-error").innerHTML = "NIE/DNI incorrecto, formato no válido";
            $("#register-dni").css("border-color", "red");
            return false;
        }
        //Comprobamos que la letra del dni sea correcta.
        else if (nifRegex.test(dni) == true) {
            numero = dni.substr(0, dni.length - 1);
            letr = dni.substr(dni.length - 1, 1);
            numero = numero % 23;
            letra = 'TRWAGMYFPDXBNJZSQVHLCKET';
            letra = letra.substring(numero, numero + 1);
            if (letra != letr.toUpperCase()) {
                document.getElementById("register-dni-error").innerHTML = "DNI erroneo, la letra del DNI no se corresponde";
                $("#register-dni").css("border-color", "red");
                return false;
            } else {
                document.getElementById("register-dni-error").innerHTML = "";
                $("#register-dni").css("border-color", "green");
                return true;
            }
        }
        //Comprobamos que la letra del NIE sea correcta
        else {
            numero = dni.substr(1, dni.length - 2);
            numero2 = dni.charAt(0);
            switch (numero2) {
                case "X":
                    numero2 = 0;
                    break;
                case "Y":
                    numero2 = 1;
                    break;
                case "Z":
                    numero2 = 2;
                    break;
            }
            letr = dni.substr(dni.length - 1, 1);
            numero = (numero2 + numero) % 23;
            letra = 'TRWAGMYFPDXBNJZSQVHLCKET';
            letra = letra.substring(numero, numero + 1);
            if (letra != letr.toUpperCase()) {
                document.getElementById("register-dni-error").innerHTML = "NIE erroneo, la letra del NIE no se corresponde";
                $("#register-dni").css("border-color", "red");
                return false;
            } else {
                document.getElementById("register-dni-error").innerHTML = "";
                $("#register-dni").css("border-color", "green");
                return true;
            }
        }
        return true;

    }

//Comprobamos direccion
    function comprobar_direccion() {
        direccion = document.getElementById("register-adress").value;
        if (direccion.length == 0) {
            document.getElementById("register-adress-error").innerHTML = "Escriba su dirección";
            $("#register-adress").css("border-color", "red");
            return false;
        } else {
            document.getElementById("register-adress-error").innerHTML = "";
            $("#register-adress").css("border-color", "green");
            return true;
        }
    }

//Comprobamos codigo postal
    function comprobar_cp() {
        cp = document.getElementById("register-cp").value;
        if (cp.length == 0) {
            document.getElementById("register-cp-error").innerHTML = "Escriba su código postal";
            $("#register-cp").css("border-color", "red");
            return false;
        } else if (cp.length != 5) {
            document.getElementById("register-cp-error").innerHTML = "Debe contener 5 dígitos";
            $("#register-cp").css("border-color", "red");
            return false;
        } else {
            $.getJSON('libraries_php/comprobarCP.php', {'cp': cp}, function (data) {
                $.each(data, function (i, camp) {
                    cpexiste = camp.cpexiste;
                    poblacion = camp.poblacion;
                    provincia = camp.provincia;
                    if (cpexiste == true) {
                        document.getElementById("register-population").value = poblacion;
                        document.getElementById("register-province").value = provincia;
                        document.getElementById("register-cp-error").innerHTML = "";
                        $("#register-cp").css("border-color", "green");
                        cptrue = true;
                        return true;
                    } else {
                        document.getElementById("register-cp-error").innerHTML = "Código postal no existe";
                        $("#register-cp").css("border-color", "red");
                        cptrue = false;
                        return false;
                    }
                });
            })
        }
    }
});

