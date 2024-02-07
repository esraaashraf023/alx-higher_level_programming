// Wait for the document to be ready
$(document).ready(function() {
    // Handle button click or ENTER key press
    $("#btn_translate").on("click", function() {
      translateHello();
    });
  
    $("#language_code").on("keypress", function(event) {
      if (event.which === 13) {
        translateHello();
      }
    });
  
    // Function to fetch and display translation
    function translateHello() {
      var languageCode = $("#language_code").val();
      var apiUrl = "https://www.fourtonfish.com/hellosalut/hello/";
  
      // Fetch translation
      $.ajax({
        url: apiUrl + languageCode,
        method: "GET",
        success: function(data) {
          var translatedHello = data.hello;
          $("#hello").text(translatedHello);
        },
        error: function() {
          console.log("Error fetching translation.");
        }
      });
    }
  });  