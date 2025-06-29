import matplotlib.pyplot as plt

# Data
categories = ["A", "B", "C", "D", "E"]
values = [10, 24, 36, 18, 45]

# Create Figure and Axes
fig, ax = plt.subplots()

# Create Horizontal Bar Graph
ax.barh(categories, values, color=['r', 'b', 'g', 'c', 'm'])  # r = Red, b = Blue, g = Green, c = Cyan, m = Magenta

# Set labels and title in white
ax.set_xlabel("Values", color="white")  # X-axis is now the value
ax.set_ylabel("Categories", color="white")
ax.set_title("Simple Horizontal Bar Graph", color="white")

# Change tick colors to white
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")

# Change axis spine colors to white
ax.spines["bottom"].set_color("white")
ax.spines["top"].set_color("white")
ax.spines["right"].set_color("white")
ax.spines["left"].set_color("white")

# Remove background
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Save as Transparent PNG
plt.savefig("horizontal_bargraph.png", dpi=300, transparent=True)

# Show the Plot
plt.show()
