function addToken(my_class, template, token) {
  $(my_class).append(Mustache.render(template, {'token':token}));
}

$(document).ready(function(){
  console.log("ELLO WARLD");

  // manually trigger modal
  // TODO only trigger modal if cookie not present
  $("#loginModal").modal("show");


  // handle submission of todo
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

  // handle clicking of "sign up" link in login modal
  $('#sign-up-link').on('click', function(event){
    // hide login modal
    $("#loginModal").modal("hide");

    // show  register modal
    $("#registerModal").modal("show");
  });

    // handle clicking of "signin" link in register modal
  $('#sign-in-link').on('click', function(event){
    // hide register modal
    $("#registerModal").modal("hide");

    // show  login modal
    $("#loginModal").modal("show");
  })

  // handle submission of "log in" in modal
  $('button#li-submit').on('click', function(event){
    // prevent submission
    event.preventDefault();

    // get un and pw
    var username = $('#li-username').val();
    var password = $('#li-password').val()

    // put data in dict
    var data = {
      'username': username,
      'password': password
    }

    // make acceptable for ajax
    data = JSON.stringify(data);

    // prepare ajax request
    $.ajax({
      type: "POST",
      url: "http://127.0.0.1:8000/todos/login",
      data: data,
      // dataType: "jsonp",

      // set cookie on sucess
      success: function(response){
        // set cookie
        $.cookie('token', response['token']);
        // kill sign-in modal
        $("#loginModal").modal("hide");
        //append UN to screen
        var unTemplate = "Your token is {{token}}"
        // ad token to html via mustache
        addToken('.username-p', unTemplate, response['token']);

      },

      error: function(response){
        console.log('something terrible happened. You should probably kill urself :(');
        console.log(response);
      }
    })


  })

  $("#view-todos-button").on('click', function(event){

    var todoTemplate = "<li>Task: {{content}}, Completed?: {{finished}}</li>"

    function addTodo(todo) {
        $('.todos').append(Mustache.render(todoTemplate, todo));
    }

    var token = $.cookie('token');

    var url = "http://127.0.0.1:8000/todos/" + token + "/view-all"

    $.get(url, function(todos){

      $.each(JSON.parse(todos), function(i, todo){
          addTodo(todo);
      });
    });

  })
})


