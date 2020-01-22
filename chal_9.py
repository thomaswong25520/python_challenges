s = ""

while True:
    a = input("Enter sentence: ")
    if a == "":
        break
    else:
        s += a
        s += "\n"

print(s.upper())
