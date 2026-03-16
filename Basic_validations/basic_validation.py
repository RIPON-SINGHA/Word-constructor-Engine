def main():
    user_input = input("Enter your delusional sequence of letters: ")
    
    valid_words = []
    temp_input = user_input.replace(" ", "")

    if not temp_input.isalpha():
        print("You must enter alphabatical letters only!")
    else:
        cleaned_input = clean_input(user_input)
        input_freq = char_freq(cleaned_input)

        words = load_dictionary()

        for word in words:
            if len(word) > len(cleaned_input):
                continue
            
            if can_form(word, input_freq):
                    unused_chars = unused_Chars(word, cleaned_input)
                    valid_words.append((word, unused_chars))
        
        if len(valid_words) == 0:
            print(f"Your Input is: {cleaned_input}")
            print("No words can be formed from this input.")
        else:        
            print(f"Your Input is: {cleaned_input}")
            for word, unused in valid_words:
                print(f"{word} -> unused: {unused}")
            print(f"Total {len(valid_words)} words formed")
                
    

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
    with open("words.txt", "r") as dict:
        word_list = []
        for word in dict:
            word_list.append(word.strip().lower())
        
        return word_list

main()