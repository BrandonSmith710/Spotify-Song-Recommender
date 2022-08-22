from data import df_song, DB, Song, UserIP, feat_names
from flask import Flask, render_template, request
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import pickle
import pandas as pd
from sklearn.neighbors import NearestNeighbors
'''
suggest a song to the user based on audio attributes of the input song
'''

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_spotify.sqlite3'
APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
DB.init_app(APP)
model = pickle.load(
    open('knn_model.h5', 'rb')
)
@APP.before_first_request
def create_tables():
    DB.create_all()

@APP.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'POST':
        id = request.form.get('search')
        try:
            song = Song.query.get(id)
            query = [song.acoustic, song.danceable, song.energy, song.loudness,
            song.mode, song.liveness, song.valence, song.tempo, song.duration_ms]
        except AttributeError:
            print('No attributes exist for Nonetype object')
            return render_template('base.html')
        query = pd.Series(query, index = feat_names[2:])
        distances, indices = model.kneighbors([query])
        rec = []
        for index in indices[0][1:]:
            rec.append(Song.query.filter(Song.ind == int(index)).first().name)
        result = ' | '.join(rec)
        address = UserIP(ip = str(request.remote_addr))
        if not UserIP.query.get(address.ip):
            DB.session.add(address)
        DB.session.commit()
        return render_template('results.html', answer = result)
    return render_template('base.html')

@APP.route('/view_name_and_id', methods = ['GET', 'POST'])
def view_name_and_id():
    if request.method == 'POST':
        num = request.form.get('search2')
        num = num.replace(',', '')
        if num.isdigit():
            num = int(num)
            if 0 <= num < 50000:
                try:
                    song = Song.query.filter(Song.ind == num).first()
                    res = str((song.name, song.id))
                except AttributeError:
                    print('No attributes exist for Nonetype object')
                    return render_template('base2.html')
                return render_template('results2.html', answer = res)
            return render_template('base2.html')
        return render_template('base2.html')
    return render_template('base2.html')
        

'''the refresh route only need be used if a user would like to edit the size of the
   database, then simply run the add route with the adjusted parameters.'''

@APP.route('/refresh')
def refresh():
    DB.drop_all()
    DB.create_all()
    return 'Data has been refreshed.'

@APP.route('/add')
def add_one():
    for i in range(50000):
        sid, n, a, d, e, l, m, li, v, t, d = df_song.iloc[i].values
        temp = Song(id = sid, ind = i, name = n, acoustic = a, danceable = d,
        energy = e, loudness = l, mode = m, liveness = li, valence = v, tempo = t,
        duration_ms = d)
        if not Song.query.get(temp.id):
            DB.session.add(temp)
    DB.session.commit()
    return 'Songs have been added'

# @APP.route('/_see_addresses')
# def _see_addresses():
#     return str([uip.ip for uip in UserIP.query.all()])

if __name__ == '__main__':
    APP.run(host = '127.0.0.1', port = 8080, debug = True)
