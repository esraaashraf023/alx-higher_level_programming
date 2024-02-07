$(document).ready(function() {
    $("#add_item").on("click", function() {
      var newItem = $("<li>").text("Item");
      $("ul.my_list").append(newItem);
    });
    $("#remove_item").on("click", function() {
      $("ul.my_list li:last-child").remove();
    });
    $("#clear_list").on("click", function() {
      $("ul.my_list").empty();
    });
  });  