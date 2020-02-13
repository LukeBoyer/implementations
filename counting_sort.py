#counting sort

def sort(A):
    # init c (and b?)
    c = [0] * (mx(A) + 1)
    b = [0] * len(A)

    # count values from c into a such that c[i] = number of elements in a with value i
    for i in A:
        c[i] = c[i] + 1
    # edit c such that c[i] is all the numbers in a less than or equal to i
    for j in range(1, len(c)):
        c[j] = c[j] + c[j - 1]
    print(c)
    # place x in the correct position such that b[i] where i is given by the amount of numbers in a less than or equal to x 
    for k in range(len(A)):
        b[c[A[k]]- 1] = A[k]
        c[A[k]] = c[A[k]] - 1
    return b
# subroutine to calculate highest value (accounts for only positive values)

def mx(A):
    i = 0
    for j in A:
        i = max(j, i)
    return i

# tests

l = [1, 4, 2, 3, 6]
mt = []
l2 = [3, 7, 6, 1]

print(sort(l))
print(sort(mt))
print(sort(l2))

