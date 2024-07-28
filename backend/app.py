from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load movie data
with open('data/movies.json') as f:
    movies = json.load(f)

# Dummy user preference data
user_preferences = {
    "user1": ["Movie A", "Movie B"],
    "user2": ["Movie B", "Movie C"],
    "user3": ["Movie A", "Movie C", "Movie D"]
}

def recommend_movies(user_id):
    if user_id not in user_preferences:
        return []

    user_movies = user_preferences[user_id]
    recommended_movies = []

    for user, movies_list in user_preferences.items():
        if user != user_id:
            for movie in movies_list:
                if movie not in user_movies:
                    recommended_movies.append(movie)

    recommended_movies = list(set(recommended_movies))
    return recommended_movies[:5]

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data.get('user_id', '')
    recommendations = recommend_movies(user_id)
    return jsonify({'recommendations': recommendations})

if __name__ == '__main__':
    app.run(debug=True)
