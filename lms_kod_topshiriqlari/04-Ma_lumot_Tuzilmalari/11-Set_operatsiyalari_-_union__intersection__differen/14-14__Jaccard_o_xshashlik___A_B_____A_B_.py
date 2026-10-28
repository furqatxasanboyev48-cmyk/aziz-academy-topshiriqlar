A = set(map(int, input().split()))
B = set(map(int, input().split()))
jaccard = len(A & B) / len(A | B)
print("{:.3f}".format(jaccard))