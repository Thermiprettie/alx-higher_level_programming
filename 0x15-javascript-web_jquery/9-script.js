$(document).ready(function () {
  const urlsalut = 'https://fourtonfish.com/hellosalut/?lang=fr';
  const $justhello = $('div#hello');

  function getSalut () {
    return $.get({
      url: urlsalut,
      dataType: 'json'
    });
  }

  getSalut().then((say) => {
    $justhello.text(say.hello);
  });
});
