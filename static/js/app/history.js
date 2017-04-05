$(document).ready(function() {
  var id = $(this).attr('id');
  var url = BASE_URL.replace(/\/$/, '');
  var new_url = BASE_URL + HISTORY.join('/');
  
  History.pushState({}, document.title, new_url);
});

$('.history').on('click', function() {
  var id = $(this).attr('id');
  History.pushState(null, document.title, id);
});
