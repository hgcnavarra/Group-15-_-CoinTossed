import matplotlib.pyplot as plt
import matplotlib.animation as animation

# ------------------------
# CUMULATIVE DATA (FROM YOUR TABLE)
# ------------------------

heads = [
0,0,1,2,3,3,3,3,4,5,6,7,8,9,9,9,9,10,11,12,
13,14,14,14,14,14,15,15,15,16,16,17,18,19,19,19,19,20,20,21,
21,21,22,23,23,24,24,24,24,24,25,25,26,27,28,28,29,30,30,30,
30,30,31,32,32,32,33,33,34,34,35,36,36,36,36,37,38,39,40,40,
40,41,41,42,42,43,44,44,45,45,45,46,47,47,47,47,47,48,48,49,
49,49,50,51,51,51,52,52,53,54,55,55,56,56,56,57,58,59,59,60,
61,62,63,63,63,63,63,63,63,64,65,65,66,67,68,69,70,71,71,72,
73,74,75,76,77,77,77,78,79,80,80,80,80,81,81,81,82,83,83,84,
84,84,84,84,84,85,85,85,85,85,85,86,86,87,88,89,90,90,91,92,
93,94,94,95,95,95,96,96,97,97,98,98,98,98,98,98,98,99,99,100
]

tails = [
1,2,2,2,2,3,4,5,5,5,5,5,5,5,6,7,8,8,8,8,
8,8,9,10,11,12,12,13,14,14,15,15,15,15,16,17,18,18,19,19,
20,21,21,21,22,22,23,24,25,26,26,27,27,27,27,28,28,28,29,30,
31,32,32,32,33,34,34,35,35,36,36,36,37,38,39,39,39,39,39,40,
41,41,42,42,43,43,43,44,44,45,46,46,46,47,48,49,50,50,51,51,
52,53,53,53,54,55,55,56,56,56,56,57,57,58,59,59,59,59,60,60,
60,60,60,61,62,63,64,65,66,66,66,67,67,67,67,67,67,67,68,68,
68,68,68,68,68,69,70,70,70,70,71,72,73,73,74,75,75,75,76,76,
77,78,79,80,81,81,82,83,84,85,86,86,87,87,87,87,87,88,88,88,
88,88,89,89,90,91,91,92,92,93,93,94,95,96,97,98,99,99,100,100
]

# ------------------------
# STYLE
# ------------------------

plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(10,6))
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

ax.set_xlim(0, 200)
ax.set_ylim(0, 110)

ax.set_title("1A & 5B Combined (200 Flips)", color='white')
ax.set_xlabel("Number of Flips", color='white')
ax.set_ylabel("Cumulative Count", color='white')
ax.tick_params(colors='white')

lineH, = ax.plot([], [], color='cyan', linewidth=2.5, label="Heads")
lineT, = ax.plot([], [], color='magenta', linewidth=2.5, label="Tails")

ax.legend(facecolor='black')

# ------------------------
# ANIMATION
# ------------------------

def update(frame):
    lineH.set_data(range(frame), heads[:frame])
    lineT.set_data(range(frame), tails[:frame])
    return lineH, lineT

ani = animation.FuncAnimation(
    fig,
    update,
    frames=len(heads) + 1,
    interval=40,     # slightly faster for 200 frames
    repeat=False
)

plt.tight_layout()
plt.show()
