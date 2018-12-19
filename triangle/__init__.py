def check_triangle_type(a,b,c):
    triangle = set()
    triangle = {a,b,c}

    if len(triangle) == 1:
        return 'equilateral'
    elif len(triangle) == 2:
        return 'isosceles'
    else:
        return 'scalene'

print(check_triangle_type(1,2,3))