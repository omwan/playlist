$(document).ready(function(){
    console.log("running")
    
    $.get('https://api.spotify.com/v1/me/playlists?limit=10&offset=5', function(data){
        console.log(JSON.parse(data.text).items)
    })
})