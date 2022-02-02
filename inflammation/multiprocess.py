from multiprocessing import Pool

def sum_of_squares(sequence):
    """Test sum of squares for either strings or lists being passed into the function"""
    from functools import reduce

    integers = [int(a) for a in sequence]
    squares = [i * i for i in integers]

    return reduce(lambda b, c: b + c, squares)


def product(a):
    """Return the product of two numbers"""
    return a*a


with Pool(2) as p:
    print(p.map(product, [1,2,3]))
