import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


GRID_SIZE = (100, 100)


def random_grid(grid_size):
    return np.random.choice([0, 1], size=grid_size, p=[0.8, 0.2])


def update(frameNum, img, grid, N):
    
    newGrid = grid.copy()

    
    for i in range(N[0]):
        for j in range(N[1]):
            
            live_neighbors = (
                grid[(i - 1) % N[0], (j - 1) % N[1]] +
                grid[(i - 1) % N[0], j % N[1]] +
                grid[(i - 1) % N[0], (j + 1) % N[1]] +
                grid[i % N[0], (j - 1) % N[1]] +
                grid[i % N[0], (j + 1) % N[1]] +
                grid[(i + 1) % N[0], (j - 1) % N[1]] +
                grid[(i + 1) % N[0], j % N[1]] +
                grid[(i + 1) % N[0], (j + 1) % N[1]]
            )

            
            if grid[i, j] == 1 and live_neighbors < 2:
                newGrid[i, j] = 0
            
            elif grid[i, j] == 1 and (live_neighbors == 2 or live_neighbors == 3):
                newGrid[i, j] = 1
            
            elif grid[i, j] == 1 and live_neighbors > 3:
                newGrid[i, j] = 0
            
            elif grid[i, j] == 0 and live_neighbors == 3:
                newGrid[i, j] = 1

    
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    return img,


def main():
    
    fig, ax = plt.subplots()

    
    grid = random_grid(GRID_SIZE)

    
    img = ax.imshow(grid, interpolation='nearest', cmap='binary')

    
    ani = animation.FuncAnimation(fig, update, fargs=(img, grid, GRID_SIZE),
                                   frames=100,  
                                   interval=100, 
                                   save_count=50) 

    # To display the animation in a Jupyter Notebook/Colab environment:
    from IPython.display import HTML
    return HTML(ani.to_jshtml())


main()
