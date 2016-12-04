from collections import deque


def populate_next_right_pointer(root):
    queue = deque()
    queue.append(root)

    while queue:
        sz = i = len(queue)
        for _ in xrange(sz):
            node = queue.popleft()
            if i > 1:
                node.next = queue[0]
                i -= 1
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
