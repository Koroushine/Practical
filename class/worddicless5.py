s = input("Enter your string: ")
d = {i: w for i, w in enumerate(set(s.lower().split()), start=1)} if len(s) <= 5 else {}
print(d)
# not working