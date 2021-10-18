from collections import Counter
a=[1,2,3,4,5,6,7,7,7,4,3,2,1,1,1]
c=Counter(a)
print(c)
print(list(c.elements()))
print(c.most_common())
sub={2:1,7:1}
print(c.subtract(sub))
print(c.most_common())