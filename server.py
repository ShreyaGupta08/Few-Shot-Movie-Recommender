from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

def get_openai_key():
    """
    Retrieve the OpenAI API key from an environment variable.

    Returns:
        str: OpenAI API key.
    """
    key = os.environ.get('OPENAI_API_KEY')
    if not key:
        raise ValueError("OpenAI API key not found")
    return key

def generate_recommendation(top_movies):
    """
    Generate movie recommendations based on the user's top movies using the GPT API.

    Args:
        top_movies (list): A list of top movies.

    Returns:
        str: Movie recommendations.
    """
    api_url = "https://api.openai.com/v1/chat/completions"
    prompt = "Can you get me movie recommendations based on these movies I like: " + ", ".join(top_movies) + "."
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + get_openai_key()
    }
    data = {
        'model': "gpt-3.5-turbo",
        'messages':[{
            "role": "user",
            "content": prompt
        }],
        'max_tokens': 100,
        'temperature': 0.3
    }
    response = requests.post(api_url, json=data, headers=headers)
    recommendation = response.json()['choices'][0]['message']['content'].strip()
    return recommendation

@app.route('/api/get_recommendation', methods=['POST'])
def get_recommendation():
    """
    Handle the API request to generate movie recommendations.

    Returns:
        dict: A JSON response containing the movie recommendation.
    """
    args = request.get_json()
    top_movies = args['top_movies']

    # Generate movie recommendations using the GPT API
    recommendation = generate_recommendation(top_movies)
    return jsonify({'recommendation': recommendation})


if __name__=='__main__':
    # Run the Flask app
    app.run(host='0.0.0.0', threaded=True, processes=1)
