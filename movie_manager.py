movie_list = []

def display_menu():
    print("\n===== FAVOURITE MOVIE MANAGER =====")
    print("1. Add a Movie.")
    print("2. Remove a Movie.")
    print("3. View all Movies.")
    print("4. Search a movie.")
    print("5. Count Total Movies.")
    print("6. Sort Movies.")
    print("7. EXIT.")

def add_movie():
    movie = input("Enter movie name: ").title()
    movie_list.append(movie)
    print(f"{movie} added successfully!")

def remove_movie():
    movie = input("Enter movie to remove: ").title()
    if movie in movie_list:
        movie_list.remove(movie)
        print(f"{movie} removed.")
    else:
        print(f"{movie} not found.")

def view_movies():
    if movie_list:
        print("\n🎬 Your Movies: ")
        for idx, movie in enumerate(movie_list, start=1):
            print(f"{idx}.{movie}") 
    else:
        print("No movies in the list yet.")

def search_movie():
    movie = input("Enter movie to search: ").title()
    if movie in movie_list:
        print(f"{movie} is in your collection!")
    else:
        print(f"{movie} Not found!")

def count_movies():
    print(f"Total Movies in your collection: {len(movie_list)}")

def sort_movies():
    movie_list.sort()
    print("Movie List sorted A-Z.")

while True:
    display_menu()
    choice = input("Enter Your choice (1-7): ")

    if choice == '1':
        add_movie()
    elif choice == '2':
        remove_movie()
    elif choice == '3':
        view_movies()
    elif choice == '4':
        search_movie()
    elif choice == '5':
        count_movies()
    elif choice == '6':
        sort_movies()
    elif choice == '7':
        print("Thanks for using Movie Manager, Have Fun!")
        break 
    else:
        print("INVALID CHOICE: Try Again...")