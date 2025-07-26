import sys
from stats import get_num_words, get_sorted_char_count, get_book_text, get_char_count

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  


  path_to_file = sys.argv[1]
  book_text = get_book_text(path_to_file)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path_to_file}...")
  print("----------- Word Count ----------")
  print(f"Found {get_num_words(book_text)} total words")
  print("--------- Character Count -------")
  for entry in get_sorted_char_count(get_char_count(book_text)):
    if entry["char"].isalpha():
      print(f"{entry["char"]}: {entry["num"]}")
  
main()
