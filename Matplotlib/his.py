import matplotlib.pyplot as plt

data = [12, 19, 29, 24, 27, 45, 32, 33, 25, 30, 31, 19, 23, 41, 18, 28, 22]

fig, ax = plt.subplots()

ax.hist(data, bins=6, color="cyan", edgecolor="white")

# Set labels and title in white
ax.set_xlabel("Value Ranges", color="white")
ax.set_ylabel("Frequency", color="white")
ax.set_title("Simple Histogram", color="white")

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
plt.savefig("histogram.png", dpi=300, transparent=True)

# Show the Plot
plt.show()
