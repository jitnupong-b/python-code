myset = set(['1', 2, 'test', 0.21])
myset_2 = set((1, 2, 3))
myset_3 = set('abcdefg')
myset_4 = set(['dog', 'cat', 'mouse'])
#print(type(myset))
#print(type(myset_2))
#print(myset_3)
#print(myset_4)
myset_4.add('bird')
myset_4.update(['fish', 'zebra'])
myset_5 = set(['ant', 'deer', 'fish'])
#print(myset_4)

union_set = myset_4.union(myset_3)
print(union_set)

#intersect_set = myset_4 & myset_5
intersect_set = myset_4.intersection(myset_5)
print(intersect_set)

#diff_set = myset_4 - myset_5
diff_set = myset_4.difference(myset_5)
print(diff_set)

symmatric_diff_set = myset_4.symmetric_difference(myset_5)
print(symmatric_diff_set)

print(myset_5.issubset(myset_4))
print(myset_4.issuperset(myset_5))