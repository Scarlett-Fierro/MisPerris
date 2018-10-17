$(document).ready(function() {
    $("#idformulario").validate({
        rules: {
            txtRut: {
                required:true, /*Que sea "True" significa que es un campo obligatorio */
                minlength:8, /*Este indica el largo minimo*/
                maxlength:12 /*Este es el largo maximo*/
            },
            txtNombreCompleto:{
                required:true,
                minlength:2,
                maxlength:60
            },
            txtCorreoElectronico:{
                required:true,
                minlength:4,   
                maxlength:45
            },
            txtDateNacimiento:{
                required:true, /* AQUÍ FALTA VALIDAR QUE LA FECHA NO SEA MENOR A 2001*/
                date:true,
                max:"2001-01-01"
            },
            txtTelefono:{
                required:true,
                minlength:7,
                maxlength:15
            },
            cboRegion:{
                required:true
            },
            cboCiudad:{
                required:true,
            },
            cboVivienda:{
                required:true,
            },

        }
    });
});

