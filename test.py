"""This is simply for learning. This file will mostly be empty"""
import load_dictionary

word_list = load_dictionary.load("2of4brif.txt")

word = 'banded'
end = len(word)
rev_word = word[::-1]
pali_list = []

for i in range(end):
    if rev_word[end-i:] in word_list and word[i:] == rev_word[:end-i]:
        pali_list.append((word,rev_word[end-i:]))


word = 'grits'
end = len(word)
rev_word = word[::-1]

for i in range(end):
    if rev_word[:end-i] in word_list and word[:i] == rev_word[end-i:]:
        pali_list.append((rev_word[:end-i],word))

print(pali_list)

# word = "grits"
# end = len(word)
# rev = word[::-1]

# for i in range(end):
#     if rev[end-i:]