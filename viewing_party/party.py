# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # check if title, genre, or rating is falsy
    if (not title) or (not genre) or (not rating):
        # return None
        return None
    # check if title_value and genre_value are string, rating is a float
    if (not isinstance(title, str)) or (not isinstance(genre, str)) or (not isinstance(rating, float)):
        # raise ValueError("Invalid input")
        return None
    # initialize empty dictionary
    new_movie = {}

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = float(rating)

    return new_movie


create_movie("Scream 6", "Horror", 4.0)


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


movie = {
    "title": "Lion King",
    "genre": "Family",
    "rating": 5.0
}
user_data = {"watched": []}

add_to_watched(user_data, movie)


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


movie = {
    "title": "Title A",
    "genre": "Horror",
    "rating": 3.5
}
user_data = {
    "watchlist": []
}
add_to_watchlist(user_data, movie)


def watch_movie(user_data, title):
    # iterate through each movie dictionary in the list
    for movie in user_data["watchlist"]:
        # checks if the title entered is found inside of the watchlist
        if title in movie["title"]:
            # move_movie captures the current movie found to be moved
            move_movie = movie
            # updates user_data to remove current movie from watchlist
            user_data["watchlist"].remove(movie)
            # updates user_data to add current movie to watched
            user_data["watched"].append(move_movie)
    # returns updated user_data
    return user_data


janes_data = {
    "watchlist": [{
        "title": "Super Man",
        "genre": "Action",
        "rating": 4.0
    }],
    "watched": []
}
watch_movie(janes_data, "Super Man")

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
