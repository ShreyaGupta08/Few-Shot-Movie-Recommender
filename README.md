# MOVIE RECOMMENDER

This project provides a movie recommendation system based on user's top movie choices. Given a list of top movies, the system uses the OpenAI GPT API to generate movie recommendations tailored to the user's preferences.

## Server
The server code (server.py) is responsible for handling API requests and generating movie recommendations using the GPT API. It is built using Flask, a Python web framework.

### Dependencies
Python 3.x

Flask

Requests

### Setup

1. Make sure you are in the code directory by running the following:
```
$cd <path to file>
$unzip movie_reco.zip
$cd movie_reco.zip
```

2. Set the OpenAI API key as an environment variable:
```
$export OPENAI_API_KEY=<your-api-key>
```
Replace <your-api-key> with your actual OpenAI API key. 

3. Build the docker image by running the command:

```
$docker build -t movie_recommender .
```

this will install all the dependecies and create the static docker image needed to run the following pipeline.

4. Run the docker image created:

```
$docker run -p 5000:5000 -e OPENAI_API_KEY -t movie_recommender
```

The server will start running inside the Docker container on http://localhost:5000.

## API Endpoint

* /api/get_recommendation (POST): Accepts a JSON payload containing the user's top movies and returns a JSON response containing the movie recommendation. 

Request made to the server:
```
{
  "top_movies": ["movie1", "movie2", "movie3"]
}
```
Respnse received:
```
{
  "recommendation": "Recommended movie 1, Recommended movie 2, Recommended movie 3"
}
```

## CLIENT

The client code (movie_reco_client.py) demonstrates how to send a request to the server and retrieve movie recommendations based on the user's top movies.

### Dependencies
Python 3.x
  
Requests

### Setup
  
1. Set the server IP and port in the client code (movie_reco_client.py) by updating the server_ip and port variables. (if you are running client and server on the same machine, this step is not needed).

2. Now we are ready to get recommendations! In a new terminal, run the client code which will ask the server for movie predictions:

```
$python movie_reco_client.py movie1 movie2 movie3 movie4
```
Replace movie1, movie2, movie3, etc., with the actual top movies of the user.

The client will send a POST request to the server with the top movies and print the movie recommendations received from the server. You can feed the program as many movies as you want. 

Note: If a movie consists of more than one word, insert it with an underscore separation. for example, if you want to give the movie 'Men In Black', input 'Men_in_Black' (the code will deal with the rest).

Make sure to replace <your-api-key> in the README with your actual OpenAI API key.

That's it! The terminal will output the movie recommendations for the user. Happy Watching!
