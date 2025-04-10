"""Find all word pair palingrams in the dictionary"""
import load_dictionary
import time

word_list = load_dictionary.load("2of4brif.txt")

def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []
    for word in word_list:
        print(word)
        end = len(word)
        rev_word = word[::-1]
        if end > 1: #This is so that we can skip letters
            for i in range(end):
                if rev_word[end-i:] in word_list and rev_word[:end-i] == word[i:]:
                    pali_list.append((word, rev_word[end-i:]))
                if rev_word[:end-i] in word_list and rev_word[end-i:] == word[:i]:
                    pali_list.append((rev_word[:end-i], word))
        else:
            print(word)
    return pali_list

start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
print(f"Runtime for this program {end_time-start_time}")
palingrams_sorted = sorted(palingrams)

# print(f"\nNumber of palingrams = {len(palingrams_sorted)}")
# for first,second in palingrams_sorted:
#     print(f"{first} {second}")
