s = input("Enter a string: ")
d = {i:w for i, w in enumerate(set(s.lower().split()), start=1)}
print(d)