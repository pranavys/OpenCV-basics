movies_watched = {"ggvv", "kgf", "rsb"}
user_movie = input("Enter something you've watched recently: ").lower()

if user_movie in movies_watched:
    print(f"I have watched {user_movie} too!")

else:
    print("I haven't watched that yet.")


# Magic number
number = 7
user = input("Enter 'y' if you would like to play:").lower()

if user == "y":
# if user in ("y" "Y"):
# Alternative for lower()
    user_num = int(input("Guess out number: "))
    if user_num == number:
        print("Correct!!!")
    elif number - user_num in (1, -1):
    # elif abs(number - user_num) == 1:
    # abs() gives positive values
        print("You were off by one.")
    else:
        print("It's wrong :)")
        