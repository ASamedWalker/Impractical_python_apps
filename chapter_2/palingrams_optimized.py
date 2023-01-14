#!/usr/bin/env python
"""Find all world-pair palingrams in a doctionary file."""
import load_dictionary
import time

word_list = load_dictionary.load("2of4brif.txt")


# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        rev_word = word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[: end - i] and rev_word[end - i :] in words:
                    pali_list.append((word, rev_word[end - i :]))
                if word[:i] == rev_word[end - i :] and rev_word[: end - i] in words:
                    pali_list.append((rev_word[end - i :], word))
    return pali_list


start_time = time.time()
palingrams = find_palingrams()
end_time = time.time()
# sorting palingrams on first word
palingrams_sorted = sorted(palingrams)

print(f"Number of palingrams = {len(palingrams_sorted)}")
for first, second in palingrams_sorted:
    print(f"{first, second}")


print(f"Runtime for this program was {end_time - start_time} seconds.")
