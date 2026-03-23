def main():
    user_input = input("Enter your delusional sequence of letters: ")
    
    temp_input = user_input.replace(" ", "")

    if not temp_input.isalpha():
        print("You must enter alphabatical letters only!")
    else:
        cleaned_input = clean_input(user_input)
        input_freq = char_freq(cleaned_input)

        words = load_dictionary()

        valid_words = result_words(words, cleaned_input, input_freq)
       
        output_formatting(valid_words, cleaned_input)
    

def clean_input(word):
    return word.replace(" ", "").lower()
    

def char_freq(word):
    freq = {}

    for char in word:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    
    return freq


def can_form(word, input_freq):
    word_freq = char_freq(word)

    for char in word_freq:
        if char not in input_freq:
            return False
        if word_freq[char] > input_freq[char]:
            return False
        
    return True


def unused_Chars(word, input):
    word_freq = list(word)

    unused_chars = []

    for char in input:
        if char in word_freq:
            word_freq.remove(char)
        else:
            unused_chars.append(char)
    
    return unused_chars


def load_dictionary():
    with open("english_words.txt", "r") as dict:
        word_list = []
        for word in dict:
            word_list.append(word.strip().lower())
        
        return word_list
    

def result_words(words, user_input, input_freq):
    result = []
    for word in words:
        if len(word) > len(user_input):
            continue

        if can_form(word, input_freq):
            unused_chars = unused_Chars(word, user_input)
            result.append((word, unused_chars))
        
    return result


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