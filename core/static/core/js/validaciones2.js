$(document).ready(function() {
    $("#id_modificar_formulario_mascota").validate({
        rules: {
            txtNombreMascota: {
                required:true, /*Que sea "True" significa que es un campo obligatorio */
                minlength:1, /*Este indica el largo minimo*/
                maxlength:60 /*Este es el largo maximo*/
            },
            cboRaza:{
                required:true,
            },
            cboGenero:{
                required:true,
            },
            dateFechaNacimientoMascota:{
                required:false,
                date:true,
            },
            dateFechaIngreso:{
                required:true, /* AQUÍ FALTA VALIDAR QUE LA FECHA NO SEA MENOR A 2001*/
                date:true,
            },
            fileFoto:{
                required:true,
            },
            cboEstado:{
                required:true,
            },
            
        }
    });
});



