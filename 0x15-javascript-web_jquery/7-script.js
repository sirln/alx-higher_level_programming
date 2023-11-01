const url = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'
$.get(url, function (response) {
  $('DIV#character').text(response.name);
});
