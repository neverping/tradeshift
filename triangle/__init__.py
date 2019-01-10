def check_triangle_type(a,b,c):

    if not all(isinstance(v, int) for v in [a,b,c]):
        raise ValueError('All values must be integer type!')

    if not all(v > 0 for v in [a,b,c]):
        raise ValueError('You must pass values greater than 0!')

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        raise ValueError('One the sides are too small to form a triangle! The value was {}.'.format(min(a,b,c)))

    triangle = set()
    triangle = {a,b,c}

    if len(triangle) == 1:
        return 'This triangle is an equilateral type.'
    elif len(triangle) == 2:
        return 'This triangle is an isosceles type.'
    else:
        return 'This triangle is a scalene type.'