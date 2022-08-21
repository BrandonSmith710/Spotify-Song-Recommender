import pandas as pd
import os
from flask_sqlalchemy import SQLAlchemy
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

DB = SQLAlchemy()
class Song(DB.Model):

    id = DB.Column(DB.String(100), primary_key = True, nullable = False)
    ind = DB.Column(DB.BigInteger, nullable = False)
    name = DB.Column(DB.String(50), nullable = False)
    acoustic = DB.Column(DB.Float, nullable = False)
    danceable = DB.Column(DB.Float, nullable = False)
    energy = DB.Column(DB.Float, nullable = False)
    loudness = DB.Column(DB.Float, nullable = False)
    mode = DB.Column(DB.Float, nullable = False)
    liveness = DB.Column(DB.Float, nullable = False)
    valence = DB.Column(DB.Float, nullable = False)
    tempo = DB.Column(DB.Float, nullable = False)
    duration_ms = DB.Column(DB.Float, nullable = False)

    def __repr__(self):
        return f'{self.name} is {round(self.duration_ms*60000, 2)} minutes long'
    

class UserIP(DB.Model):
    ip = DB.Column(DB.String(50), primary_key = True, nullable = False)

path = os.path.join(os.getcwd(), 'data.csv')
df_song = pd.read_csv(path)
feat_names = ['id', 'name', 'acousticness', 'danceability', 'energy', 'loudness',
          'mode', 'liveness', 'valence', 'tempo', 'duration_ms']
df_song = df_song[feat_names][:50000]

# df_copy = df_song[feat_names[2:]]
# model = NearestNeighbors(n_neighbors = 6, algorithm = 'kd_tree')
# # scaler = StandardScaler()
# # feats = scaler.fit_transform(df_copy)
# model.fit(df_copy.values)
# with open('knn_model.h5', 'wb') as f:
#     pickle.dump(model, f)




