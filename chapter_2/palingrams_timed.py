#!/usr/bin/env python
"""Find all world-pair palingrams in a doctionary file."""
import load_dictionary
import time

word_list = load_dictionary.load("2of4brif.txt")
start_time = time.time()

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    for word in word_list:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in word_list:
                    pali_list.append((word, rev_word[end - i :]))
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in word_list:
                    pali_list.append((word, rev_word[end - i :]))
    return pali_list


palingrams = find_palingrams()
# sorting palingrams on first word
palingrams_sorted = sorted(palingrams)

print(f"Number of palingrams = {len(palingrams_sorted)}")
for first, second in palingrams_sorted:
    print(f"{first, second}")

end_time = time.time()
print(f"Runtime for this program was {end_time - start_time} seconds.")