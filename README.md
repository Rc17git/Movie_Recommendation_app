# Movie Recommendation App

Welcome to the Movie Recommendation App! This application utilizes content-based filtering to provide personalized movie suggestions based on various movie details.

## Features

- **Content-Based Filtering:** The system analyzes movie details such as plot overview, cast, director, and keywords.
- **Vectorization Techniques:** TF-IDF and Count Vectorizer are used to generate a vector matrix for movie attributes.
- **Similarity Calculations:** Pairwise and cosine similarity methods are employed to recommend movies based on plot, actors, directors, etc.

## Technologies Used

- **Flask:** The web app is developed using the Flask framework.

## Getting Started
### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rc17git/Movie_Recommendation_app.git
   cd movie-recommendation-app
2. install dependencies:
   ```bash
   pip install -r requirements.txt
4. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate
6. Run the application:
   ```bash
   python app.py

### Contributing

If you'd like to contribute to this project, please follow the standard GitHub fork and pull request workflow.
