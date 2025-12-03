# welcome user
def welcomeUser():
    print("welcome to the text analyse tool, I will mine and analyse a body of text from a file you give me!")

# Get username

def getUsername():
    # Print message prompting the user to input their name
    usernamefrominput = input("\nTo begin, Please Enter Your Username:\n")
    return usernamefrominput

# Greet the User
def greetUser(name):
    print("Hello, " + name) 

def runprogram():
    welcomeUser()
    username =  getUsername()
    greetUser(username)
runprogram()