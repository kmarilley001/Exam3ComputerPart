###############################################################################
# DONE: 1. (3 pts)
#
#   For this module, we are going to create a basic program to handle movie
#   times at a movie theater. For our purposes, a movie is going to be defined
#   as a dictionary with these keys:
#       - title
#       - duration
#       - start_time
#       - theater_num
#       - num_of_tickets
#
#   For this __todo__, write a function called show_movies() that takes one
#   argument:
#       - movies     <-- list of dictionaries (movies)
#
#   First, it should print the line:
#       Movies:
#   
#   Then, This function should loop through the list of movies and, for each
#   movie, print information about the movie like so:
#
#       Title: Braveheart
#       Duration: 170 minutes
#       Start Time: 2:15 PM
#       Theater: 8
#       Tickets Available: 20
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# In this session i have defined a function that takes the parameter movies. Created a for loop that would take the dictionary made and run it through loop of the parameter(movies) and print the list. The dictionary is enclosed in a list because when I didn't enclose in a list I would run the code and seeing the output multiple times. 
def show_movies(movies): 
    print("Movies: ")
    for movie in movies: 
        print ("Title:", movie["title"])
        print("Duration:", movie["duration"], "minutes")
        print("Start Time:", movie["start_time"])
        print("Theater:", movie["theater_num"])
        print("Tickets Available:", movie["num_of_tickets"])
        print()

movies = [{"title": "Braveheart", 
          "duration": 170,
          "start_time": "2:15 PM", 
          "theater_num": 8, 
          "num_of_tickets": 20}]
show_movies(movies)
        
    
###############################################################################
# DONE: 2. (3 pts)
#
#   For this _todo_, write a function called get_ticket() that takes one
#   parameter:
#       - movie      <-- dictionary (movie)
#
#   This function should behave like this:
#
#       - If the movie has tickets available (that is, it is greater than 0), it
#         should set the value of num_of_tickets to one less than what it was
#         before and print:
#           "Success! You know have a ticket for <MOVIE TITLE HERE>!"
#       - If the movie's num_of_tickets value is not greater than 0 (that is,
#         it is there are not tickets available), it should print:
#           "There are currently no tickets available for that movie."
#
#   HINT: Remember that you will need to convert the number of tickets to an
#   integer
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
# define a function that takes the parameter movie and inside the function it checks the number of tickets available given by the num_of_tickets key in the dictionary called movies. If are available it reduces the number of tickets available by 1 and prints a success and if no tickets available it would print a message indicating there is no more tickets. 
def get_ticket(movie): 
    if movie["num_of_tickets"] > 0:
        movie["num_of_tickets"] -= 1 
        print("Success! You know have a ticket for" + movie["title"])
    else: 
        print("There are currently no tickets available for that movie.")

    
###############################################################################
# DONE: 3. (9 pts)
#
#   Now, let's create our movie showtimes system.
#
#   For this _todo_, write a function called main() that will start things off.
#   This function should do these things in order:
#
#       1. Print a welcome message to the user
#       2. Continually ask the user for information about movies (title,
#          duration (in minutes), start time, theater number, tickets
#          available). If the user types "end" for any of the fields, the
#          program should stop asking for movie information. (HINT: I used a
#          while loop)
#       3. For each movie, create a dictionary to hold the movie's information.
#          The dictionary should have all of this information: title, duration,
#          start_time, theater_num, num_of_tickets.
#       4. It should keep track of all the movies in a list.
#       5. Once the user stops entering movie information, the program should
#          use the show_movies() function to print the list of movies and their
#          information.
#       6. Then, the program should continually prompt the user like so:
#           "Which movie would you like to buy a ticket for? "
#       7. If the user types a movie title that is in the list of movies, it
#          should get a ticket for the user (using the get_ticket() function)
#          and reprint the list of movies with the updated information. It
#          should keep asking the user for more movies to get tickets for until
#          they type "end".
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################
#Defines a main function and welcomes user and starts an empty list called movies to stor info. creates a loop to prompt user to input movie details and that info is stored in a dictionary and appended to a list. after that list of available movies are shown creating a loop in which a user can purchase tickets. 
def main(): 
    print("Welcome to Movie Showtime Center!")
    
    movies = [] 

    while True: 
        title = input("Enter the movie title (type 'end' to finish): ")
        if title.lower() == 'end': 
            break 

        duration = int(input("Enter the duration of the movie in minutes: "))
        start_time = input("Enter the start time of the movie: ")
        theater_num = int(input("Enter the theater number: "))
        num_of_tickets = int(input("Enter the number of tickets available: "))

        movie = {"title": title, 
                 "duration": duration,
                 "start_time": start_time, 
                 "theater_num": theater_num,
                 "num_of_tickets": num_of_tickets}
        
        movies.append(movie)

    show_movies(movies)  # Moved inside the main function

    while True: 
        option = input("Which movie would you like to buy a ticket for? (or 'end' to finish): ")
        if option.lower() == 'end': 
            break 
        
        found = False
        for movie in movies:
            if option.lower() == movie['title'].lower(): 
                get_ticket(movie)
                found = True 
                break 

        if not found: 
            print("Movie is not found. Please try again.")

        show_movies(movies) 
main()



