import media
import fresh_tomatoes


# Function to get direct information of Movie details like
# title , rating , poster etc.
# Using Info function to get Movie Information

toy_story = media.Movie("Toy Story",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")
gangs_of_w = media.Movie("Gangs of Wasseypur",
                         "https://www.youtube.com/watch?v=j-AkWDkXcMY")
dangal = media.Movie("Dangal",
                     "https://www.youtube.com/watch?v=x_7YlGv9u1g")
bahubali = media.Movie("Delhi Belly",
                       "https://www.youtube.com/watch?v=VdafjyFK3ko")
rings = media.Movie("Rings",
                    "https://www.youtube.com/watch?v=mZBLbeDtpaE&t=3s")
# Array of Movie objects is Created
movies = [toy_story, avatar, gangs_of_w, dangal, bahubali, rings]
# HTML page is requested
fresh_tomatoes.open_movies_page(movies)
