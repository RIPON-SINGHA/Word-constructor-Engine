def main():
    user_input = input("Enter your delusional sequence of characters: ")

    cleaned_input = clean_input(user_input)
    input_freq = char_freq(cleaned_input)

    print(cleaned_input)
    print(input_freq)

    if can_form("cab", input_freq):
        print("YES the word can be formed")
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


main()
