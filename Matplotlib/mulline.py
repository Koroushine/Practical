import matplotlib.pyplot as mp

# Data for multiple lines
overs = [10, 20, 30, 40, 50]
india_scores = [65, 98, 170, 220, 310]
england_scores = [70, 120, 160, 210, 280]
australia_scores = [50, 90, 140, 200, 290]

# Create Figure and Axes
fig, ax = mp.subplots()

# Plot multiple lines with different colors and markers
ax.plot(overs, india_scores, color="#ff6666", marker="o", linestyle="-", linewidth=2, markersize=6, label="India")
ax.plot(overs, england_scores, color="#66b3ff", marker="s", linestyle="--", linewidth=2, markersize=6, label="England")
ax.plot(overs, australia_scores, color="#99ff99", marker="D", linestyle=":", linewidth=2, markersize=6, label="Australia")

# Set labels and title in white
ax.set_xlabel("Overs", color="white")
ax.set_ylabel("Runs Scored", color="white")
ax.set_title("Over-wise Runs Scored\nIndia vs England vs Australia", color="white")

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
mp.savefig("multiline_chart.png", dpi=300, transparent=True)

# Show the Plot
mp.show()
