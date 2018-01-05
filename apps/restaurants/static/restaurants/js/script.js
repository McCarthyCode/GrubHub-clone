$(document).ready(function () {
    $(".tags label").click(function () {
        $input = $("input#" + $(this).attr("for"));
        if($input.prop("checked")) {
            $(this).removeClass("active");
            $(this).addClass("inactive");
            $input.prop("checked", true);
        } else {
            $(this).removeClass("inactive");
            $(this).addClass("active");
            $input.prop("checked", false);
        }
    });
    $( "#tabs" ).tabs();
    $('#tabs a').click(function(){
        var $tabs = $("#tabs li");
        $tabs.addClass('inactive');
        $tabs.addClass('active');
        $(this).parent().addClass('active');
        $(this).parent().removeClass('inactive');
    });
});