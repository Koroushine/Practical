import matplotlib.pyplot as pl
import numpy as np

def plotting():
    x = np.arange(50)
    y = np.sin(x)
    z = np.cos(x)
    e = np.exp(x)
    p = x**2 + 2*x + 4

    pl.figure(figsize=(10, 8))

    pl.subplot(2, 2, 1)
    pl.plot(x, y, color='c')
    pl.title("Sine")

    pl.subplot(2, 2, 2)
    pl.plot(x, z, color='r')
    pl.title("Cosine")

    pl.subplot(2, 2, 3)
    pl.plot(x, e, color='g')
    pl.title("Exponent")

    pl.subplot(2, 2, 4)
    pl.plot(x, p, color='k')
    pl.title("Polynomial")

    pl.tight_layout()
    pl.show()

if __name__ == "__main__":
    plotting()
