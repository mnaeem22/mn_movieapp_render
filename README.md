# Movie Recommendation App

A Flask-based web application that provides movie recommendations using The Movie Database (TMDB) API.

## 🎬 Application Functionality

### Overview
This application allows users to search for movies and get personalized recommendations based on their selected movie. It leverages the TMDB API to fetch real-time movie data and recommendations.

### Core Features

1. **Movie Search**
   - Enter any movie title in the search box
   - Retrieves matching movies from TMDB database
   - Displays movie posters and titles in a card-based layout

2. **Movie Recommendations**
   - Click "Get Recommendations" on any movie
   - Fetches similar movies based on the selected movie
   - Shows recommended movies with overview/description

3. **User Interface**
   - Clean, responsive design using Bootstrap
   - Card-based movie display with posters
   - Easy navigation between search and recommendations

## 📖 How to Use This App

### Home Page (`/`)

The home page is your starting point for discovering movies and getting recommendations.

**Step-by-Step Guide:**

1. **Access the Application**
   - Open your web browser
   - Navigate to `http://127.0.0.1:5000`
   - You'll see the Movie Recommendation App homepage

2. **Search for a Movie**
   - Locate the search box at the top of the page
   - Type in a movie title (e.g., "The Matrix", "Inception", "Avatar")
   - Click the "Search Movies" button or press Enter

3. **View Search Results**
   - The app displays matching movies in a grid layout
   - Each movie shows:
     - Movie poster image
     - Movie title
     - "Get Recommendations" button

4. **Browse Multiple Results**
   - Scroll through the search results
   - Results are displayed in cards (3 per row on desktop)
   - Each card represents a different movie match

5. **Get Recommendations**
   - Find a movie you're interested in
   - Click the "Get Recommendations" button on that movie's card
   - You'll be taken to the recommendations page

6. **Explore Recommendations**
   - View a curated list of similar movies
   - Each recommendation includes:
     - Movie poster
     - Title
     - Brief overview/plot summary
   
7. **Return to Search**
   - Click the "Back to Search" button at the bottom of the recommendations page
   - Start a new search or explore different movies

### Quick Tips

- **Be Specific**: More specific movie titles yield better results
- **Try Different Searches**: If you don't find what you're looking for, try alternative titles
- **Explore Recommendations**: Use recommendations to discover movies you might have missed
- **Mobile Friendly**: The app works great on mobile devices too!

## 🏗️ How It Works

### Architecture

```
User Interface (Templates)
    ↓
Routes (Blueprint: main)
    ↓
Services (TMDBService)
    ↓
TMDB API
```

### Component Breakdown

#### 1. **Frontend Layer** (`app/templates/`)
- `base.html`: Base template with common HTML structure and Bootstrap styling
- `index.html`: Search page with movie results display
- `recommendations.html`: Recommendations display page

#### 2. **Routing Layer** (`app/routes.py`)
- Uses Flask Blueprint (`main`) for organized routing
- Two main endpoints:
  - `/` (GET/POST): Handles movie search and displays results
  - `/recommendations/<movie_id>` (GET): Displays recommendations for a specific movie

#### 3. **Service Layer** (`app/services.py`)
- `TMDBService` class handles all API interactions
- Methods:
  - `search_movie(title)`: Searches TMDB for movies matching the title
  - `get_movie_recommendations(movie_id)`: Fetches similar movies from TMDB

#### 4. **Configuration** (`config.py`)
- Loads environment variables
- Manages API keys and secret keys
- Supports both environment variables and `.env` file

#### 5. **Application Factory** (`app/__init__.py`)
- `create_app()` function initializes the Flask app
- Registers blueprints
- Loads configuration

## 🔧 Technical Details

### API Integration
The app communicates with TMDB API v3:
- **Search Endpoint**: `https://api.themoviedb.org/3/search/movie`
- **Recommendations Endpoint**: `https://api.themoviedb.org/3/movie/{movie_id}/recommendations`

### Request Flow

1. **Search Flow**:
   ```
   User enters movie title → POST / → routes.index() 
   → TMDBService.search_movie() → TMDB API → Returns movie list 
   → Renders index.html with results
   ```

2. **Recommendation Flow**:
   ```
   User clicks "Get Recommendations" → GET /recommendations/{id} 
   → routes.recommendations() → TMDBService.get_movie_recommendations() 
   → TMDB API → Returns recommendation list 
   → Renders recommendations.html
   ```

## 📦 Project Structure

```
movie_recommendation_app/
├── app/
│   ├── templates/
│   │   ├── base.html          # Base HTML template
│   │   ├── index.html         # Search page
│   │   └── recommendations.html # Recommendations page
│   ├── __init__.py            # App factory
│   ├── routes.py              # Route handlers (Blueprint)
│   └── services.py            # TMDB API service
├── config.py                  # Configuration settings
├── run.py                     # Application entry point
├── requirements.txt           # Python dependencies
└── .env                       # Environment variables
```

## 🚀 Running the Application

### Prerequisites
- Python 3.x
- Virtual environment (included in `movie/` directory)
- TMDB API key (pre-configured in `.env`)

### Local Development Setup

1. **Navigate to project directory**:
   ```bash
   cd movie_recommendation_app
   ```

2. **Activate virtual environment** (Windows PowerShell):
   ```powershell
   .\movie\Scripts\Activate.ps1
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment** (optional - already configured):
   Edit `.env` file with your TMDB API key:
   ```
   TMDB_API_KEY=your_api_key_here
   ```

5. **Run the application**:
   ```bash
   python run.py
   ```

6. **Access the app**:
   Open browser and navigate to: `http://127.0.0.1:5000`

### Production Deployment (Render)

This app is ready for deployment on Render! See [`DEPLOYMENT.md`](DEPLOYMENT.md) for detailed instructions.

**Quick Deploy Steps:**
1. Push code to GitHub
2. Create new Web Service on Render
3. Connect your repository
4. Set environment variables (`TMDB_API_KEY`, `FLASK_ENV`)
5. Deploy!

Your app will be live at: `https://your-app-name.onrender.com`

## 🛠️ Technology Stack

- **Flask** (2.0.1): Web framework
- **Werkzeug** (2.0.1): WSGI utilities
- **Requests** (2.32.0): HTTP library for API calls
- **python-dotenv** (0.19.2): Environment variable management
- **Bootstrap**: Frontend CSS framework (via CDN)
- **Jinja2**: Template engine

## 🎯 Key Implementation Details

### Blueprint Pattern
The app uses Flask Blueprint (`main`) for better organization:
```python
bp = Blueprint('main', __name__)
```
All routes are registered under this blueprint, requiring endpoint references to use `main.endpoint_name`.

### Service Layer Pattern
Business logic is separated into `TMDBService`:
- Decouples API logic from routes
- Makes testing and maintenance easier
- Single responsibility principle

### Environment Configuration
API keys and secrets are loaded from environment variables:
```python
TMDB_API_KEY = os.environ.get('TMDB_API_KEY', 'default_key')
SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_hex(16))
```

## 📝 Notes

- The app runs in debug mode by default (auto-reload on code changes)
- All movie data comes from TMDB API in real-time
- No database storage - purely a proxy to TMDB
- Responsive design works on desktop and mobile devices

## 🔑 TMDB API

The app uses The Movie Database (TMDB) API to fetch movie data. You can get your own free API key from: https://www.themoviedb.org/settings/api

## 📄 License

This project is for educational purposes. Movie data and images are provided by TMDB and subject to their terms of use.
