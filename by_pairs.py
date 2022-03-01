#!/usr/bin/env python3
# iterate over pairs of ajacent elements

# version without zip. Do not use, this is stupid
by_pairs = (lambda it: (lambda f: f(f, *it))(lambda f, *it: []
            if len(it) < 2 else [(it[0], it[1]), *f(f, *it[1:])]))

by_pairs = (lambda it: zip(it, it[1:]))

if __name__ == "__main__":
    print(list(by_pairs([])))
    print(list(by_pairs([1, 2, 3, 4, 5, 6, 7, 8, 9])))
