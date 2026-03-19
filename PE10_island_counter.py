from collections import deque

# Import deque for efficient queue operations in BFS.

class IslandCounterClass:
  """
  Class to count islands using Breadth-First Search.
  Logging visited islands so we do not count them more than once.
  """

  def __init__(self, grid):
    """
    Initializes Class with Grid

    Parameters
    ----------
    grid : 2d-array
      Grid made up of lists where 1 represents islands and 0 represents water.
    """
    # Store input grid in object.
    self.grid = grid
    # Create visited grid same size as grid, initialized to "0".
    self.visited = [['0' for x in range(len(grid[0]))] for y in range(len(grid))]

  def print_grid_visited(self):
    """ Outputs current state of grid and visited grid """
    # Print map grid.
    print("Map:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.grid]))
    # Print visited marker grid.
    print("Visited:")
    print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.visited]))

  def count_island(self):
    """
    Iterates through the grid counting the islands.
    Marks when an island has been visited to skip future iterations.
    This avoids duplicate counts.

    Returns
    -------
    int
      Number of islands detected. (1 and 3 in this case)
    """
    # Keep island count in result.
    result = 0
    # Iterate through each row index.
    for i in range(len(self.grid)):
      # Iterate through each column index.
      for j in range(len(self.grid[0])):
        # If current cell is land and not tracked as visited
        if self.grid[i][j] == "1" and self.visited[i][j] == "0":
          # Mark all connected island cells via BFS.
          self.mark_visited_island(i, j)
          # Increment island count once for new island.
          result += 1
    # Return total number of distinct islands.
    return result

  def mark_visited_island(self, x, y):
    """
    Method used by count_island to mark an entire island as visited.

    Parameters
    ----------
    x : integer
      Row index of first land cell.
    y : integer
      Column index of first land cell.
    """
    # Use two parallel queues for BFS row and column coordinates.
    queue_x = deque()
    queue_y = deque()
    # Enqueue starting land coordinates.
    queue_x.append(x)
    queue_y.append(y)
    # Mark starting cell as visited.
    self.visited[x][y] = "1"
    # Define 4-directional neighbor offsets (up, down, left, right).
    orientation = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Perform BFS to visit all connected land cells in island.
    while queue_x:
      # Dequeue next current coordinates.
      curr_x = queue_x.popleft()
      curr_y = queue_y.popleft()
      # Check each neighbor direction.
      for a, b in orientation:
        c, d = curr_x + a, curr_y + b
        # Verify neighbor is inside grid bounds.
        if 0 <= c < len(self.grid) and 0 <= d < len(self.grid[0]):
          # If neighbor is land and unvisited, mark and enqueue it.
          if self.grid[c][d] == "1" and self.visited[c][d] == "0":
            queue_x.append(c)
            queue_y.append(d)
            self.visited[c][d] = "1"

"""
def mark_visited_island_recursive(x, y):
    if x < 0 or x >= rows or y < 0 or y >= cols:
        return
    if grid[x][y] == "0" or visited[x][y] == "1":
        return

    visited[x][y] = "1"

    # Recursively visit neighbors
    mark_visited_island_recursive(x - 1, y)  # up
    mark_visited_island_recursive(x + 1, y)  # down
    mark_visited_island_recursive(x, y - 1)  # left
    mark_visited_island_recursive(x, y + 1)  # right
"""