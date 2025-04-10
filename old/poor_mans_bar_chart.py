"""Poor Man's bar Chart Practise Question"""
from collections import defaultdict
import pprint

MNEMONIC = 'etaoin'
mnemonic_dict = defaultdict(list)
while True:
    sentence = input("Please input the sentence for the Poor Man's Barchart: ")
    for i in range(65,91):
        mnemonic_dict[chr(i)] = []
    for i in range(97,123):
        mnemonic_dict[chr(i)] = []
    for i in sentence:
        mnemonic_dict[i].append(i)
    pprint.pp(mnemonic_dict)
    try_again = input("Try Again? (Press enter else n to quit)")
    if try_again == "n":
        break
    