var $SCRIPT_ROOT = {{ request.app|tojson|safe }};

$(function() {
    $.getJSON($SCRIPT_ROOT + '/tracks', function(data) {
        $(".playlists").text(data.result);
    });
    return false;
});