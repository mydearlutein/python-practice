import argparse
from collections import Counter


def most_common_word(self, paragraph: str, banned: List[str]) -> str:

    # Make lowercase
    paragraph = paragraph.lower()

    # Make word list
    word = ""
    words = []
    for char in list(paragraph):
        if char.isalpha():
            word += char
        else:
            if word != "":
                words.append(word)
                word = ""

    if word != "":
        words.append(word)

    # Remove banned words
    allowed_words = []
    for word in words:
        if word not in banned:
            allowed_words.append(word)

    words_counter = Counter(allowed_words)
    most_common_word = max(words_counter, key=words_counter.get, default="")

    return most_common_word


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find most common word in paragraph")
    parser.add_argument("paragraph", required=True, tyep=str, help="Input paragraph")
    parser.add_argument("banned", required=True, tyep=List[str], help="list of banned words")

    args = parser.parse_args()
    print("Most common word is", most_common_word(args.paragraph, args.banned))
