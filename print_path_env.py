import os
import sys


def print_directories_in_path():
    paths = os.environ["PATH"].split(";")
    print(*paths, sep="\n")


def print_directories_and_exes_in_path():
    paths = os.environ["PATH"].split(";")
    for path in paths:
        print(path)
        try:
            for file in os.listdir(path):
                if file.endswith(".exe"):
                    print(file, sep=", ")
            print("\n")
        except FileNotFoundError:
            print(f"Error: Could not access directory {path}")


if __name__ == "__main__":
    if sys.argv[1] == "1":
        print_directories_in_path()
    elif sys.argv[1] == "2":
        print_directories_and_exes_in_path()
    else:
        print("Wrong argument")
