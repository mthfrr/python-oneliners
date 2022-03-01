# python-oneliners

Because sometimes you feel using more than one line is a waste of space

Tested with Python 3.10

## Basics

These oneliners use lambda functions in Python.

```py
my_func = lambda param1, param2: print(param1, param2)
```

The probleme is that only one statement can be executed in a `lamdba` and its
result will be returned. Since Python 3.8 you cannot use `yield` in `lambdas`

That's why to accomplish complexe task, a few tricks are used.

```py
# ternary operator
(val1 if cond else val2) # note: the else part is requiered

# the [do(x) for x in mylist] or the map function
[x**2 for x in [1, 2, 3]] # [1, 4, 9]

# the filter function
filter(lambda x: x%2==0, [0, 1, 2, 4, 5]) # [0, 2, 4]

# the unpacking operator *
def sum(a, b):
    return a + b
sum(*[5, 6]) # sum(5, 6)
```

Be careful, all of these functions do not actualy return a list.
They create generators.

## Recursion

An other key technique is recursion.

An easy way is to store the function in a variable and then call it.
This works because the function is stored in the global scope and is then
reachable when the lambda is called.

```py
factorial = (lambda x: 1 if x <= 1 else x * factorial(x - 1))

# if factorial is no longer in scope, the function breaks
fact = factorial
del factorial
fact(5) # NameError: name 'factorial' is not defined
```

However, this is not perfect as it is impossible to embed it in a bigger
oneliner.

The better solution is to use 3 lambdas`:

```py
factorial = (lambda x: (lambda f: f(f, x))(lambda f, x: 1 if x <= 1 else x * f(f, x-1)))

fact = factorial
del factorial
fact(5) # 120
```

There is a main, wrapper lambda which executes an other lambda which takes the
recusive function as a parameter and can then call it with itself as a parameter
