print('\\n')
print(r'\n')

# multiline string input
data = ''
while True:
    line = input()
    if not line:
        break
    data += line + '\n'
print('----->OUTPUT<------')
print(len(data), 'chars')