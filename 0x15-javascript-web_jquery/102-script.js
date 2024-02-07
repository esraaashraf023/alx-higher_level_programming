$(document).ready(function() {
    $("#btn_translate").click(function() {
        var languageCode = $("#language_code").val();
        $.ajax({
            url: "https://www.fourtonfish.com/hellosalut/hello/",
            data: { lang: languageCode },
            method: "GET",
            success: function(response) {
                $("#hello").text(response.hello);
            },
            error: function() {
                $("#hello").text("Translation not available for the specified language.");
            }
        });
    });
});