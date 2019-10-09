A = {0, 2, 5, 10, 11, 12, 15, 16, 19, 23, 24, 30}
B = {1, 3, 4, 6, 7, 15, 16, 22, 23, 25, 29}
U = set(list(range(0,31)))
C = U.difference(A)
D = C.intersection(B)

def cardinality(A,B,U):
    return 2**len(D)

# print(len(A))
# print(len(B))
# print(len(U))
# print(len(C))
# print(len(D))
# print(C)
# print(D)
#print(U.difference(A).union(B))

print(cardinality(A, B, U))
