const urlcharacter = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
const $characterdv = $('div#character');

$.ajax({
  url: urlcharacter,
  dataType: 'json'
}).done((data) => {
  $characterdv.text(data.name);
});
