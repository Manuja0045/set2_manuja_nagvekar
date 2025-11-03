def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    def bfs(r, c):
        queue = [(r, c)]
        grid[r][c] = 0
        while queue:
            x, y = queue.pop(0)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                    grid[nx][ny] = 0
                    queue.append((nx, ny))

    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                count += 1
                bfs(i, j)

    return count


if __name__ == "__main__":
    test_cases = [
        {"name": "Basic Example", "grid": [[1, 1, 0, 0], [0, 1, 0, 1], [1, 0, 0, 1]], "expected": 3},
        {"name": "Multiple Clusters", "grid": [[1, 0, 1, 0], [1, 1, 0, 1], [0, 0, 1, 1], [0, 1, 0, 0]], "expected": 4},
        {"name": "No Land", "grid": [[0, 0, 0], [0, 0, 0]], "expected": 0},
        {"name": "Single Big Island", "grid": [[1, 1, 1], [1, 1, 1]], "expected": 1},
    ]

    
    print("ISLAND COUNTER TEST RESULTS")
    print("------------------------------------------------------------")

    print(f"{'Test Name':<25} | {'Output':<8} | {'Expected':<9} | {'Status'}")
    print("------------------------------------------------------------")

    import copy
    for case in test_cases:
        grid_copy = copy.deepcopy(case["grid"])
        output = count_islands(grid_copy)
        status = "PASS" if output == case["expected"] else "FAIL"
        print(f"{case['name']:<25} | {output:<8} | {case['expected']:<9} | {status}")

