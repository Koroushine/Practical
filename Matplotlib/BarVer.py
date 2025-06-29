import matplotlib.pyplot as plt

# Data
categories = ["A", "B", "C", "D", "E"]
values = [10, 24, 36, 18, 45]

# Create Figure and Axes
fig, ax = plt.subplots()

# Bar Graph using letter colors
ax.bar(categories, values, color=['r', 'b', 'g', 'c', 'm'])  # r = Red, b = Blue, g = Green, c = Cyan, m = Magenta

# Set labels and title in white
ax.set_xlabel("Categories", color="white")
ax.set_ylabel("Values", color="white")
ax.set_title("Simple Bar Graph with Basic Colors", color="white")

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
plt.savefig("bargraph_basic_colors.png", dpi=300, transparent=True)

# Show the Plot
plt.show()
