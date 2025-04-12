"""Remove single letter words"""
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')
end = len(word_list)




for i in range(end):
    if 0 <= i < len(word_list):
        if len(word_list[i]) == 1:
            word_list.pop(i)
