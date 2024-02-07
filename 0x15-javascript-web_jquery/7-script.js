$(document).ready(function() {
    $.ajax({
      url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",
      method: "GET",
      success: function(data) {
        var characterName = data.name;
        var characterDiv = $("#character");
        characterDiv.text(characterName);
      },
      error: function() {
        console.log("Error fetching data from the URL.");
      }
    });
  });  