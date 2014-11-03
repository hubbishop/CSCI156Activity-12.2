__author__ = 'Dark-Knight'


L = [[1, 2], [1, -1], [5, 8], [-4, -2], [4, 3], [4, 2]]
M = []
for x in L:
    max(x)
    M.append((max(x), x))

print(M)
M.sort(reverse=True)
print(M)
