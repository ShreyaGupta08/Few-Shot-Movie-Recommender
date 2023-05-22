import sys
import requests


server_ip = '0.0.0.0'
port = '5000'
base_url = f"http://{server_ip}:{port}"

def get_top_movies():
    """
    Get the top movies from the command line arguments.

    Returns:
        list: List of top movies.
    """
    top_movies = sys.argv[1:]
    for idx, movie in enumerate(top_movies):
        mov_split = movie.split("_")
        top_movies[idx] = " ".join(mov_split)
    return top_movies

if __name__=='__main__':
    # Get the top movies from command line arguments
    top_movies = get_top_movies()
    print("movies: ", top_movies)
    # Create the URL for the API endpoint
    url = base_url + "/api/get_recommendation"

    # Send a POST request to the server with the top movies
    response = requests.post(url, json={'top_movies': top_movies})

    # Get the movie recommendations from the response
    movie_reco = response.json()['recommendation']

    # Print the movie recommendations
    print(movie_reco)
