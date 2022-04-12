#CS 2302
#Bradley Beltran
#Lab 3
#Instructor: Olac Fuentes
#Teaching Assistant: Jose Perez
#Instructional Assistant: David Dominguez

import matplotlib.pyplot as plt
import numpy as np
import random

import dsf
import graph_AL
from maze import Maze

# ************************ PART I: Create a maze with a disjoint-set forest ************************
def create_maze_regular_DSF(M, N):
    # Create a full maze with all adjacent cells separated by a wall
    maze = Maze(M, N)

    # Draw the maze
    maze.draw(f'{M}x{N} maze', cell_info=False)
    maze.draw(f'{M}x{N} maze with cell numbers', cell_info=True)

    # Get the list of all the walls of the maze in integer form
    # Then pick a random wall
    # Then remove it from the maze
    # And finally remove it from the list of walls
    #walls = maze.walls(tuple_form=False)
    #random_wall = random.choice(walls)
    #maze.remove_wall(random_wall)
    #walls.remove(random_wall)
    #print('We will be removing the wall between: ', random_wall)

    # Get the list of all the walls of the maze in tuple form
    # Then pick a random wall
    # Then remove it from the maze
    # And finally remove it from the list of walls
    #walls = maze.walls(tuple_form=True)
    #random_wall = random.choice(walls)
    #maze.remove_wall(random_wall)
    #walls.remove(random_wall)
    #print('We will be removing the wall between: ', random_wall)

    # Draw the maze after removing both walls
    maze.draw(f'{M}x{N} maze after removing randomly-chosen walls', cell_info=True)

    # Assign each cell to a different set in a DSF
    n_sets = M * N
    S = dsf.DSF(n_sets)
    G = graph_AL.Graph(n_sets)
    walls = maze.walls(tuple_form=False)
    while n_sets>1:
        random_wall = random.choice(walls)
        if not S.in_same_set(random_wall[0],random_wall[1]):
            S.union(random_wall[0], random_wall[1])
            maze.remove_wall(random_wall)
            walls.remove(random_wall)
            G.insert_edge(random_wall[0], random_wall[1],weight=1)
            n_sets-=1                    

    # Create a graph for the maze to be used later for graph search

    # DO NOT CHANGE THE RETURN FUNCTION!
    return maze, S, G

# ************************ PART II: Disjoint Set Forest using Dictionaries ************************
class DSF_Dict:
    def __init__(self):
        self.parent = {}

    def find(self, cell):
        assert type(cell) == tuple, 'cell must be a tuple'

        if cell not in self.parent:
            self.parent[cell] = 1
        if type(self.parent[cell]) == int:
            return cell
        return self.find(self.parent[cell])

    def in_same_set(self, c1, c2):
        return self.find(c1) == self.find(c2)

    def union(self, c1, c2):
        assert type(c1) == tuple, 'c1 must be a tuple'
        assert type(c2) == tuple, 'c2 must be a tuple'

        # ************************ WRITE YOUR CODE HERE! ************************
        # ************************ WRITE YOUR CODE HERE! ************************
        # ************************ WRITE YOUR CODE HERE! ************************
        root_i = self.find(c1)
        root_j = self.find(c2)
        if root_i != root_j:
            if self.parent[root_i]<self.parent[root_j]:
                self.parent[root_i] += self.parent[root_j]
                self.parent[root_j] = root_i
            else:
                self.parent[root_j] += self.parent[root_i]
                self.parent[root_i] = root_j
            return 1
        return 0

def create_maze_dictionary_DSF(M, N):
    # Create a full maze with all adjacent cells separated by a wall
    maze = Maze(M, N)

    # Assign each cell to a different set in the dictionary DSF
    n_sets = M * N
    S = DSF_Dict()

    # Create a graph for the maze to be used later for graph search
    G = graph_AL.Graph(n_sets)

    # ************************ WRITE YOUR CODE HERE! ************************
    # ************************ WRITE YOUR CODE HERE! ************************
    # ************************ WRITE YOUR CODE HERE! ************************
    maze.draw(f'{M}x{N} maze with cell numbers', cell_info=True)

    # Get the list of all the walls of the maze in tuple form
    # Then pick a random wall
    # Then remove it from the maze
    # And finally remove it from the list of walls
    walls = maze.walls(tuple_form=True)
    while n_sets>1:
        random_wall = random.choice(walls)
        if not S.in_same_set(random_wall[0],random_wall[1]):
            S.union(random_wall[0], random_wall[1])
            maze.remove_wall(random_wall)
            walls.remove(random_wall)
            G.insert_edge(maze.cell_tuple_to_int(random_wall[0]), maze.cell_tuple_to_int(random_wall[1]),weight=1)
            n_sets-=1

    # Draw the maze after removing both walls
    maze.draw(f'{M}x{N} maze after removing randomly-chosen walls', cell_info=True)

    # DO NOT CHANGE THE RETURN FUNCTION!
    return maze, S, G

# ************************ PART III: Solve the maze using Graph Search ************************
def get_path(prev,v):
    if prev[v]<0:
        return [v]
    return get_path(prev,prev[v]) + [v]

# Note that G will be created using the create_maze() functions so you need to be sure to create the graph inside them
def solve_maze_bfs(maze, G):
    solution_path = [0,1]
    # ************************ WRITE YOUR CODE HERE! ************************
    # ************************ WRITE YOUR CODE HERE! ************************
    # ************************ WRITE YOUR CODE HERE! ************************
    visited = set([solution_path[0]])
    prev = [-1 for i in range(len(G.AL))]
    Q = [0]
    while len(Q)>0:
        u = Q.pop(0)
        for edge in G.AL[u]:
            if edge.dest not in visited:
                prev[edge.dest] = u
                visited.add(edge.dest)
                Q.append(edge.dest)
    solution_path = get_path(prev, len(G.AL)-1)
    return solution_path

def solve_maze_dfs(maze, G):
    solution_path = [0, 1]
    # ************************ WRITE YOUR CODE HERE! ************************
    # ************************ WRITE YOUR CODE HERE! ************************
    # ************************ WRITE YOUR CODE HERE! ************************
    def depth_first_search(G,source=0,visited=None,prev=None):
        if visited==None:
            visited = set()
        if prev ==None:
            prev = [-1 for i in range(len(G.AL))]
        visited.add(source)
        for edge in G.AL[source]:
            if edge.dest not in visited:
                prev[edge.dest] = source
                depth_first_search(G,edge.dest,visited,prev)
        return prev
    
    prev = depth_first_search(G)
    solution_path = get_path(prev, len(G.AL)-1)
    return solution_path

# ************************ Program Main Function ************************
if __name__ == "__main__":
    # Close all current active plots
    plt.close("all")

    # Maze properties
    n_rows = 4
    n_cols = 4

    # Generate a maze using a regular DSF
    M, S, G = create_maze_regular_DSF(n_rows, n_cols)
    M.draw('Maze #1 generated using regular DSF')
    G.draw()
    # S.draw()
    # print(S.parent)

    # Generate solutions using BFS and DFS
    path_bfs = solve_maze_bfs(M, G)
    path_dfs = solve_maze_dfs(M, G)
    M.draw('Solution to maze #1 using BFS', path=path_bfs)
    M.draw('Solution to maze #1 using DFS', path=path_dfs)

    # Generate a maze using the dictionary DSF
    M, S, G = create_maze_dictionary_DSF(n_rows, n_cols)
    M.draw('Maze #2 generated using dictionary version of DSF')

    # Generate solutions using BFS and DFS
    path_bfs = solve_maze_bfs(M, G)
    path_dfs = solve_maze_dfs(M, G)
    M.draw('Solution to maze #2 using BFS', path=path_bfs)
    M.draw('Solution to maze #2 using DFS', path=path_dfs)