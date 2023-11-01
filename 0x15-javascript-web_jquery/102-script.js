$('document').ready(function(){
  $('INPUT#btn_translate').click(function() {
    const languageCode = $('INPUT#language_code').val();
    const url = `https://www.fourtonfish.com/hellosalut/?lang=${languageCode}`
    $.get(url, function(response) {
      $('DIV#hello').text(response.hello);
    });
  });
});
