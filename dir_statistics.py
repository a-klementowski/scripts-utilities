import json
import os
import subprocess
import sys


def process_file(filepath):
    result = subprocess.run(["python", "file_stats.py", filepath], capture_output=True, text=True)
    return json.loads(result.stdout)


def files_processing():
    if len(sys.argv) != 2:
        print("Wrong arguments")
        sys.exit(1)

    directory_path = sys.argv[1]
    list_of_stats = []

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(directory_path, filename)
            stats = process_file(filepath)
            list_of_stats.append(stats)

    character_count = sum([stat["character_count"] for stat in list_of_stats])
    word_count = sum([stat["word_count"] for stat in list_of_stats])
    line_count = sum([stat["line_count"] for stat in list_of_stats])
    most_frequent_character = max(list_of_stats, key=lambda x: x["most_frequent_character"]["count"])[
        "most_frequent_character"]
    most_frequent_word = max(list_of_stats, key=lambda x: x["most_frequent_word"]["count"])["most_frequent_word"]

    result = {
        "number_of_files": len(list_of_stats),
        "character_count": character_count,
        "word_count": word_count,
        "line_count": line_count,
        "most_frequent_character": most_frequent_character,
        "most_frequent_word": most_frequent_word
    }

    print(json.dumps(result))


if __name__ == "__main__":
    files_processing()
