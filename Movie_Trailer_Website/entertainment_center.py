import media
import fresh_tomatoes

the_revenant = media.Movie("The Revenant",
                        "Leo survives a bear attack.",
                        "http://cinemaroot.com/wp-content/uploads/2015/12/Watch-The-Revenant-full-movie.jpg",
                        "https://www.youtube.com/watch?v=QRfj1VCg16Y")

wall_street = media.Movie("The Wolf of Wall Street",
                          "Leo buys drugs with his stock market money.",
                          "http://www.impawards.com/2013/posters/wolf_of_wall_street_ver3.jpg",
                          "https://www.youtube.com/watch?v=idAVRvQeYAE")

great_gatsby = media.Movie("The Great Gatsby",
                           "Leo is really rich.",
                           "http://www.slantmagazine.com/assets/house/film/posterlabgreatgatsby.jpg",
                           "https://www.youtube.com/watch?v=TaBVLhcHcc0")

django = media.Movie("Django Unchained",
                     "Never watched it...",
                     "http://www.impawards.com/2012/posters/django_unchained_ver9.jpg",
                     "https://www.youtube.com/watch?v=eUdM9vrCbow")

j_edgar = media.Movie("J. Edgar",
                      "Leo is a president.",
                      "http://www.impawards.com/2011/posters/j_edgar_xlg.jpg",
                      "https://www.youtube.com/watch?v=XULIO67YIRA")
                

inception = media.Movie("Inception",
                        "Leo lives in peoples' dreams.",
                        "https://www.movieposter.com/posters/archive/main/101/MPW-50904",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

movies = [the_revenant, wall_street, great_gatsby, django, j_edgar, inception]
fresh_tomatoes.open_movies_page(movies)
