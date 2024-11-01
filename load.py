import json
from difflib import get_close_matches

# Load the JSON data
def load_data():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data

# Function to get word definition
def get_definition(word, dictionary):
    # Normalize the word to lowercase
    word = word.lower()
    
    # Check if the word exists in dictionary
    if word in dictionary:
        return dictionary[word]
    
    # Suggest similar words if the word is not found
    else:
        # Get close matches to the word
        matches = get_close_matches(word, dictionary.keys(), cutoff=0.8)
        
        if matches:
            suggestion = matches[0]
            return f"Did you mean '{suggestion}'? Definition: {dictionary[suggestion]}"
        else:
            return "The word doesn't exist in the dictionary."

# Main program
def main():
    # Load dictionary data
    dictionary = load_data()
    
    # Input from user
    word = input("Enter a word: ")
    
    # Fetch definition
    result = get_definition(word, dictionary)
    print(result)

if __name__ == "__main__":
    main()
