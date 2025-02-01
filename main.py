def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letters_sorted_list = count_characters(text)


    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()

    for item in letters_sorted_list:
        if not item["letter"].isalpha():
            continue
        print(f"The '{item['letter']}' character was found {item['counter']} times")

    print("--- End report ---")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["counter"]

def count_characters(text):
    letters = {}
    letters_sorted = []
    lowered_text = text.lower()
    #new_dict = {}
    
    for char in lowered_text:
        if char in letters:
            letters[char] += 1
        else:
            letters[char] = 1
    #print(letters)
    
    for character in letters:
        new_dict = {}
        if character.isalpha():
            new_dict["letter"] = character
            new_dict["counter"] = letters[character]

            letters_sorted.append(new_dict)
    letters_sorted.sort(reverse=True, key=sort_on)
    return letters_sorted

main()