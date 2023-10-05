def is_magic_square(matrix):
    # Calculate the sum of the first row (horizontal sum)
    target_sum = sum(matrix[0])
    
    # Check horizontal and vertical sums
    for i in range(3):
        if sum(matrix[i]) != target_sum:
            return False
        if sum(matrix[j][i] for j in range(3)) != target_sum:
            return False
    
    # Check diagonal sums
    if sum(matrix[i][i] for i in range(3)) != target_sum:
        return False
    if sum(matrix[i][2 - i] for i in range(3)) != target_sum:
        return False
    
    return True

def generate_magic_square():
    for a in range(1, 10):
        for b in range(1, 10):
            if b != a:
                for c in range(1, 10):
                    if c != a and c != b:
                        for d in range(1, 10):
                            if d != a and d != b and d != c:
                                for e in range(1, 10):
                                    if e != a and e != b and e != c and e != d:
                                        for f in range(1, 10):
                                            if f != a and f != b and f != c and f != d and f != e:
                                                for g in range(1, 10):
                                                    if g != a and g != b and g != c and g != d and g != e and g != f:
                                                        for h in range(1, 10):
                                                            if h != a and h != b and h != c and h != d and h != e and h != f and h != g:
                                                                i = 45 - a - b - c - d - e - f - g - h
                                                                matrix = [[a, b, c], [d, e, f], [g, h, i]]
                                                                if is_magic_square(matrix):
                                                                    return matrix

magic_square = generate_magic_square()

# Print the magic square
for row in magic_square:
    print(row)
