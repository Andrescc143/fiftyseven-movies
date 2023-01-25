# Fiftyseven-movies

This is a services designed to provide to its user a way to create movies playlists by selecting the desired movies from a pre-filled-up database. The users will be able to:

* See the total number of registered users.
* Sign up and create their own user.
* Login and logout as desired following and authentication approach using JWT
* Create their own movies playlists selecting the movies from a list of pre-inserted movies. 
  * The playlists can be public or private, depending on the user's choice. 
  * A registered user is the only one allowed to interact with the movie/playlist endpoints (in which all the previous logic was implemented). 
  * The playlist can be updated according to user's instructions.


## Intallation process

Follow the instructions below to retrieve and executed all the features implemented:

1. Clone the repository executing on your desired directory: 
   '''
   git clone https://github.com/Andrescc143/fiftyseven-movies.git
   '''
2. Create a new virtual environment in the root folder of the project by executing '''python -m venv venv'''. Make sure you have installed python as the that it is include in the PATH variable (windows).
4. Activate the virtual environment by using """source venv/Script/activate""" (git bash) and install all the dependencies by executing """python -m pip install -r requirements.txt"""
5. It is recommended to create an admin user to user the admin interface for validation purposes. For that, first change the current directory to the fiftyseven_movies directory, where is located the manage.py file and execute """py manage.py createsuperuser""". Type all the info requested.
6. Finally, run the server by executing """py manage.py runserver"""

