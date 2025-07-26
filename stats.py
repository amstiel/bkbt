def get_book_text(path_to_file):
  with open(path_to_file) as file:
    return file.read()
  
def get_num_words(text):
  words = text.split()
  return len(words)

def get_char_count(text):
  count_by_char = {}

  words = text.split()
  for word in words:
    for char in word:
      lowercased_char = char.lower()
      if lowercased_char in count_by_char:
        count_by_char[lowercased_char] += 1
      else:
        count_by_char[lowercased_char] = 1
    
  return count_by_char

def get_sorted_char_count(char_count):
  char_num_pairs = []
  for char in char_count:
    char_num_pairs.append({ "char": char, "num": char_count[char] })

  char_num_pairs.sort(reverse=True, key=lambda item: item["num"])

  return char_num_pairs
