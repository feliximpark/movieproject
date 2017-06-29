import media
import fresh_tomatoes

# creating instances of the movie-object
guardians_2 = media.Movie("Guardians of the Galaxy Vol. 2", "May 5, 2017",
                          """The Guardians of the Galaxy are fighting
                          a new enemy.""",
                          "http://t2.gstatic.com/images?q=tbn:ANd9GcSzRHzPW9j56dGLliOdUV0lzjeUwfALe9Zn2Ys7Kkwj4YsvDpsh",
                          "https://www.youtube.com/watch?v=pr7tDrwQ3t8")
doctor_strange = media.Movie("Doctor Strange", "November 4, 2016",
                             """A Doctor is learingn, that life is more
                             complex than it seems to be""",
                             "http://t3.gstatic.com/images?q=tbn:ANd9GcSKS0s-IiPnSKY5TwqL-CoUJfKRk5VYt6QBD4O66-1Wct_aPjhM",
                             "https://www.youtube.com/watch?v=MWRUNTLisPo")
captain_america_3 = media.Movie("Captain America: Civil War", "May 6, 2016",
                                """A crack goes through the Avengers. They
                                fight each other""",
                                "http://t0.gstatic.com/images?q=tbn:ANd9GcTVQ1HWTAPvw21dZLbh_exuiws7Y4HWcMT0OiOgtkk-rOWQiCiH",
                                "https://www.youtube.com/watch?v=FkTybqcX-Yo")
ant_man = media.Movie("Ant-Man", "July 17, 2015",
                      "A former criminal gets the power to become supersmall",
                      "http://t3.gstatic.com/images?q=tbn:ANd9GcRvTs_PtoegY0eToOxODXT12cfV-AipOD6GftFO0ze7wbociMNB",
                      "https://www.youtube.com/watch?v=QfOZWGLT1JM")
avengers_2 = media.Movie("Avengers: Age of Ultron", "May 1, 2015",
                         """The Avengers have to fight an artifical
                         intelligence""",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcRlGeugacRkKznDOtRhUCVt0AkrOTPbaaKwF9xgGZgNViyC_Xko",
                         "https://www.youtube.com/watch?v=rD8lWtcgeyg")
guardians = media.Movie("Guardians of the Galaxy", "August 1, 2014",
                        """A group of space adventures are joining together
                        to find a mysterious source of energy""",
                        "http://t1.gstatic.com/images?q=tbn:ANd9GcQosfipEWfoKWReYjWOUS1bKJOMuEXs7gth_2ySs9DKL2kTyPLA",
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")
captain_america_2 = media.Movie("The Winter Soldier", "April 4, 2014",
                                """Captain America is looking for his old
                                friend... who has become an enemy""",
                                "http://vignette3.wikia.nocookie.net/avengers/images/5/50/Captain_America_2_The_Return_of_the_First_Avenger.jpg/revision/latest?cb=20140222150959&path-prefix=de",
                                "https://www.youtube.com/watch?v=7SlILk2WMTI")
thor_2 = media.Movie("Thor: The Dark World", "November 8, 2013",
                     """Thor is a God - he is fighting against Aliens...
                     and his brother""",
                     "http://vignette4.wikia.nocookie.net/avengers/images/6/6c/Thor_-_The_Dark_Kingdom.jpg/revision/latest?cb=20140829154032&path-prefix=de",
                     "https://www.youtube.com/watch?v=4KTvjFGgGkk")
iron_man_3 = media.Movie("Iron Man 3", "May 3, 2013",
                         """Billionaire Tony Stark is fighting an
                         international terrorist. At least he thinks so...""",
                         "http://t0.gstatic.com/images?q=tbn:ANd9GcRLonM7bpdRGXJH75VkND-gHkSn4QXJZ108x7eKTQkCcNQ6xEVa",
                         "https://www.youtube.com/watch?v=Ke1Y3P9D0Bc")
avengers = media.Movie("Marvel's The Avengers", "May 4, 2012",
                       "A group of superheros is saving the world",
                       "http://t1.gstatic.com/images?q=tbn:ANd9GcTp0qlAoWcOOswIkL_qpjYzJqCCDmWXiBzCXiqbE43Obo8c0Z-s",
                       "https://www.youtube.com/results?search_query=Marvel%27s+The+Avengers+trailer+official")
captain_america = media.Movie("The First Avenger", "July 22, 2011",
                              """A super-soldier from the 40th awakes today
                              - and is fighting a nazi-organisation""",
                              "http://t1.gstatic.com/images?q=tbn:ANd9GcSawHqQ0WjKUclOs-1KvPDRGuBpILVOZVKsYyanuHjDg43aJNYE",
                              "https://www.youtube.com/watch?v=JerVrbLldXw")
thor = media.Movie("Thor", "May 6, 2011",
                   "The son of the God Odin is coming to Earth",
                   "http://t0.gstatic.com/images?q=tbn:ANd9GcRSZN3c1Wj6s6Nz0DLOYTZY4GM27rt6zRDCdw_z_0ff8oAKTeXE",
                   "https://www.youtube.com/watch?v=YSC9CjSYvYA")
iron_man_2 = media.Movie("Iron Man 2", "May 7, 2010",
                         """Billionaire Tony Stark is confronted with the
                         history of his murderd dad""",
                         "http://t1.gstatic.com/images?q=tbn:ANd9GcTbUWVX-6eusHp85uW6cbtbwzrW5UtBXgpc2FkCQEJ_YUO574gO",
                         "https://www.youtube.com/watch?v=BoohRoVA9WQ")
hulk = media.Movie("The Incredible Hulk", "June 13, 2008",
                   """A scientist is becoming a green monster, when he wants
                   to save the world""",
                   "http://www.hulk-derfilm.de/wp-content/uploads/poster_lg01.jpg",
                   "https://www.youtube.com/watch?v=FBSfUg-D7MI")
iron_man_1 = media.Movie("Iron Man", "May 2, 2008",
                         "A rich playboy is becoming an iron superhero",
                         "http://www.gstatic.com/tv/thumb/movieposters/170620/p170620_p_v8_ak.jpg",
                         "https://www.youtube.com/watch?v=8hYlB38asDY")

#creating a list with all movie-class-instances
movies = [iron_man_1, hulk, iron_man_2, thor, captain_america, avengers,
          iron_man_3, thor_2, captain_america_2, guardians, avengers_2,
          ant_man, captain_america_3, doctor_strange, guardians_2]
#setting movies in the right order (oldest film last)
movies.reverse()
#open the Web-App-building function in fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)
