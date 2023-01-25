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
4. Activate the virtual environment by using ```source venv/Scripts/activate``` (git bash) and install all the dependencies by executing ```python -m pip install -r requirements.txt```.
5. It is recommended to create an admin user to interact with the admin interface for validation purposes during the testing of all the features of the service built. For that, first change the current directory to the *fiftyseven_movies* directory, where is located the *manage.py* file, and execute ```py manage.py createsuperuser```. Type all the info requested by the command prompt.
6. Finally, run the server by executing ```py manage.py runserver```


## Documentation and guideline

It was prepared an easy-to-read and user-friendly guideline to use the service. You can access the material through Notion, by clicking the following link: https://grape-fuel-459.notion.site/Fiftyseven-movies-857021689b9640f5993577770d79ee7d


## Cloud-based deployment

> **Note**
The app version uploaded to the cloud is the one in the *production* branch of this repo. The main differences are that in the production branch the *Whitenoise* package was installed to serve the staticfiles associated to the DRF built-in interfaces so that the user can use it during his tests, as well as the corresponding configuration parameters modified in the settings file of the project.

You can access to the app by clicking on https://fiftyseven-movies.azurewebsites.net/get-movies/. It is important to point out that, as it is no any index or welcoming page created, the first page you will see will be the one associated to the *get-movies* endpoint (The one with which the Movies table is filled up), however, you can add/change the corresponding endpoints to the URL and use the app as it is described in the guideline (previous section) 

On the other hand, as most of the endpoints are protected and only accessible passing a valid authorization token in the header, if you're going to use the DRF built-in interface, it is recommended to use an extension in your browser which allow you to define headers for each request. If you're using Chrome, for example, you can check this one: https://modheader.com/modheader/tutorial.

The below image shows a working GET request which require an authorization token:

![example_API_working_image](https://github.com/Andrescc143/fiftyseven-movies/blob/production/fiftyseven_movies/fiftyseven_movies/staticfiles/services-working.png)

The following is another example, but this time, retrieving private data (data which belongs to and which is only accessible by its owner)

![private_data_example](https://github.com/Andrescc143/fiftyseven-movies/blob/production/fiftyseven_movies/fiftyseven_movies/staticfiles/services-working-private-data.png)


## APP Highlights 

### Features

* JWT authentication using Simple-JWT
* Endpoint to fill up table of the Movie model, in order to use its elements during the interaction with the table of the MoviePlaylist model
* The project is divided by apps, considering the general logic of each feature. The apps are: 
  * movies: Where all the features related to the movies and moviesplaylists was built, including the models (Movie and MoviePlaylist), the serializers, the views, etc.
  * users: Where all the features related to the users authentication was built, including the models (User), the configuration of the JWT classes,the serializers, the Login and Logout views, etc.
* The *settings.py* file was divided into base.py, local.py and production.py, where the last two files inherits from the base.py the general configurations. This to make easier the configuration of the project depending on the running environment.
* The validation processes for the data were included in the serializers used for each view. For this app is being use both, the default validators (based on the field to be validated, like the ones for Email fields) and some custom validators.
* The app has two versions:
  * Source code: To download and execute in a local environment
  * Cloud-base: To get access through internet and interact with all the services built (the code is available in the *production* branch of this repo.)

### Ongoing work - Recommended future developments

* Modify the models associated to the authentication system to increase the cohesion between the JWT-based system and the built-in DRF authentication system.
* Modify the models of the Movies app to atomize the data, following the normalization rules established internationally.
* Check the logic and abstract all the possible behaviors/procedures in order to improve the service performance and increase its scalability.
* Build a more robust data architecture, using dedicated cloud-based services, to make as independent as possible the data from the app, and ensure high availability. 
* Implement strict security policies on the cloud service used for the app deployment, for example, if the service is a VM (Virtual Machine), define inbound rules to filter the trafic based on, for example, IP addresses; In addition, implement a tracking system to monitor the users activity and limit the use of the service to prevent DoS and DDoS attacks.
* Implement testing procedures to increase the quality of the services provided

