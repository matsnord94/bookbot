def main():
    book_path = "books/frankenstein.txt"
    bok = book_text(book_path).lower()
    counted_words = count_words(bok)
    counted_characters = count_characters(bok)
    counted_characters_in_tuples = convert_dict_counts_to_tuples(counted_characters)
    sorted_tuples = sort_character_tuples_by_count(counted_characters_in_tuples)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{counted_words} words found in the document")
    for tuple in sorted_tuples:
        if tuple[0].isalpha(): 
            print(f"the '{tuple[0]}' character was found {tuple[1]} times")
    print("--- End report ---")


def book_text(path):
    with open(path) as f:
        return f.read()

def count_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(book):
    dict = {}
    book_in_lower_case = book.lower()
    for char in book_in_lower_case:
        if char not in dict:
            dict[char] = 1
        elif char in dict:
            dict[char] += 1
    return dict

def convert_dict_counts_to_tuples(dict):
    return list(dict.items())

def sort_character_tuples_by_count(counted_characters_in_tuples):
    counted_characters_in_tuples.sort(key=lambda x: x[1], reverse=True)
    return counted_characters_in_tuples



        

main()