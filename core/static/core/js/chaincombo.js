// Con este JavaScript Vamos a hacer que el ComboBox de Ciudad se desbloquee cuando se selecione una Region
var chaincombo=(function(){
    var _cboreg=null;
    var _cbociu=null;
    var _cbocom=null;
    var _init=function(){
        _cboreg=$('select.cboRegion');
        _cbociu=$('select.cboCiudad');
        _cbocom=$('select.cboComuna');
        
        _cboreg.on('change',_regchange);
        _cbociu.on('change',_ciuchange);
    }
    var _regchange=function(evt){
        var _idreg=_cboreg.val();
        if(!_idreg)return;
        $.ajax({
            url: '../get_ciudades/'+_idreg+'/',
            type: 'GET',
            success: function(response){
                _cbociu.find('option').remove().end();
                _cbociu.prop('disabled',true);
                if(response.length){
                    var o = new Option('Seleccione', '');
                    $(o).html('Seleccione');
                    _cbociu.append(o);
                    _cbociu.prop('disabled',false);
                }   
                _cbocom.find('option').remove().end();
                _cbocom.prop('disabled',true);
                for(var i=0,l=response.length;i<l;i++){
                    var _c=response[i];
                    var o = new Option(_c.fields.nombreCiudad, _c.pk);
                    $(o).html(_c.fields.nombreCiudad);
                    _cbociu.append(o);
                }
            },
            error: function (request, status, error) {
                alert(error);
            }
        });
    }
    /*var _ciuchange=function(evt){
        var _idciu=_cbociu.val();
        if(!_idciu)return;
        $.ajax({
            url: '../get_comunas/'+_idciu+'/',
            type: 'GET',
            success: function(response){
                _cbocom.find('option').remove().end();
                if(response.length){
                    var o = new Option('Seleccione', '');
                    $(o).html('Seleccione');
                    _cbocom.append(o);
                    _cbocom.prop('disabled',false);
                }   
                for(var i=0,l=response.length;i<l;i++){
                    var _c=response[i];
                    var o = new Option(_c.fields.nombre_comuna, _c.pk);
                    $(o).html(_c.fields.nombre_comuna);
                    _cbocom.append(o);
                }
            },
            error: function (request, status, error) {
                alert(error);
            }
        });
    }*/
    return{
        init:_init
    };
})();

$(document).ready(function() {
    chaincombo.init();
});