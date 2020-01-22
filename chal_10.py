w = input("Enter whitespace separated words: ")

l_w = w.split(' ')
print(l_w)
s_w = set(l_w)
s = list(s_w)
print(sorted(s))
s.sort()
print(s)
