def main():
    user_input = input("Enter your delusional sequence of characters: ")

    cleaned_input = clean_input(user_input)
    input_freq = char_freq(cleaned_input)

    print(cleaned_input)
    print(input_freq)


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

main()