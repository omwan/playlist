# playlist

http://devpost.com/software/perfect-party-playlist

Made for HuskyHacks 2016

<h3>Inspiration</h3>
Our goal was to make a playlist so that there will never be a moment at a party where the next song is so different from the last that the mood is killed and people lose interest.

<h3>What it does</h3>
Perfect Party Playlist reorders a personal Spotify playlist. It uses track factors like "danceability", "energy", and "tempo" (which are built into Spotify) to find the songs on the playlist with the minimum differences and ordered them next to each other. We also made the general mood of the party an arch, the songs build up in the energy and danceability, reach a climax song (highest ratings of our factors), and then has a few songs at the end to work the energy down gradually.

<h3>How we built it</h3>
We worked with the Spotify API and their web app developer, the Spotipy python library, HTML and flask. The Spotipy library allowed us to access built in functions which enable users to authorize their account with our app, access users playlists and also to rewrite them. We used distance formulas between the different tracks to make a sorted list of tracks going from highest to lowest energy and daceability and then we reordered that list to be more of an arch.

<h3>Challenges we ran into</h3>
Our biggest challenge was getting the Spotify authorization to work so that we could access a user's tracks.

<h3>Accomplishments that we're proud of</h3>
This was our first time making a web app for a pre-made API and dealing with the troubles that go along with that. We were able to get our app up and running and working with Spotify, which was huge for us.

<h3>What we learned</h3>
We learned how to use Git hub, how to combine front end and back end and how to work with Spotify's API.

<h3>What's next for Perfect Party Playlist</h3>
In an ideal world, Perfect Party Playlist would have different party models to choose from. At the moment, our model is an arch with rising action, a climax and a conclusion. For a longer playlist, it might be a better idea to make a model that is more like a wave, with multiple climaxes and some slower rests in between. Also, some people may want their party to have their climax as the last song. Users should be able to see these different modes and choose which one they prefer.

<h3>Built With</h3>
html
css
python
spotify
spotipy
flask
