const urlmovies = 'https://swapi-api.hbtn.io/api/films/?format=json';
const $list_movie = $('ul#list_movies');

$.ajax({
  url: urlmovies,
  dataType: 'json'
}).done((data) => {
  const movies = data.results;

  for (let st8 = 0; st8 < movies.length; ++st8) {
    const tit_movie = movies[st8].title;
    const oths = `<li>${tit_movie}`;
    $list_movie.append(oths);
  }
});
