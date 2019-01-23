import sys


def height(d, root):
    arr = d[root]
    n = len(arr)
    max_height = 1
    if n == 0:
        pass
    else:
        for i in range(0, n):
            height_child = 1 + height(d, arr[i])
            max_height = max(max_height, height_child)
    return max_height


node = []
n = len(node)
d = dict()

for i in range(0, n):
    d[i] = []

for j in range(0, n):
    val = node[j]
    if val == -1:
        root = j
    else:
        d[val].append(j)

for k in range(0, n):
    print(k, d[k])


k = height(d, root)
print('height is ', k)





'''

for i in range(1,5):
    sys.stdout.write('Minie')
    sys.stderr.write('Kabra')

for i in range(1,5):
    print('Minie')
    print('Kabra')
    
'''

