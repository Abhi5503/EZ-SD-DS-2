def generate_magic_square():
    n = 3
    magic_square = [[0] * n for _ in range(n)]
    
    i, j = 0, n // 2

    # Fill the magic square with numbers from 1 to n*n
    num = 1
    while num <= n * n:
        magic_square[i][j] = num
        num += 1

        # Calculate the next position
        new_i, new_j = (i - 1) % n, (j + 1) % n

        # If the next position is already filled, move down
        if magic_square[new_i][new_j] != 0:
            i = (i + 1) % n
        else:
            i, j = new_i, new_j

    return magic_square

def print_magic_square(magic_square):
    for row in magic_square:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    magic_square = generate_magic_square()
    print("Magic Square:")
    print_magic_square(magic_square)
