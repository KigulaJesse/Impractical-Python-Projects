"""File to process Palindromes"""
import load_dictionary

list_of_words = load_dictionary.load('2of4brif.txt')
palindromes = [word for word in list_of_words if len(word) > 1 and word[::-1] == word]
print(f"Number of palindromes found: {len(palindromes)}")

palindromes = []
for word in list_of_words:
    if len(word) > 1 and word[::-1] == word:
        palindromes.append(word)

print(f"Number of palindromes found: {len(palindromes)}")
print(*palindromes, sep="\n")
