s = {1,2,2,3,4,4,4,5}
empty_set = set()

#methods
s.add(6)
s.remove(2)
s.pop()
s.clear()
print(s)
print(len(s))

s1 = {1,2,2,4,5,6,6}
s2 = {2,4,4}

print(s1.intersection(s2))
print(s1.union(s2))