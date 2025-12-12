from random_username.generate import generate_username

# welcome user
def welcomeUser():
    print("\nwelcome to the text analyse tool, I will mine and analyse a body of text from a file you give me!")

# Get Username

def getUsername():
    # Print message prompting the user to input their name
    usernamefrominput = input("\nTo begin, Please Enter Your Username:\n")

    if len(usernamefrominput) < 5 or not usernamefrominput.isidentifier():
        print("Your username must be aleast five character long, alphanumeric only (a-z/A-Z/0-9), have no spaces, and cannot start with a number")
        print("Assigning username instead n...")
        usernamefrominput = generate_username()[0]
        
    return usernamefrominput

# Greet the User
def greetUser(name):
    print("Hello, " + name)
    
welcomeUser()
username =  getUsername()
greetUser(username)