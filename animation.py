import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Animation:
    def __init__(self, positions, masses):
        self.positions = positions
        self.masses = masses

    def animate_simulation(self):
        fig, ax = plt.subplots()
        ax.set_xlim([-100, 100])
        ax.set_ylim([-100, 100])

        scat = ax.scatter(0, 0)

        def animate(i):
            scat.set_offsets(self.positions[i])
            scat.set_sizes(self.masses[i])
            return scat,

        ani = animation.FuncAnimation(fig,
                                      animate,
                                      repeat=False,
                                      frames=len(self.positions) - 1,
                                      interval=1)

        # To save the animation using Pillow as a gif
        # writer = animation.PillowWriter(fps=15,
        #                                 metadata=dict(artist='Me'),
        #                                 bitrate=1800)
        # ani.save('scatter.gif', writer=writer)

        plt.show()
