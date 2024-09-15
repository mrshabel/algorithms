def unique_paths_in_matrix(grid: list[list[int]]) -> int:
    """
    Count the unique paths from the top left to bottom right of a matrix where only 0's can be visited
    """
    def dfs(grid: list[list[int]], start_row: int, start_col: int, visited: set[tuple[int, int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        count = 0
        # edge cases
        if (start_row < 0 or start_col < 0) or (start_row >= rows or start_col >= cols) or ((start_row, start_col) in visited)  or (grid[start_row][start_col] == 1):
            return 0
        # base case for when last node is reached
        if start_row == rows - 1 and start_col == cols - 1:
            return 1
        
        # mark current position as visited
        visited.add((start_row, start_col))
        
        # recursively calculate the length of the unique path
        # move left
        count += dfs(grid=grid, start_row=start_row, start_col=start_col - 1, visited=visited)
        # move right
        count += dfs(grid=grid, start_row=start_row, start_col=start_col + 1, visited=visited)
        # move up
        count += dfs(grid=grid, start_row=start_row - 1, start_col=start_col, visited=visited)
        # move down
        count += dfs(grid=grid, start_row=start_row + 1, start_col=start_col, visited=visited)

        # backtrack by removing the currently visited position
        visited.remove((start_row, start_col))

        return count
    
    return dfs(grid=grid, start_row=0, start_col=0, visited=set())


if __name__ == "__main__":
    matrix = [
        [0, 0, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 1, 0, 0]
    ]

    result = unique_paths_in_matrix(matrix)
    print(result)