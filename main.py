from database_link import *

def new_user():
    user_name = (input("Enter the new users name: "))
    try:
        ict_score = int(input("Enter the new users ict score: "))
        maths_score = int(input("Enter the new users maths score: "))
        chemistry_score = int(input("Enter the new users chemistry score: "))
    except ValueError:
        print("Score must be a number between 0 and 100.")
        return
    if user_name.replace(' ', '').isalpha():
        fetch_data(user_name)
    else:
        print("invalid name")
        return

    if (ict_score >= 0 and ict_score <= 100 and maths_score >= 0 and maths_score <= 100 and chemistry_score >= 0 and chemistry_score <= 100):
        insert_data(user_name, ict_score, maths_score, chemistry_score)
    else:
        print("Score must be a number between 0 and 100.")

#Code above is for inserting new user data into database, calls function in another file

def view_database():
    user_name = (input("Enter the users name: "))
    if user_name.replace(' ', '').isalpha():
        for x in fetch_data(user_name):
            print(x)
    else:
        print("invalid name")

    return()

#Code above calls function in other file, returns data from database

print ("Would you like to view results or add a new user?")

while True:
    user_option = (input("Enter 'results' or 'new user' to choose: "))
    if user_option == ("results" or "Results"):
        view_database()
    elif user_option == ("new user" or "New User"):
        new_user()
    else:
        print ("Invalid response.")

    if (input("Continue? Y/N: ")) != "Y":
        break



#other things that need doing:
#Uploading the whole thing to GIT (bit by bit hopefully)
#BONUS: have a seperate python class for database link code
