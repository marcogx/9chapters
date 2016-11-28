# http://www.geeksforgeeks.org/shortest-path-in-a-binary-maze/

from collections import deque


def find_min_steps(maze, x, y):
    if not maze or not maze[0] or maze[0][0] == 1:
        return -1

    rows, cols = len(maze), len(maze[0])
    if rows < 1 or cols < 1 or x < 0 or x >= rows or y < 0 or y >= cols:
        return -1

    visited = [[0 for _ in xrange(cols)] for _ in xrange(rows)]
    for r in xrange(rows):
        for c in xrange(cols):
            visited[r][c] = maze[r][c]

    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        point = queue.popleft()
        px, py, step = point[0], point[1], point[2]
        if px == x and py == y:
            return step
        maze[px][py] = 1
        if px - 1 >= 0 and maze[px - 1][py] == 0:
            queue.append((px - 1, py, step + 1))
        if px + 1 < rows and maze[px + 1][py] == 0:
            queue.append((px + 1, py, step + 1))
        if py - 1 >= 0 and maze[px][py - 1] == 0:
            queue.append((px, py - 1, step + 1))
        if py + 1 < cols and maze[px][py + 1] == 0:
            queue.append((px, py + 1, step + 1))

    return -1


def main():
    m = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 1, 0], [1, 1, 1, 1, 0], [0, 0, 0, 1, 0]]
    print find_min_steps(m, 3, 4)


if __name__ == '__main__':
    main()
