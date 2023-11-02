$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (response) {
    const translation = response.hello;
    $('DIV#hello').text(translation);
  });
});
