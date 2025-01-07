def main():
    book_path = "books/frankenstein.txt"

    text = get_text(book_path)
    counter = get_word_count(text)
    chars_dict = get_letter_count(text)
    characters = sort_chars(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{counter} words found in the document")
    print()

    for item in characters:
        if not item["char"].isalpha():
            continue
        print(f"The {item['char']} character was found {item['num']} times")
    
    print("--- End report ---")

def sort_on(d):
    return d["num"]

def sort_chars(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char" : char, "num" : num_chars_dict[char]})
    sorted_list.sort(reverse=True, key = sort_on)
    return sorted_list
    
def get_letter_count(text):
    words = text.split()
    dict = {}
    for string in words:
        string = string.lower()
        for i in string:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
    return dict


def get_word_count(text):
    words = text.split()
    return len(words)


def get_text(book_path):
    with open(book_path) as f:
        return f.read()


main()