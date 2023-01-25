# Fiftyseven-movies

This is a services designed to provide to the users a way to create movies playlists by selecting the desired movies from a pre-filled-up database. The users will be able to:

* See the total number of registered users.
* Sign up and create their own user.
* Login and logout as desired following and authentication approach using JWT
* Create their own movies playlists selecting the movies from a list of pre-inserted movies. 
  * The playlists can be public or private, depending on the user's choice. 
  * A registered user is the only one allowed to interact with the movie/playlist endpoints (in which all the previous logic was implemented). 
  * The playlist can be updated according to user's instructions.


## Intallation process

Follow the instructions below to retrieve and executed all the features implemented:

1. Clone the repository executing in your desired directory ```git clone https://github.com/Andrescc143/fiftyseven-movies.git```.
2. Create a new virtual environment in the root folder of the project by executing ```python -m venv venv```. Make sure you have installed python and that it is included in the PATH variable (Windows).
4. Activate the virtual environment by using ```source venv/Script/activate``` (git bash) and install all the dependencies by executing ```python -m pip install -r requirements.txt```.
5. It is recommended to create an admin user to interact with the admin interface for validation purposes during the testing of all the features of the service built. For that, first change the current directory to the *fiftyseven_movies* directory, where is located the *manage.py* file, and execute ```py manage.py createsuperuser```. Type all the info requested by the command prompt.
6. Finally, run the server by executing ```py manage.py runserver```


## Documentation and guideline

It was prepared an easy-to-read and user-friendly guideline to use the service. You can access the material through Notion, by clicking the following link: https://grape-fuel-459.notion.site/Fiftyseven-movies-857021689b9640f5993577770d79ee7d


## Cloud-based deployment

You can access to the app by clicking on https://fiftyseven-movies.azurewebsites.net/get-movies/. It is important to point out that, as it is no any index or welcoming page created, the first page you will see will be the one associated to the *get-movies* endpoint (The one with which the Movies table is filled up), however, you can add/change the corresponding endpoints to the URL and use the app as it is described in the guideline (previous section) 

On the other hand, as most of the endpoints are protected and only accessible passing a valid authorization token in the header, if you're going to use the DRF built-in interface, it is recommended to use an extension in your browser which allow you to define headers for each request. If you're using Chrome, for example, you can check this one: https://modheader.com/modheader/tutorial.

The below image shows a working GET request which require an authorization token:

![example_API_working_image](https://github.com/Andrescc143/fiftyseven-movies/blob/production/fiftyseven_movies/fiftyseven_movies/staticfiles/services-working.png)
