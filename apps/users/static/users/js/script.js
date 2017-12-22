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
});