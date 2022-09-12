a ='Excalibur'
print(a)

b = "Smallfoot"
print(b)

c = '''Once upon
a time, there was a person
that used to sleep.
The end'''
print(c)

print(a[0]) # first char
print(a[2]) # third char
print(a[-1]) # last char
print(a[-3]) # third last char

print(a[0], a[2], a[3])

name = 'Vijay Deenanath Chauhan'
for i,c in enumerate(name):
    print(i, c)
mname = name[6 : -8]
fname = name[:5]
lname = name[-7:]
print(mname)
print(fname)
print(lname)

# reverse the string
print( name[::-1] )

print( name[:5][::-1] )

# every even idx char
print(name[::2]) # vjy

# every odd idx char
print(name[1::2])

# for i in range(15000,20000):
#     print(i, chr(i))

print('‱'*80)