#!/usr/bin/env python3
# similar to itertools.chain

chain = (lambda *it: (lambda f: f(f, *it))(lambda f, *it: []
         if len(it) == 0 else [*it[0], *f(f, *it[1:])]))

if __name__ == "__main__":
    print(chain([1, 2, 3], [4, 5, 6], [7, 8, 9]))

    # due to the use of recursion, if the number of arguments is too big,
    # if will raise a RecursionError exception
    try:
        print(chain(*[[0]]*1000))
    except RecursionError as e:
        print(e)
