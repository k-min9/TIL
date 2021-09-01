words = input().rstrip()
change = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']

for c in change:
    words = words.replace(c, '#')
print(words)
print(len(words))