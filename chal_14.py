sentence = input("Enter sentence: ")

d = {}

for c in sentence:
    if c.isupper():
        if 'UPPERCASE' in d:
            d['UPPERCASE'] += 1
        else:
            d.setdefault('UPPERCASE', 1)
    elif c.islower():
        if 'LOWERCASE' in d:
            d['LOWERCASE'] += 1
        else:
            d.setdefault('LOWERCASE', 1)
    else:
        pass

print("UPPERCASE : {} and LOWERCASE: {}".format(d['UPPERCASE'], d['LOWERCASE']))
