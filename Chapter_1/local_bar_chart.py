#!/usr/bin/env python
"""Generate program to identity six commonly used letters in the English language."""
import sys
import pprint
from collections import defaultdict


def main():
    """Run this program to return the bar chart of commonly used letters."""
    activate_code = True
    while activate_code:
        sentence = input("Enter a sentence (or 'q' to quit):\n")
        if sentence == "q":
            break

        ALPHABET = "abcdefghijklmnopqrstuvwxyz"

        new_list = defaultdict(list)

        for letters in sentence:
            character = letters.lower()
            if character in ALPHABET:
                new_list[character].append(character)

        pprint.pprint(new_list, width=110)
        print(f"\n{sentence}", file=sys.stderr)


if __name__ == "__main__":
    main()
