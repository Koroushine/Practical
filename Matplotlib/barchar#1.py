try:
    import matplotlib.pyplot as plt
    import numpy as np

    a = [34, 54, 23, 54, 65]
    b = [30, 50, 20, 50, 60]
    c = [40, 60, 30, 60, 70]

    x = np.arange(len(a))  # Numeric positions for each bar group
    labels = ["Satees", "Korou", "Thaimei", "Halondo", "Borish"]

    width = 0.25  # Width of each bar

    plt.bar(x - width, a, width=width, color='magenta', label='Python')
    plt.bar(x, b, width=width, color='black', label='Architecture')
    plt.bar(x + width, c, width=width, color='cyan', label='C++')

    plt.xticks(x, labels)
    plt.legend()
    plt.show()

except:
    print("Chumna eirek ou")
