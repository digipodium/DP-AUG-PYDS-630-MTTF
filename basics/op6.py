x = 10
y = 10
z = x
c = 5
d = 10

print(x is y)   # True
print(x is c)   # False
print(x is z)   # True
print(y is z)   # True
print(y is x)   # True
print(c is x)   # False
print(c is c)   # True
print(c is d)   # False
print(x is d)   # True

x = [1,2,3]
y = [1,2,3]
z = x

print(x is y) # False
print(x is z) # True
print(z is y) # False