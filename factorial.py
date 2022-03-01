#!/usr/bin/env python3
# factorial

# version with a named variable
factorial = (lambda x: 1 if x <= 1 else x * factorial(x - 1))


name_doesnt_matter = (lambda x: (lambda f: f(f, x))(
    lambda f, x: 1 if x <= 1 else x * f(f, x-1)))


if __name__ == "__main__":
    print(factorial(5))
    print(name_doesnt_matter(5))

    fact = factorial
    fact2 = name_doesnt_matter
    del factorial
    del name_doesnt_matter
    try:
        print(fact(5))
    except NameError as e:
        print(e)
    print(fact2(5))
