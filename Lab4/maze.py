# Author: Jose G. Perez
# Last Date Modified: 12/4/2021
import matplotlib.pyplot as plt

class Maze:
    def __init__(self, maze_rows, maze_cols):
        self.maze_rows = maze_rows
        self.maze_cols = maze_cols

        self.wall_dict = {}

        for r in range(self.maze_rows):
            for c in range(self.maze_cols):
                w = []
                top_cell, right_cell = (r, c+1), (r+1, c)
                if self.in_bounds(top_cell):
                    w.append(top_cell)
                if self.in_bounds(right_cell):
                    w.append(right_cell)
                self.wall_dict[(r, c)] = w

    def walls(self, tuple_form=False):
        w = []
        for (cell_tuple, neighbors) in self.wall_dict.items():
            for neighbor_cell_tuple in neighbors:
                if tuple_form:
                    w.append([cell_tuple, neighbor_cell_tuple])
                else:
                    w.append([self.cell_tuple_to_int(cell_tuple), self.cell_tuple_to_int(neighbor_cell_tuple)])
        return w

    def cell_tuple_to_int(self, cell_tuple):
        r, c = cell_tuple
        return c + r * self.maze_cols

    def cell_int_to_tuple(self, cell_int):
        r = cell_int // self.maze_cols
        c = cell_int % self.maze_cols
        return (r, c)

    def in_bounds(self, cell):
        if type(cell) == int:
            cell = self.cell_int_to_tuple(cell)

        r, c = cell
        return r >= 0 and r < self.maze_rows and c >= 0 and c < self.maze_cols

    def remove_wall(self, wall):
        src_cell, dst_cell = wall[0], wall[1]

        if type(src_cell) == int:
            src_cell = self.cell_int_to_tuple(src_cell)
        if type(dst_cell) == int:
            dst_cell = self.cell_int_to_tuple(dst_cell)
        
        try:
            self.wall_dict[src_cell].remove(dst_cell)
        except ValueError:
            print(f'Tried to remove wall from {src_cell} to {dst_cell} but there is no wall to remove there')

    def draw(self, title='Maze', cell_info=False, save_fig=False, path=None):
        fig, ax = plt.subplots()
        plt.suptitle(title)

        for (cell_tuple, neighbors) in self.wall_dict.items():
            r, c = cell_tuple

            if cell_info:
                cell_int = self.cell_tuple_to_int(cell_tuple)
                ax.text((c+.5), (r+.5), f'{cell_int} {cell_tuple}', size=10, ha="center", va="center")

            for neighbor_cell_tuple in neighbors:
                nr, nc = neighbor_cell_tuple
                is_vertical_wall = nc > c

                assert self.cell_int_to_tuple(self.cell_tuple_to_int(cell_tuple)) == cell_tuple, 'Conversion formula seems to be incorrect'

                # Add walls
                if is_vertical_wall:
                    ax.plot([c+1, c+1], [r, r+1], linewidth=1, color='black')
                else:
                    ax.plot([c, c+1], [r+1, r+1], linewidth=1, color='black')

        # Draw outside borders
        sx = self.maze_cols
        sy = self.maze_rows
        ax.plot([0, 0, sx, sx, 0], [0, sy, sy, 0, 0], linewidth=2, color='k')

        # Draw path if available
        if path:
            for idx in range(len(path)-1):
                r, c = self.cell_int_to_tuple(path[idx])
                nr, nc = self.cell_int_to_tuple(path[idx+1])

                ax.plot([c+.5, nc+.5], [r+.5, nr+.5], linewidth=3, color='r')

        # Tweak some plot settings for better visuals
        ax.axis('off')
        ax.set_aspect(1.0)
        plt.show()

        if save_fig:
            plt.savefig(title + '.png')