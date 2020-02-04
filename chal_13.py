# import re

# digits = '0 1 2 3 4 5 6 7 8 9'
# l_dig = digits.split(' ')

# sentence = input("Enter sentence: ")

# s = re.split(' |!', sentence)

# s = ''.join(s)

# print(s)

# val_dig = 0

# for i in s:
#     if i in l_dig:
#         val_dig += 1

# print(f"DIGITS: {val_dig}\nLETTERS: {len(s)-val_dig}")

# Dict method

sentence = input("Enter sentence: ")

d = {}

for c in sentence:
    if c.isdigit():
        if 'DIGITS' not in d:
            d.setdefault('DIGITS', 1)
        else:
            d['DIGITS'] += 1
    elif c.isalpha():
        if 'LETTERS' not in d:
            d.setdefault('LETTERS', 1)
        else:
            d['LETTERS'] += 1
    else:
        pass

print('DIGITS: {} and LETTERS: {}'.format(d['DIGITS'], d['LETTERS']))
