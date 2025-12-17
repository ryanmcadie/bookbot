import sys
from stats import get_num_words, get_char_counts, sort_char_counts

def get_book_text(filepath):
	with open(filepath, "r", encoding="utf-8") as file:
		return file.read()


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
		
	path = sys.argv[1]

	book_text = get_book_text(path)
	num_words = get_num_words(book_text)
	char_counts = get_char_counts(book_text)
	sorted_chars = sort_char_counts(char_counts)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path}...")
	print("----------- Word Count ----------")
	print(f"Found {num_words} total words")
	print("--------- Character Count -------")
			
	for item in sorted_chars:
			if item["char"].isalpha():
				print(f"{item['char']}: {item['num']}")
			
	print("============= END ===============")
    
main()
