from collections import deque

def shortest_path(grid: list[list[int]]) -> int:
    """
    Find the length of the shortest path from the start of an adjacency matrix to the end of it
    """
    # keep count of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])

    # store a tuple of (row, column in the queue and hash set)
    queue: deque[tuple[int, int]] = deque()
    visited: set[tuple[int, int]] = set()

    # initialize with first entry of the grid
    queue.append((0, 0))
    visited.add((0, 0))
    
    length = 0

    while queue:
        # operate on current neighbors
        for _ in range(len(queue)):
            # get current element 
            (row, col) = queue.popleft()

            # check if destination is reached
            if row == rows - 1 and col == cols - 1:
                return length


            # get movement to valid neighbors. thus, the 4 valid movement paths in a list of tuples (row, col). 2 row movements, 2 column movements
            movements: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for (row_move, col_move) in movements:
                row1, col1 = row + row_move, col + col_move
                
                # check if path is valid
                if (row1 < 0 or col1 < 0) or (row1 >= rows or col1 >= cols) or ((row1, col1) in visited) or (grid[row1][col1] == 1):
                    continue

                queue.append((row1, col1))
                visited.add((row1, col1))
        
        length += 1

    
    return length


if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0],
    ]

    result = shortest_path(grid)
    print(result)
