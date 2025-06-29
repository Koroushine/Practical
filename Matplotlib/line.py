import matplotlib.pyplot as mp

# Data
x = [10, 20, 30, 40, 50]
y = [65, 98, 170, 220, 310]

# Create Plot
fig, ax = mp.subplots()

# Plot the line with markers
ax.plot(x, y, color="white", marker="o", linestyle="-", linewidth=2, markersize=6)  

# Set labels and title to white
ax.set_xlabel("Overs", color="white")
ax.set_ylabel("Runs Scored", color="white")
ax.set_title("Over-wise Runs Scored\nIndia vs England", color="white")

# Change tick colors
ax.tick_params(axis="x", colors="white")
ax.tick_params(axis="y", colors="white")

# Change axis spine colors
ax.spines["bottom"].set_color("white")
ax.spines["top"].set_color("white")
ax.spines["right"].set_color("white")
ax.spines["left"].set_color("white")

# Remove background
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Save as transparent PNG
mp.savefig("line_2.png", dpi=300, transparent=True)

# Show Plot
mp.show()
