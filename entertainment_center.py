import media
import fresh_tomatoes

# Defining movies
ride_along_2 = media.Movie("Ride Along 2",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/6/6b/Ride_Along_2_poster.jpg/220px-Ride_Along_2_poster.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=iWfmmwdCHTg"  # NOQA
                        )

avatar = media.Movie("Paranormal Activity",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/5/54/Paranormal_Activity_poster.jpg/220px-Paranormal_Activity_poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=F_UxLEqd074"  # NOQA
                     )

the_nightmare_before_christmas = media.Movie("The Nightmare Before Christmas",
                                             "https://upload.wikimedia.org/wikipedia/en/thumb/9/9a/The_nightmare_before_christmas_poster.jpg/220px-The_nightmare_before_christmas_poster.jpg",  # NOQA
                                             "https://www.youtube.com/watch?v=wr6N_hZyBCk"  # NOQA
                                             )

balls_of_fury = media.Movie("Balls Of Fury",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/Balls_of_furymp.jpg/220px-Balls_of_furymp.jpg",  # NOQA
                             "https://www.youtube.com/watch?v=l0nxP-izD2U"  # NOQA
                             )

ratatouille = media.Movie("Ratatouille",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk"  # NOQA
                          )

suicide_squad = media.Movie("Suicide Squad",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/Suicide_Squad_%28film%29_Poster.png/250px-Suicide_Squad_%28film%29_Poster.png",  # NOQA
                            "https://www.youtube.com/watch?v=CmRih_VtVAs"  # NOQA
                            )

hunger_games = media.Movie("Hunger Games",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=mfmrPu43DF8"  # NOQA
                           )

# Adds the movies to a list
movies = [ride_along_2, avatar, the_nightmare_before_christmas,
          balls_of_fury, ratatouille, suicide_squad, hunger_games
          ]

# Displays movies added to the list above to open_movies_page
fresh_tomatoes.open_movies_page(movies)
