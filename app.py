from flask import Flask, render_template, request
import pandas as pd
from sklearn.metrics.pairwise import linear_kernel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from ast import literal_eval
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Read the CSV file and extract movie titles
movies_df = pd.read_csv('movies.csv')  # Replace 'movies.csv' with your CSV file path
movie_titles = movies_df['title'].tolist()

#Recommendation code 
tfidf = TfidfVectorizer(stop_words='english')
movies_df['overview'] = movies_df['overview'].fillna('')
tfidf_matrix = tfidf.fit_transform(movies_df['overview'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices = pd.Series(movies_df.index, index=movies_df['title']).drop_duplicates()
features = ['cast', 'crew', 'keywords', 'genres']
count = CountVectorizer(stop_words='english')
count_matrix = count.fit_transform(movies_df['soup'])
cosine_sim2 = cosine_similarity(count_matrix, count_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3]
    movie_indices = [i[0] for i in sim_scores]
    return movies_df['title'].iloc[movie_indices]


@app.route("/", methods=["GET", "POST"])
def index():
    selected_movie1 = ""
    selected_movie2 = ""
    result1 = ""
    result2 = ""

    if request.method == "POST":
        selected_movie1 = request.form.get("movie1")
        selected_movie2 = request.form.get("movie2")

        # Call the function to generate the list based on selected movies
        x=get_recommendations(selected_movie1, cosine_sim2)
        y=get_recommendations(selected_movie1, cosine_sim)
        U1 = x.append(y)
        U1=list(set(U1))
        x2=get_recommendations(selected_movie2, cosine_sim2)
        y2=get_recommendations(selected_movie2, cosine_sim)
        U2=x2.append(y2)
        U2=list(set(U2))
        result1 = "<br>".join(U1)
        result2 = "<br>".join(U2)

    return render_template(
        "index.html",
        movie_titles=movie_titles,  # Pass the movie titles as options
        selected_movie1=selected_movie1,
        selected_movie2=selected_movie2,
        result1=result1,
        result2=result2,
    )

if __name__ == "__main__":
    app.run()
