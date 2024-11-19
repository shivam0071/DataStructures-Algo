# Breadth First Search


### BFS on Trees – Exploring Level by Level
In a tree, you have a "root" at the top. BFS explores this root, then checks all nodes directly connected to it (its "children"), before moving on to the next layer down (the children of children), and so on. This level-by-level approach keeps you "close to home" before venturing farther out.

The queue is essential for BFS, keeping track of where you've been and what’s next.

### TREE Template for BFS
    from collections import deque

    # Tree Node structure
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def bfs_tree(root):
        if not root:
            return
    
    queue = deque([root])  # Start with the root in the queue

    while queue:
        node = queue.popleft()  # Get the next node to process
        print(node.value)  # Process the node (e.g., print its value)

        # Add the children to the queue, if they exist
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)



### BFS on a 2D List (Grid) – Moving Through Layers

Imagine standing on a tiled floor. Each tile represents a cell in the 2D list (grid), and BFS explores all tiles connected to you, one "ring" at a time.

Steps for BFS in a Grid:

1. Start at your position (say, [0][0]).
2. Move in four directions (up, down, left, right) to visit adjacent cells.
3. After covering all immediate neighbors, move to the next "layer" (neighbors of neighbors).
4. Repeat until all reachable tiles are explored.

### Template of BFS for 2-D Array

    from collections import deque

    # Define the BFS function for a 2D grid
    def bfs_grid(grid, start):
        rows, cols = len(grid), len(grid[0])
        queue = deque([start])  # Start BFS from the initial position
        visited = set([start])  # Track visited cells to avoid revisiting
    
        # Directions for moving in the grid (up, down, left, right)
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
        while queue:
            x, y = queue.popleft()  # Current cell
            print(f"Visiting cell ({x}, {y}) with value {grid[x][y]}")  # Process the cell
    
            # Explore the four possible directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
    
                # Check if the new position is within bounds and unvisited
                if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                    visited.add((nx, ny))  # Mark the new cell as visited
                    queue.append((nx, ny))  # Add the new cell to the queue
    
    bfs_grid(grid, (0, 0))  # Starts from top-left corner, visiting each cell




# *** PROBLEMS ***

### 7.) 200. Number of Islands

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def bfs(r, c):
            q = deque()
            visit.add((r, c))
            q.append((r, c))

            while q:
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                r, c = q.popleft()
                for dr, dc in directions:
                    dr, dc = r + dr, c + dc

                    if dr in range(row) and dc in range(col) and grid[dr][dc] == "1" and (dr, dc) not in visit:
                        q.append((dr, dc))
                        visit.add((dr, dc))

        count = 0
        row = len(grid)
        col = len(grid[0])
        visit = set()

        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1' and (r, c) not in visit:
                    bfs(r, c)
                    count += 1
        return count

    # This is almost a copy of above Template, Trick here was BFS ofcourse
    # O(M * N)