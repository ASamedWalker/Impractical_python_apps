"""This program adds 'ay' if the word starts with a consonant and 'way' if it's a vowels."""
import sys

def main():
    """Accept users input to add additional words."""
    activate = True
    while activate:
        word = input("Enter word or ('q' to quit): ")
        if word == "q":
            break

        characters = list(word)
        vowels = "aeiouy"
        article = "way" if word[0].lower() in vowels else 'ay'
        if word[0].lower() in vowels:
            article = "".join(characters) + article
        else:
            article = "".join(characters) + article

        print((f"The word is {article}."), file=sys.stedrr)


if __name__ == "__main__":
    main()
