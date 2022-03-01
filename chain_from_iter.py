#!/usr/bin/env python3
# similar to itertools.chain.from_iterator

chain_from_iter = (lambda *it: (lambda chain: chain(chain, *chain(chain, *it)))
                   (lambda chain, *it: [] if len(it) == 0 else [*it[0], *chain(chain, *it[1:])]))

if __name__ == "__main__":
    print(chain_from_iter([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
          [[10, 11], [12, 13], [14, 15]]))

    # due to the use of recursion, if the number of arguments is too big,
    # if will raise a RecursionError exception
    try:
        print(chain_from_iter(*[[[0]]]*1000))
    except RecursionError as e:
        print(e)
