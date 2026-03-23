def main(): # Entry point: handles input validation, processing, and output flow
    # taking user input
    user_input = input("Enter your delusional sequence of letters: ")

    # Remove spaces to validate that input contains only alphabetic characters
    temp_input = user_input.replace(" ", "")

    # Reject input if it contains non-alphabetic characters
    if not temp_input.isalpha():
        print("You must enter alphabatical letters only!")
    else:
        cleaned_input = clean_input(user_input) # Normalize input by removing spaces and converting to lowercase
        input_freq = char_freq(cleaned_input) # Build frequency map of input letters for comparison with dictionary words

        words = load_dictionary() # Load list of valid words from dictionary file

        # Filter dictionary words that can be formed from input letters also compute unused letters for each valid word
        valid_words = result_words(words, cleaned_input, input_freq) 
       
        output_formatting(valid_words, cleaned_input) # this is for only output given by the program. it is formatted for better understanding.
    
# cleaning input function
def clean_input(word):
    return word.replace(" ", "").lower()
    
# character frequency making function
def char_freq(word):
    freq = {}

    for char in word:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    return freq

# Check if a word can be formed using the available input letter frequencies
def can_form(word, input_freq):
    word_freq = char_freq(word)

    for char in word_freq:
        if char not in input_freq:
            return False
        if word_freq[char] > input_freq[char]:
            return False
        
    return True

# Return letters from input that are not used when forming the given word
def unused_Chars(word, input):
    word_freq = list(word)

    unused_chars = []

    for char in input:
        if char in word_freq:
            word_freq.remove(char)
        else:
            unused_chars.append(char)
    
    return unused_chars

# loading dictionary function
def load_dictionary():
    with open("english_words.txt", "r") as dict:
        word_list = []
        for word in dict:
            word_list.append(word.strip().lower())
        
        return word_list
    
# checking the word and conduction can_form() from earlier
def result_words(words, user_input, input_freq):
    result = []
    for word in words:
        if len(word) > len(user_input):
            continue

        if can_form(word, input_freq):
            unused_chars = unused_Chars(word, user_input)
            result.append((word, unused_chars))
        
    return result

# Display results in a readable format
def output_formatting(valid_words, user_input):
    if valid_words:
        print(f"Your input is {user_input}")
        for word, unused in valid_words:
            print(f"Words: {word} | Unused -> {unused}")
        print(f"Total {len(valid_words)} words formed.")
    else:
        print(f"Your input is {user_input}")
        print("No word can be formed from this input.")

main()