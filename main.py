import re

# Assumption: the file is a plain text file with one tweet per line
tweets_file = "tweets.txt"
racial_slurs = {"asshole","freak","bastard","niggar","paki","moron"}
 # Assumption: a set of racial slurs is provided

# Function to calculate the degree of profanity for a given sentence
def calculate_profanity(sentence):
    # Split the sentence into words
    words = re.findall(r'\w+', sentence)
    # Count the number of racial slurs in the sentence
    num_slurs = len(set(words) & racial_slurs)
    # Calculate the degree of profanity as a percentage of total words
    profanity_degree = num_slurs / len(words) * 100 if len(words) > 0 else 0
    return profanity_degree

# Read in the tweets file and calculate the degree of profanity for each sentence
with open(tweets_file, "r") as f:
    tweets = f.readlines()
    for tweet in tweets:
        profanity_degree = calculate_profanity(tweet)
        print(f"Sentence: {tweet.strip()}, Profanity Degree: {profanity_degree:.2f}%")