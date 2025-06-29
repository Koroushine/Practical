import numpy as np
import matplotlib.pyplot as plt

# Data
categories = ["A", "B", "C", "D", "E"]
values_1 = [10, 24, 36, 18, 45]  # Group 1
values_2 = [15, 30, 25, 22, 40]  # Group 2
values_3 = [12, 28, 33, 20, 38]  # Group 3

# Number of categories
x = np.arange(len(categories))

# Width of bars
width = 0.25  

# Create Figure and Axes
fig, ax = plt.subplots()

# Plot Multiple Bars (Side by Side)
ax.bar(x - width, values_1, width, color='r', label="Group 1")  # Red Bars
ax.bar(x, values_2, width, color='b', label="Group 2")          # Blue Bars
ax.bar(x + width, values_3, width, color='g', label="Group 3")  # Green Bars

# Set category labels at correct positions
ax.set_xticks(x)
ax.set_xticklabels(categories, color="white")

# Set labels and title in white
ax.set_xlabel("Categories", color="white")
ax.set_ylabel("Values", color="white")
ax.set_title("Multiple Bar Graph", color="white")

# Change tick colors to white
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")

# Change axis spine colors to white
ax.spines["bottom"].set_color("white")
ax.spines["top"].set_color("white")
ax.spines["right"].set_color("white")
ax.spines["left"].set_color("white")

# Add a legend with white text
legend = ax.legend()
for text in legend.get_texts():
    text.set_color("white")

# Remove background
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Save as Transparent PNG
plt.savefig("multiple_bargraph.png", dpi=300, transparent=True)

# Show the Plot
plt.show()
