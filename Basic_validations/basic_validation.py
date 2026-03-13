def main():
    user_input = input("Enter your delusional sequence of characters: ")
    word = "moose"

    cleaned_input = clean_input(user_input)
    input_freq = char_freq(cleaned_input)

    print(cleaned_input)
    print(input_freq)

    if can_form(word, input_freq):
        print("YES the word can be formed")
        usused_chars = unused_chars(word, cleaned_input)
        print(usused_chars)
    else:
        print("No, the word can not be formed")


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
    word_freq = {}
    for char in word:
        if char not in word_freq:
            word_freq[char] = 1
        else:
            word_freq[char] += 1

    for letter in word_freq:
        if letter not in input_freq:
            return False
        if word_freq[letter] > input_freq[letter]:
            return False
    
    return True


def unused_chars(word, input_word):
    word_letters = list(word)
    unused_chars = []

    for char in input_word:
        if char in word_letters:
            word_letters.remove(char)
        else:
            unused_chars.append(char)
    
    return unused_chars


main()
