$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', (data) => {
  $('#hello').html(data.hello);
});