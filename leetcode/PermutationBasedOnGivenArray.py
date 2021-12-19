def permute(A, P, n):

    op = 0
    # For each element of P
    for i in range(n):
        next = i

        # Check if it is already
        # considered in cycle
        while (P[next] >= 0):

            op += 1
            # Swap the current element according
            # to the permutation in P
            t = A[i]
            A[i] = A[P[next]]
            A[P[next]] = t

            temp = P[next]

            # Subtract n from an entry in P
            # to make it negative which indicates
            # the corresponding move
            # has been performed
            P[next] -= n
            next = temp

    return op+1


# Driver code
if __name__ == '__main__':
    A = [5, 1, 8, 3, 7, 4, 2, 6]
    P = [0, 1, 2, 3, 4, 5, 6, 7]
    n = len(A)

    print(permute(A, P, n))

    # Print the new array after
    # applying the permutation
    # for i in range(n):
    #     print(A[i], end=" ")
