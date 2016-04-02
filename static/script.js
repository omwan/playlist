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