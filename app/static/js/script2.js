$(document).ready(function() {
  $( '#info-button' ).click( function() {
      $('#diagram').attr("style", "display:block")
      $('#background-overlay').fadeToggle();
      $('#close-diagram').fadeToggle();
      $('.diagram-area').fadeToggle();

  });


  $(document).click(function(e){
    var container = $('#diagram');
    var button = $('#info-button');

    // if the target of the click isn't the container nor a descendant of the container
    if (!container.is(e.target) && !button.is(e.target) && container.has(e.target).length === 0)
    {
      $('#diagram').fadeOut(300);
      $('#background-overlay').fadeOut(300);
      $('#close-diagram').fadeOut(300);
      $('.diagram-area').fadeOut(300);
    }
  });
});
