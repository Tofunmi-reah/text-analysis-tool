from random_username.generate import generate_username
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger_eng')
wordLemmatizer = WordNetLemmatizer()
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

# Get the average word for sentences
def getwordsPerSentences(sentences):
    totalWords = 0
    for sentence in sentences:
       totalWords += len(sentence.split(" "))
    return totalWords / len(sentences)

# Covert part of speech from pos_tag function
# into wordnet compatible  pos tag
posToWordnetTag = {
    "J": wordnet.ADJ,
    "V": wordnet.VERB,
    "N": wordnet.NOUN,
    "K": wordnet.ADV,
}

def treebankPosToWordnetPos(partofspeech):
    posFirstChar = partofspeech[0]
    if posFirstChar in posToWordnetTag:
        return posToWordnetTag[posFirstChar]
    return wordnet.NOUN

# Convert raw list of (word, POS) tuple to a list of strings
# that only include valid english words
def cleanseWordList(posTaggedWordTuples):
    cleansedWords = []
    invalidWordPattern = "[^a-zA-Z-]"
    for posTaggedWordTuple in posTaggedWordTuples:
        word = posTaggedWordTuple[0]
        pos = posTaggedWordTuple[1]
        cleansedWord = word.replace(".", "").lower()
        if (not re.search(invalidWordPattern, cleansedWord)) and len(cleansedWord) > 1:
            cleansedWords.append(wordLemmatizer.lemmatize(cleansedWord, treebankPosToWordnetPos(pos)))
    return cleansedWords

    

# Get User Details
#welcomeUser()
#username =  getUsername()
#greetUser(username)

# Extract and tokenize text
articleTextRaw = getArticleText()
articleSentence = tokenizeSentences(articleTextRaw)
articleWords = tokenizeWords(articleSentence)

# Get  Sentences Analytics
stockSearchPattern = "[0-9]|[%$£€]|thousand|million|billion|trillion|profit|loss"
keySentences = extractKeySentences(articleSentence, stockSearchPattern)
wordsPerSentences = getwordsPerSentences(articleSentence)

# Get Word Analytics
wordsPosTagged = nltk.pos_tag(articleWords)
articleWordsCleansed = cleanseWordList(wordsPosTagged)

print("GOT:")  
print(wordsPosTagged)