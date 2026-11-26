import sys
input = sys.stdin.readline
n, q = map(int, input().split())
a = list(map(int, input().split()))

queries = [None] * q

for i in range(q):
    l, r = map(int, input().split())
    queries[i] = (r, l, i)

queries.sort()
bit = [0] * (n + 1)
last = {}
ans = [0] * q

j = 0
distinct = 0

for r, l, idx in queries:

    while j < r:
        x = a[j]
        pos = j + 1

        old = last.get(x, None)

        if old is not None:
            k = old
            while k <= n:
                bit[k] -= 1
                k += k & -k
        else:
            distinct += 1

        k = pos
        while k <= n:
            bit[k] += 1
            k += k & -k

        last[x] = pos
        j += 1

    s = 0
    k = l - 1

    while k:
        s += bit[k]
        k -= k & -k

    ans[idx] = distinct - s

sys.stdout.write('\n'.join(map(str, ans)))


# import sys

# input = sys.stdin.readline

# n, q = map(int, input().split())

# a = list(map(int, input().split()))

# queries = [None] * q

# for i in range(q):
#     l, r = map(int, input().split())
#     queries[i] = (r, l, i)

# queries.sort()

# bit = [0] * (n + 1)


# def update(i, val):
#     while i <= n:
#         bit[i] += val
#         i += i & -i


# def query(i):
#     s = 0
#     while i:
#         s += bit[i]
#         i -= i & -i
#     return s


# last = {}
# ans = [0] * q

# j = 0
# distinct = 0

# for r, l, idx in queries:

#     while j < r:
#         x = a[j]
#         pos = j + 1

#         old = last.get(x)

#         if old is not None:
#             update(old, -1)
#         else:
#             distinct += 1

#         update(pos, 1)

#         last[x] = pos
#         j += 1

#     # distinct in [1, r] - distinct whose latest occurrence < l
#     ans[idx] = distinct - query(l - 1)

# sys.stdout.write('\n'.join(map(str, ans)))