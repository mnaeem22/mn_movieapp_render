import requests
import os

class TMDBService:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'https://api.themoviedb.org/3'
    
    def search_movie(self, title):
        """Search for movies by title"""
        url = f'{self.base_url}/search/movie'
        params = {
            'api_key': self.api_key,
            'query': title
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get('results', [])
        return []
    
    def get_movie_recommendations(self, movie_id):
        """Get movie recommendations based on movie ID"""
        url = f'{self.base_url}/movie/{movie_id}/recommendations'
        params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'page': '1'
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            data = response.json()
            return data.get('results', [])
        return []