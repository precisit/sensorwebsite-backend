$(document).ready(function() {
  var urlCodes = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/29/codes.json";
  var url = "https://opendata-download-metobs.smhi.se/api/version/1.0/parameter/29/station/97530/period/latest-day/data.json";
  var res = $.getJSON(url, function(json) {
    var items = [];
    var val = json.value[0].value;
    var res = $.getJSON(urlCodes, function(json) {
        text = json.entry[parseInt(val)].value
        console.log(text)
        console.log(val)
        $('#weather-text').append(text);
    })
  })
  .done(function() {
    console.log( "Get JSON done" );
  })
  .fail(function(jqxhr, textStatus, error) {
    console.log( "Get JSON error" );
  })
  .always(function() {
    console.log( "Get JSON complete" );
  });
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
