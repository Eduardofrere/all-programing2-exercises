import pandas as pd

movies_url = r"https://github.com/wesm/pydata-book/raw/refs/heads/3rd-edition/datasets/movielens/movies.dat"
ratings_url = r"https://github.com/wesm/pydata-book/raw/refs/heads/3rd-edition/datasets/movielens/ratings.dat"
users_url = r"https://github.com/wesm/pydata-book/raw/refs/heads/3rd-edition/datasets/movielens/users.dat"

# Column names
user_columns = ["user_id", "gender", "age", "occupation", "zip"]
movie_columns = ["movie_id", "title", "genres"]
rating_columns = ["user_id", "movie_id", "rating", "timestamp"]


movies=pd.read_table(movies_url, sep="::", engine="python" ,names=movie_columns )
ratings = pd.read_table(ratings_url, sep="::", engine="python",names=rating_columns)
users=pd.read_table(users_url ,sep="::" , engine= "python", names= user_columns)

data= pd.merge(ratings, users, on ="user_id")
data= pd.merge(data, movies, on ="movie_id")

occupation_bias= data.groupby("occupation")["rating"].mean().sort_values((ascending=false))
average_for_each = data.groupby("genres")["rating"].mean