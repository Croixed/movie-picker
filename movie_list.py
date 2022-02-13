import os, random

def pick_movie_list(dir, length):
    """Return a random list of movies."""
    picked_movie_list = []
    for num in range(length):
        ran_movie = random.choice(os.listdir(dir))
        ran_movie = ran_movie.replace('.', ' ')
        picked_movie_list.append(ran_movie)
    return picked_movie_list

def get_length(dir):
    """Return total number of folders in this directory."""
    folder_count = len(os.listdir(dir))
    return folder_count

def print_list_result(count, movie, folder):
    """Prints a neatly formatted list of movie titles."""
    print(f"\ncurrent Folder: {folder}")
    print(f"There are {count} movies in this folder.")
    print(f"The next movies you can watch are:")
    for film_name in movie:
        print(f"\t{film_name}")


active_folder = "Z:\\UNWATCHED"
chosen_movies = pick_movie_list(active_folder, 3)
movie_total = get_length(active_folder)

print_list_result(movie_total, chosen_movies, active_folder)