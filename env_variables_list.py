import os
import sys


def print_environment_variables():
    list_of_variables = sorted(list(os.environ))
    if len(sys.argv) == 1:
        for variable in list_of_variables:
            print(f"{variable}: {os.environ[variable]}")
    else:
        for variable in list_of_variables:
            if any(arg in variable for arg in sys.argv[1:]):
                print(f"{variable}: {os.environ[variable]}")


if __name__ == "__main__":
    print_environment_variables()
