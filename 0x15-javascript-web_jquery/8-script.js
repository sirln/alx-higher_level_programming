const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(url, function (response) {
  const movies = response.results;
  const listMovies = $('UL#list_movies');
  $.each(movies, function (index, movie) {
    listMovies.append(`<li>${movie.title}<li>`);
  });
});
