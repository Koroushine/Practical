def dou(word):
    l = []
    l.append(word)
    for ch in s:
        l.append(ch*2)
    return l

s = input("Enter a string: ")
print("The string is: ", s)
print("The double string is: ", dou(s))