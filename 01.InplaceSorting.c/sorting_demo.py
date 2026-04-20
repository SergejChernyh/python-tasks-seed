#!/usr/bin/env -S python3
"""
Sorts array of integers from sys.argv and prints them into stdout
"""

import sys
import sortings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Provide at least one number!", file=sys.stderr)
        sys.exit(1)

    input_data = list(map(int, sys.argv[1:]))

    for name, sort_alg in sortings.sorting_algs:
        data = input_data[:]
        try:
            sort_alg(data)
        except IndexError:
            print(f"{name} ERROR")
            continue
        print(f"{name} {' '.join(map(str, data))}")
