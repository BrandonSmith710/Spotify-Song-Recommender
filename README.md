# Spotify-Song-Recommender
This application is a song recommendation system which accepts a Spotify Song Identifier, and uses vectorized audio attributes of 50,000 Spotify songs to recommend the five most similar songs to the input song. First visit the view_name_and_id route, enter a number between 0 and 49,999, copy the id for the song that appears, and then visit the home route to paste the id and view the rcommendations.

Installation:

First clone the repository.

Next, change directories to the clone, and run the following command:

pipenv install flask flask-sqlalchemy gunicorn pandas scikit-learn==1.0.2 jinja2 numpy

Then run:

export FLASK_APP=app.py

Now run:

pipenv shell

Finally, run:

flask run
