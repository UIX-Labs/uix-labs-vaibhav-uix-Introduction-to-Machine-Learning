import os
from datetime import datetime

from dotenv import load_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from recommenders.popularity_recommender import recommend_popular_movies
from recommenders.content_based import content_based_recommendation
from recommenders.collaborative_filtering import collaborative_recommendation


app = Flask(__name__)


@app.route('/')
def index():
    data = "Welcome to Instalearn ML Tutorial!"
    return {"message": data}



@app.route('/recommend/popular')
def popular_movies():
    data = recommend_popular_movies()
    return data


@app.route('/recommend/content_based', methods=['POST'])
def content_based():
    if request.method == "POST":
        data = request.get_json()
        data = content_based_recommendation(data['movie'])
        return data
    

@app.route('/recommend/collaborative', methods=['POST'])
def collaborative_recommend():
    if request.method == "POST":
        data = request.get_json()
        data = collaborative_recommendation(data['movie'])
        return data


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, debug=True)