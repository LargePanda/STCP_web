function add_option(target_char){
    var radioInput = document.createElement('input');
    radioInput.setAttribute('type', 'radio');
    radioInput.setAttribute('name', "foo");
    radioInput.setAttribute('value', target_char);

    var label = document.createElement('label');
    label.setAttribute('for', "new");
    var label_text = document.createTextNode(target_char);
    label.append(label_text);

    $("#radio_group").append(radioInput);
    $("#radio_group").append(label);
    $("#radio_group").append("<br/>");

    
};

function update_info(data){
    $('#example').html(data['example']);
    $('#explain').html(data['explain']);
};

function analyze_char(source_char){
    $("#radio_group").html("");
    $.ajax({
        url: '/cctk_app/query_char/'+source_char,
        dataType: "json",
        type: 'get', // This is the default though, you don't actually need to always mention it
        success: function(data) {
            console.log('/cctk_app/query_char/'+source_char);
            cands = data['candidate'];
            update_info(data);
            for (var i = 0; i<cands.length; i++){
                add_option(cands[i]);
            }
        },
        failure: function(data) { 
            console.log("Error");
        }
    }); 
};