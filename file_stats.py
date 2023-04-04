import json
import sys
from collections import Counter


def count_characters(file):
    data = file.read()
    number_of_characters = len(data.replace('\n', ''))
    # number_of_characters = len(data)
    return number_of_characters


def count_words(file):
    number_of_words = 0
    for line in file:
        number_of_words += len(line.split())
    return number_of_words


def count_lines(file):
    lines = file.readlines()
    return len(lines)


def most_frequent_character(file):
    counts = Counter(file.read())
    character, count = counts.most_common(1)[0]
    return character, count


def most_frequent_word(file):
    data = file.read().replace('\n', ' ')
    words = data.split()
    word_counts = Counter(words)
    word, count = word_counts.most_common(1)[0]
    return word, count


if __name__ == "__main__":
    filepath = sys.argv[1]
    with open(filepath) as file:
        character_count = count_characters(file)
        file.seek(0)
        word_count = count_words(file)
        file.seek(0)
        line_count = count_lines(file)
        file.seek(0)
        most_frequent_character_result = most_frequent_character(file)
        file.seek(0)
        most_frequent_word_result = most_frequent_word(file)
        file.seek(0)

        result = {
            "file_path": filepath,
            "character_count": character_count,
            "word_count": word_count,
            "line_count": line_count,
            "most_frequent_character": {
                "character": most_frequent_character_result[0],
                "count": most_frequent_character_result[1]
            },
            "most_frequent_word": {
                "word": most_frequent_word_result[0],
                "count": most_frequent_word_result[1]
            }
        }
        print(json.dumps(result))
