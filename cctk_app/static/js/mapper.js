$(document).ready(function() {
            var $ta = $("#ta");
            var $startIndex = $("#startIndex"), $endIndex = $("#endIndex");

            var selected_sel;
            function reportNewSelection() {

                var sel, range;
                sel = document.getSelection();
                if (sel.anchorNode.parentElement.id == "ta"){
                    console.log("text select");
                }

                selected_sel = sel;

                if (sel.rangeCount){
                    range = sel.getRangeAt(0);

                    // update selected_text section
                    // $("#selected_text").text(range.toString());

                    //range.deleteContents();

                    //range.insertNode(document.createTextNode("replacementText"));                    
                    //$startIndex.text(sel.getRangeAt(0).start);
                    //$endIndex.text(sel.getRangeAt(0).end);

                    analyze_char(range.toString());
                }
            };

            $ta.on("mouseup", reportNewSelection);

            function getInfo(){
                    $("#queried").text("ij");
            }

            $("#btun").mousedown(function(e) {
                e.preventDefault();
                var replacementText = $('input[name="foo"]:checked').val();

                range = selected_sel.getRangeAt(0);
                range.deleteContents();
                range.insertNode(document.createTextNode(replacementText));                    
                
                // For IE, which always shifts the focus onto the button
                window.setTimeout(function() {
                    $ta.focus();
                }, 0);
            });

            $("#trans_btun").mousedown(function(e) {
                console.log('clicked');
                e.preventDefault();
                $.ajax({
                    url: '/cctk_app/ajax/',
                    type: 'get',
                    data: {
                        'text': $('#ta').html()
                    },
                    dataType: 'json',
                    success: function (data) {
                        console.log(data.text)
                        $('#ta').html(data.text)
                    }
                });                  
                
                // For IE, which always shifts the focus onto the button
                window.setTimeout(function() {
                    $ta.focus();
                }, 0);
            });

            

});


$('.ta_left').each(function(){
    this.contentEditable = true;
});
