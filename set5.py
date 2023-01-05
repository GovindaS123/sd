s={'b', 'a', 'r'} & set('qux')
print(s)
w={1, 2, 3, 4, 5} - {3, 4} ^ {5, 6, 7}
print(w)
#d=(x & y <= x) and (x & y <= y)
#print(d)
'''x = {1, 2, 3}
y = {1, 2}
y.ispropersubset(x)'''
s = {'foo', 'bar', 'baz', 'qux'}
s -= {'bar'}
print(s)