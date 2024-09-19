def main():
    print("--- Begin report of books/frankenstein.txt ---")
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    # Get number of words.
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document.")

    print("")

    # Get the total number of each single chars.
    num_chars = get_count_chars(text)

    list_of_dict = convert_dict_to_a_list_of_dict(num_chars)

    sorted_list = statistics_about_each_word(list_of_dict)

    for item in sorted_list:
        # Check if the key is a character.
        if item['key'].isalpha() is True:
            print(f"The '{item['key']}' character was found {item['value']} times.")


def statistics_about_each_word(list):
    return sorted(list, key=lambda x: x.get('value'), reverse=True)


def convert_dict_to_a_list_of_dict(dict_of_chars):
    # return [{key: value} for key, value in dict_of_chars.items()]
    new_list = []
    for k, v in dict_of_chars.items():
        new_list.append({'key': k, 'value': v})
    return new_list


def get_count_chars(text):
    # Create an empty dict.
    chars_dict = {}
    # Iterate each char in the string.
    for char in text:
        # Convert the char in lowercase.
        char = char.lower()
        # Check if char already exists.
        if char in chars_dict:
            # If it does increment by 1.
            chars_dict[char] += 1
        else:
            # If it does not initialize it to 1.
            chars_dict[char] = 1
    return chars_dict


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


if __name__ == "__main__":
    main()
