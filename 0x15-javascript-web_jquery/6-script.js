const $headerItem = $('header');
const $updateHeaderitem = $('div#update_header');

$updateHeaderitem.on('click', () => {
  $headerItem.text('New Header!!!');
});
