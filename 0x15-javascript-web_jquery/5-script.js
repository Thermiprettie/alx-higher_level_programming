var itemElem = $("<li></li>").text("Item");

$('#add_item').click(function() {
   $('.my_list').append(itemElem)
})
