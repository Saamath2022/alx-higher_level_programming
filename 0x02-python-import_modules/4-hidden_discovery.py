#!/usr/bin/pythong3
import marshal

def print_names();

    with open('hidden_4.pyc', 'rb') as file:
        code = marshal.load(file)

        names = [name for name in code.co_names if not name.startswith('__')]

        sorted_names = sorted(names)

        for name in sorted_names:
        print(name)

if __name__ == "__main__":
    print_names()

