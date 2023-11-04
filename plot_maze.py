import  matplotlib.pyplot as plt
def plot_maze(maze):
    ax=plt.gca()
    ax.invert_yaxis()
    ax.axis('off')
    ax.set_aspect('equal')
    plt.pcolormesh(maze,edgecolors='black',linewidth=2,cmap='Accent')
    plt.show()
