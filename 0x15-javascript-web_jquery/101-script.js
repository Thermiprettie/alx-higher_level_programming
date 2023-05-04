$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    $('UL.my_list').item().last().remove();
  });
  $('DIV#clear_list').click(function () {
    $('UL.my_list').item().remove();
  });
});
