$(document).ready(function() {
    $("#update_header").on("click", function() {
      var headerElement = $("header");
      headerElement.text("New Header!!!");
    });
  });  