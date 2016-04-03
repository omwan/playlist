function embed() {
    "use strict";
    var url = document.getElementById("url").value, urlArray, albumID, userID, playlistID, embedSrc;
        urlArray = url.split("/");
    if (urlArray[3] === "user") {
        userID = urlArray[4];
        playlistID = urlArray[6];
        embedSrc = "https://embed.spotify.com/?uri=spotify:user:" + userID + ":playlist:" + playlistID;
    }
    if (urlArray[3] === "album") {
        albumID = urlArray[4];
        embedSrc = "https://embed.spotify.com/?uri=spotify:album:" + albumID;
    }

    document.getElementById("embed").src = embedSrc;
}

$(document).ready(function(){
    console.log("running")
    //get the json generated from the website, and do this function to it
    $.get('https://api.spotify.com/v1/me/playlists?limit=10&offset=5', function(data){
        console.log(JSON.parse(data.text).items)
    })
})