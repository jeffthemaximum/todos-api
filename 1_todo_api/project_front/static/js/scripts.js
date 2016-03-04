$(document).ready(function(){
  console.log("ELLO WARLD")

  $('#button').on('click', function(event){
    event.preventDefault();

    var movie_searched = $('input[name="movie"]').val().replace(" ", "+")
    console.log(movie_searched);

    $.ajax({
      method: "GET",
      url: "http://www.omdbapi.com/?t="+movie_searched,
      success:function(response){
        console.log(response)
        $('.blah').append(response.Title)
      }
    })
  })
})
