from random_username.generate import generate_username
from nltk.tokenize import word_tokenize, sent_tokenize
import re

# welcome user
def welcomeUser():
    print("\nwelcome to the text analyse tool, I will mine and analyse a body of text from a file you give me!")

# Get Username

def getUsername():
    maxAttempts = 4
    attempts = 0

    while attempts < maxAttempts:
        
        # Print message prompting the user to input their name
        inputPrompt =""
        if attempts == 0:
            inputPrompt = "\nTo begin, Please Enter Your Username:\n"
        else:
            inputPrompt = "\nPlease try again:\n"
        usernameFromInput = input(inputPrompt)

        # Validate username
        if len(usernameFromInput) < 5 or not  usernameFromInput.isidentifier():
            print("Your username must be aleast five character long, alphanumeric only (a-z/A-Z/0-9), have no spaces, and cannot start with a number")
        else:
            return usernameFromInput
        
        attempts += 1

    print("Exhausted all " + str(maxAttempts) + " attempts, Assigning username instead...")
    return generate_username()[0]     

# Greet the User
def greetUser(name):
    print("Hello, " + name)

# Get text from file
def getArticleText():
    f = open("files/article.txt", "r")
    rawText = f.read()
    f.close()
    return rawText.replace("\n", " ").replace("\r", "")

#Extract Sentences from text raw Text body
def tokenizeSentences(rawText):
    return sent_tokenize(rawText)

# Extract words from list of sentencess
def tokenizeWords(sentences):
    words = []
    for sentence in sentences:
        words.extend(word_tokenize(sentence))
    return words

# Get the key sentences based on search pattern of key words
def extractKeySentences(sentences, searchPattern):
    matchedSentences = []
    for sentence in sentences:
        #if sentence matches desired patten, add to matchedSentences
        if re.search(searchPattern, sentence.lower()):
            matchedSentences.append(sentence)
    return matchedSentences
    

# Get User Details
#welcomeUser()
#username =  getUsername()
#greetUser(username)

# Extract and tokenize text
articleTextRaw = getArticleText()
articleSentence = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentence)

# Get Analytics
stockSearchPattern = "[0-9]|[%$£€]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentence, stockSearchPattern)

print("GOT:")
print(keySentences)