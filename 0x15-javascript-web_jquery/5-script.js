$(document).ready(function() {    
    $("#add_item").on("click", function() {
      var newItem = $("<li>").text("Item");
      var myList = $("ul.my_list");
      myList.append(newItem);
    });
  });