def add_tuple(tuple_a=(), tuple_b=()):
    # If tuple_a or tuple_b is smaller than 2, fill missing values with 0
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    
    # Take only the first 2 integers from each tuple
    a = tuple_a[:2]
    b = tuple_b[:2]
    
    # Add corresponding elements
    result = (a[0] + b[0], a[1] + b[1])
    return result
