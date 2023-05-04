const $thelist = $('ul.my_list');
const $additem2gd = $('div#add_item');

$additem2gd.on('click', () => {
  $thelist.append('<li>Item</li>');
});
