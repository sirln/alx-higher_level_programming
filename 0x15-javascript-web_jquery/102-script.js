$('document').ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();
    const url = `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`;
    $.get(url, function (response) {
      $('DIV#hello').html(response.hello);
    });
  });
});
