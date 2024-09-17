def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Get number of words.
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.")

    # Get the total number of each single chars.
    num_chars = get_count_chars(text)


def get_count_chars():
    # Create an empty dict.
    chars_dict = {}
    # Iterate each char in the string.
    for char in string:
        # Convert the char in lowercase.
        char = char.lower()
        # Check if char already exists.
        if char in chars_dict:
            # If it does increment by 1.
            chars_dict[char] += 1
        else:
            # If it does not initialize it to 1.
            chars_dict[char] = 1


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
