# reverse a string very stupidly

a = ['a','b','c']

b = []

for x in range(len(a)-1, -1, -1):
    b.append(a[x])

print(b)