const url = 'https://swapi-api.hbtn.io/api/films/?format=json';
$.get(url, data =>
  data.results.forEach(r =>
    $('UL#list_movies').append(`<li>${r.title}</li>`)));
