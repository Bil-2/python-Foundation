class Movie:
    def __init__(self, name, price, available_tickets):
        self.name = name
        self.price = price
        self.available_tickets = available_tickets

def display_movies(movies):
    print("\nAvailable Movies:")
    for index, movie in enumerate(movies, start=1):
        print(f"{index}. {movie.name} (Ticket Price: ${movie.price}, Available: {movie.available_tickets})")

def main():
    print("Welcome to the Movie Ticket Booking System!")

    # Create the list of movies
    movies = [
        Movie("The Avengers", 12, 50),
        Movie("Inception", 10, 40),
        Movie("Interstellar", 15, 30)
    ]

    while True:
        display_movies(movies)
        try:
            choice = int(input("\nEnter the number of the movie you want to watch (0 to exit): "))
            if choice == 0:
                print("Thank you for using the system. Goodbye!")
                break
            if choice < 1 or choice > len(movies):
                print("Invalid choice. Please select a valid movie number.")
                continue

            selected_movie = movies[choice - 1]
            if selected_movie.available_tickets == 0:
                print(f"Sorry, no tickets are available for {selected_movie.name}.")
                continue

            tickets = int(input(f"How many tickets do you want for {selected_movie.name}? "))
            if tickets <= 0:
                print("Number of tickets must be at least 1.")
                continue
            if tickets > selected_movie.available_tickets:
                print(f"Only {selected_movie.available_tickets} tickets are available. Please choose a smaller number.")
                continue

            total_cost = tickets * selected_movie.price
            selected_movie.available_tickets -= tickets

            print(f"\nYou have successfully booked {tickets} tickets for {selected_movie.name}.")
            print(f"Total Cost: ${total_cost}")
            print(f"Remaining Tickets for {selected_movie.name}: {selected_movie.available_tickets}")

        except ValueError:
            print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    main()
