$.get('https://swapi.co/api/films/?format=json', data =>
  data.results.forEach(movie =>
    $('UL#list_movies').append(`<li>${movie.title}</li>`))
);
