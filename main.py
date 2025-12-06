import sys
from stats import get_word_count, get_unique_string_count, get_dict_list, print_dict

def get_book_text(filepath):
    print(f"Analyzing book found at {filepath}...")
    
    with open(filepath) as f:
        filecontent = f.read()

    return filecontent

def main():
    # check command line input
    if len(sys.argv) < 2:
        print ("Usage: python3 main.py <path_to_book>")
        sys.exit(1) # exit code if arguments less than 2
    
    filepath = sys.argv[1]

    print("============ BOOKBOT ============")
    book_content = get_book_text(filepath)

    print("----------- Word Count ----------")
    word_count = get_word_count(book_content)
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    string_count = get_unique_string_count(book_content)
    dict_list = get_dict_list(string_count)
    print_dict(dict_list)

    print("============= END ===============")

main()