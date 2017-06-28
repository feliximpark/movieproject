#The Marvel-Movie-Universe-App#
The Marvel-Universe-App shows all movies of the Marvel superheroes with a picture of the billboard and the date of release. By clicking on the pictures, you can open a movie-player and see the trailer of each film.
--------

##How to start the app##
You have two possibilities to start the app.

1. **You can start it from your commandline**. Just clone the repro, navigate in the command line to the directory of your cloned repro and type in: python entertainment_center.py.

2. **You can start it in your browser.** When you first start the app via the command line, Python will create a html-file with the name marvel_universe.html. This initial start was already made in this repro. So: You can just take the html-file in this repro and open it in your browser. But be aware: You don't start the app itself, only the html created with the app in advance.
--------------

##What's under the hood?##
The app includes three Python-files.

**1. entertainment_center.py**
In this app you´ll find the instances of the Movie-class, defined in the file media.py. It includes infos about all the films in the app. Also it includes a list of all the movies and the command to start the main function of the file fresh_tomatoes.py

**2. media.py**
Here you will find the constructor for the Class Movies. This constructor defines the class with the attributes title, movie_release, storyline, the posterimage-url and the youtube-url of the trailer.

**3. fresh_tomatoes**
In this file, you find the html-code, that is built into the webapp, while placeholder are taking care of showing the right movies, the right storylines and the right trailer for the right file.
------------

##Credits##
The file fresh_tomatoes.py was delivered by Udacity, I only made small extensions (like the functionality to show the storylines, changing the name of the webapp and so on).




