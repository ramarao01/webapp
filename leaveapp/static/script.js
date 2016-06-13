$(function() {
    $('button').click(function() {
        var user = $('#empfirstname').val();
        var pass = $('#emplastname').val();
        $.ajax({
            url: '/signupuser',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
});
