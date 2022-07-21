# Spotify-Song-Recommender
This application is a song recommendation system which accepts a Spotify Song Identifier, and uses vectorized audio attributes of 50,000 Spotify songs to recommend the six most similar songs to the input song.

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
