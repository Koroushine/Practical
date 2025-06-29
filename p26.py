import matplotlib.pyplot as pl
import numpy as np

n = int(input("Enter number of persons: "))
h = []
p = []

for i in range(n):
    print(f"\nFor person {i+1}:")
    hi = float(input("Enter height: "))
    pu = int(input("Enter pulse: "))

    if pu < 60 or pu > 100:
        print("Invalid pulse rate!")
        continue

    h.append(hi)
    p.append(pu)

h = np.array(h)
p = np.array(p)

pl.scatter(h, p, marker="D", color='r', s=100)
pl.xlabel('height')
pl.ylabel('pulse')
pl.show()
