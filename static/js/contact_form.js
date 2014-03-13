    var error_message;
    function isValidEmailAddress(emailAddress) {

        var pattern = new RegExp(/^((([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+(\.([a-z]|\d|[!#\$%&'\*\+\-\/=\?\^_`{\|}~]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])+)*)|((\x22)((((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(([\x01-\x08\x0b\x0c\x0e-\x1f\x7f]|\x21|[\x23-\x5b]|[\x5d-\x7e]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(\\([\x01-\x09\x0b\x0c\x0d-\x7f]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF]))))*(((\x20|\x09)*(\x0d\x0a))?(\x20|\x09)+)?(\x22)))@((([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|\d|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.)+(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])|(([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])([a-z]|\d|-|\.|_|~|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])*([a-z]|[\u00A0-\uD7FF\uF900-\uFDCF\uFDF0-\uFFEF])))\.?$/i);
        return pattern.test(emailAddress);
    }
    function addError(message,field){
        var error = '<span class="help-block">'+message+'</span>';
        var formField = $("#"+field+"-group");
        formField.addClass("has-error");
        formField.append(error);
    }
    function removeError(field){
        var formField = $("#"+field+"-group");
        formField.removeClass("has-error");
        formField.find("span").remove();
    }
    function hasError(field){
        var formField = $("#"+field+"-group");
        return formField.hasClass("has-error");
    }
    function checkForErrors(field){
        var input,error;
        if(field =='message'){
            input = $('textarea[name=message]').val();
            if (input == ""){
                error = { message : error_message }}
            else{ error = { message : 0 }}
        }else{
            if (field =='email'){
                input = $("input[name="+field+"]").val();
                if (!isValidEmailAddress(input)){
                    error = {email : error_message}}
                else error = { email : 0  }
            }else{ if ((field =='name')){
                input = $("input[name="+field+"]").val();

                if (input == ""){
                    error = { name: error_message }}
                else{ error = { name : 0 }}

            } else{
                if(field =='phone'){
                    input = $("input[name="+field+"]").val();
                    if (input == ""){
                    error = { phone: error_message }}
                    else{ phone = { name : 0 }}
                    }
                }
            }
        }
        return error
    }
    function addAlert(type,message){
        var html = '<div id="ajax_message" class="alert alert-'+type+'">'+
                   '<a class="close" data-dismiss="alert">x</a>'+
                    message+
                    '</div>';
        $("#submit-contact").before(html);
    }
    function addLoader(){
        var html = '<div id="ajax_loader" class="col-sm-12">'+
           '<img width="100%" height="30px" src="{{ STATIC_URL }}img/ajax/message_loader.gif" alt="Trwa wysyłanie..."/>'+
           '</div>';
        $("#submit-contact").before(html);
    }

    $( "#contact-form" ).submit(function( event ) {
        event.preventDefault();
        var language = location.pathname.split("/")[1];

        if  (language === "pl") error_message = "To pole jest wymagane.";
        else if (language === "de") error_message = "Dieses Feld ist erforderlich.";
             else if (language === "en") error_message = "This field is required.";
                  else if (language === "ru") error_message = "Это поле обязательно.";


        var formFields = ["name","email","phone","message"];
        var name  = $("input[name=name]").val();
        var email = $("input[name=email]").val();
        var phone = $("input[name=phone]").val();
        var message = $('textarea[name=message]').val();
//       {#   clear messages     #}
        $("#ajax_message").remove();
        $("#ajax_loader").remove();
        var errors = [];

        var url= '/ajax/contact-form/';
        for (var i=0;i<formFields.length;i++){
            removeError(formFields[i]);
            var output = checkForErrors(formFields[i]);
            if (typeof output != 'undefined' && output.constructor == Object){
            errors.push(output);
            }

        }
        var err = [];
        for (var vari=0;vari<errors.length;vari++)
        {
            for(key in errors[vari]){
                if(errors[vari].hasOwnProperty(key))
                    if(errors[vari][key]!=0)
                    err.push(1);
        }
        }
        if (err.length == 0)
        {
            addLoader();
            var request;
            if (request) {
                request.abort();
            }
            request = $.ajax({
                type: "POST",
                url: url,
                data: {
                    'name'   : name,
                    'email'  : email,
                    'phone'  : phone,
                    'message': message,
                    'csrfmiddlewaretoken': '{{ csrf_token }}'
                },
                dataType: 'json'
            });
            request.done(function (response, textStatus, jqXHR){
                if(response.done)
                    addAlert("success",response.message);
                else
                    addAlert("danger",response.message);

            });
            request.fail(function (jqXHR, textStatus, errorThrown){
                // log the error to the console
                console.error(
                    "The following error occured: "+
                    textStatus, errorThrown
                );
            });
            request.always(function () {
                $("#ajax_loader").remove();
            });
        }else{
            for (var iter=0;iter<errors.length;iter++){
                for(key in errors[iter]){
                if(errors[iter].hasOwnProperty(key))
                    if(errors[iter][key]!=0)
                    addError(errors[iter][key],key);
                }
            }

        }

    });
