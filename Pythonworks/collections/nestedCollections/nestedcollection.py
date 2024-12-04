

movies=[
    {"id":1,"title":"kgf","year":2018,"language":"kannada","run_time":150},
    {"id":2,"title":"kgf2","year":2023,"language":"kannada","run_time":160},
    {"id":3,"title":"goat life","year":2024,"language":"malayalam","run_time":120},
    {"id":4,"title":"avesham","year":2024,"language":"malayalam","run_time":130},
    {"id":5,"title":"vazha","year":2024,"language":"malayalam","run_time":140},
    {"id":6,"title":"arm","year":2024,"language":"malayalam","run_time":150},
    {"id":7,"title":"goat","year":2024,"language":"tamil","run_time":160},

]

highest_runtime_movie=max(movies,key=lambda d:d.get("run_time"))

hightest_time=highest_runtime_movie.get("run_time") #160

# max_run_time_movies=[ for m in movies if m.get("run_time")==hightest_time]


# movies released in 2024

movie_year_filter=[m.get("title") for m in movies if m.get("year")==2024]
# print(movie_year_filter)

# malayalam movie titles

# malayalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]

# print(malayalam_movies)
# movie with highest runtime



# malayalm movie counts
# in which year most number of movies released


# malayalam_movies=[m.get("title") for m in movies if m.get("language")=="malayalam"]

# print(len(malayalam_movies))

all_years=[m.get("year") for m in movies ]

# [2018, 2023, 2024, 2024, 2024, 2024, 2024]
# {2018:1,2023:1,2024:5}

year_count={y:all_years.count(y) for y in all_years}
print(year_count)