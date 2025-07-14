import sys
from stats import number_of_words, count_character_occurence, sort_dict


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


def main():
    # print(sys.argv)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        
    frankenstein = get_book_text(sys.argv[1])
    num_words = number_of_words(frankenstein)
    # print(f"{num_words} words found in the document")
    character_counts = count_character_occurence(frankenstein)
    # print(character_counts)
    # print("#"*20)

    sorted_dict = sort_dict(character_counts)
    # print(sorted_dict)
    print(f"""============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}...
----------- Word Count ----------
Found {num_words} total words
--------- Character Count -------""")
    for elem in sorted_dict:
        if elem["char"].isalpha():
            print(f"""{elem["char"]}: {elem["num"]}""")

    print("============= END ===============")

main()
