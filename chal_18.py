import re

p = input("Enter comma-separated passwords: ")
p = p.split(',')
good_p = []

for i in p:
    if len(i) < 6 or len(i) > 12:
        continue
    else:
        pass
    if re.search(r'[a-z]', i):
        pass
    else:
        continue
    if re.search(r'[0-9]', i):
        pass
    else:
        continue
    if re.search(r'[A-Z]', i):
        pass
    else:
        continue
    if re.search(r'[$#@]', i):
        pass
    else:
        continue
    good_p.append(i)

print(good_p)
