def query(arr, queries):
    n = len(arr)
    ps = [0 for i in range(n)]

    # Calculate the prefix sum array
    for i in range(n):
        if i == 0:
            ps[i] = arr[i]
        else:
            ps[i] = ps[i - 1] + arr[i]

    # Process the queries
    for query in queries:
        i = query[0]
        j = query[1]

        if i == 0:
            print(ps[j], end=" ")
        else:
            print(ps[j] - ps[i - 1], end=" ")

# Example usage:
arr = [1, 2, 3, 4, 5]
queries = [(1, 3), (0, 4), (2, 4)]
query(arr, queries)
