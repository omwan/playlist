var $SCRIPT_ROOT = {{ request.app|tojson|safe }};

$(function( {
    $.getJSON($SCRIPT_ROOT + "/tracks", function(playlists) {
        for (var i = 0; i < playlists.length; i++) {
            $(".playlists").append($('<li></li>').html(playlists[i].name))
        }
    })
}))