from collections import defaultdict

a = defaultdict(list)

# a[3] = 1
# a[4] = 2
# a[1] = 3
a['c'] = 4
a['a'] = 5
a['b'] = 6
a['d'].append('e')
a['d'].append('f')



print(a)

print(a[4])