# Movie_trailer_website
A Movie trailer website Part of Full stack Nano degree Program
# Introduction
This is server site code which is wriiten in python which takes you to a great experience of enjoying your favourite Movie trailes

# Step To follow
1) Download Zip File<br>
2) Run fresh_tomato.html to view th website<br>
3) Enjoy the Site<br>

# Want to add your favourite Movies Allright then..
1) Download Python which is freely available from  <br>
   For Windows--><a href="https://www.python.org/downloads/">Click Here</a> <br>
   For Mac --> <a href="https://www.python.org/downloads/mac-osx/">Click Here</a><br> 
2) Edit entertainment.py using Python IDE( Integrated devlopmemnt Enviroment )<br>
3) Create Your Movie Object like
  <br> object_name = media.Movie("Movie_Name","YoutubeURL")
  <br>Easy Right!!!<br>
4) Add your Created objects in list or Array
  <br>
  movies = [ object_name1 , object_name2 ]..
  <br>That's IT!!!!!!!!<br>
5) Run the File by using F5

# Specific Changes Done By Me
--- Using OMDB API to get data in JSON Format---
```
  def info(movie):
    # Getting details of requested Movie URL
    response = urllib.urlopen("http://www.omdbapi.com/?t=" +
                              movie + "&y=&plot=short&r=json")
    # Reading Data recieved in form of JSON
    output = response.read()
    # Extracting the Value from Output variable
    wjdata = json.loads(output)
    return wjdata
```
<br>
--- Using IMDB Rating From JSON Format ---

``` 
  self.rating = data['imdbRating']
```
<br>
Adding imdb image and Rating to fresh_tomato.py 
```
 <img src="http://g-ecx.images-amazon.com/images/G/01/imdb/plugins/rating/images/imdb_38x18.png" alt=" Toy Story
(1995) on IMDb" />
<p id="hh2">{movie_rating}</p>
```
<br>
Declaring movie rating Variable
```
content += movie_tile_content.format(
            movie_rating=movie.rating,
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id
        )
```
# --- Styling Done By Me
1) Adding Background Image
```
 body {
            padding-top: 80px;
            background-image: url("black_background_wood-wallpaper-2048x1152.jpg");
        }
```
<br>
2) Adding Google Fonts
```
<link href="https://fonts.googleapis.com/css?family=Gloria+Hallelujah" rel="stylesheet">
<link href="https://fonts.googleapis.com/css?family=Lobster" rel="stylesheet">
```
<br>
3) Text Editing in these classes
```
#hh{
            font-size:300%;
            color: white;
            font-family: 'Lobster', cursive;
        }
        #hh2{
            color:white;
            font-size: 200%;
        }
        .navbar-brand{
            font-size: 50px;
            font-family: 'Gloria Hallelujah', cursive;
        }
```
