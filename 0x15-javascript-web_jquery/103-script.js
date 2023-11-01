$('document').ready(function(){
  function displayTranslation() {
    const languageCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`;
    $.get(url, function(response) {
      $('DIV#hello').html(response.hello);
    });
  }
  $('INPUT#btn_translate').click(displayTranslation);
  $('INPUT#language_code').keypress(function(event) {
    if (event.which === 13) {
      displayTranslation();
    }
  });
});
