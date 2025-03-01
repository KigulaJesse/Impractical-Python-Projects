"""Find all word pair palingrams in the dictionary"""
import load_dictionary

word_list = load_dictionary.load("2of4brif.txt")

def find_palingrams():
    """Find dictionary palingrams"""
    pali_list = []

    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1: #This is so that we can skip letters
            for i in range(end):
                if word == "banded":
                    print(i)
                if rev_word[end-i:] in word_list and word[i:]==rev_word[:end-i]:
                    if word == "banded":
                        print(word)
                        print(rev_word)
                        print("")
                        print(rev_word[end-i:])
                        print(rev_word[end-i:] in word_list)
                        print("")
                        print(word[i:])
                        print(rev_word[:end-i])
                        print(word[i:]==rev_word[:end-i])
                        print("")
                        pali_list.append((word,rev_word[end-i:]))
                    # break
        #         if word[:i]==rev_word[end-i:] and rev_word[:end-i] in word_list:
        #             pali_list.append((rev_word[:end-i], word))
        if word == "banded":
            break

    return pali_list

palingrams = find_palingrams()
palingrams_sorted = sorted(palingrams)

print(f"\nNumber of palingrams = {len(palingrams_sorted)}")
for first,second in palingrams_sorted:
    print(f"{first} {second}")
