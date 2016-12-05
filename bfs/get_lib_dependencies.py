# Given a map of libraries and their immediate dependencies, 
# write a function that returns all dependencies of a given library.
# dependencies = {'foo': ['bar', 'baz'], 'bar': ['qux'], 'baz': ['bar']}
# foo_deps = get_lib_dependencies('foo', dependencies)
# foo_deps would contain the following 3 elements: bar, baz, qux

from collections import deque


def get_lib_dependencies(root, dependencies):
    queue, visited, res = deque(), set(), []
    queue.append(root)
    visited.add(root)

    while queue:
        cur = queue.popleft()
        res.append(cur)
        for nb in dependencies.get(cur, []):
            if nb not in visited:
                queue.append(nb)
                visited.add(nb)

    res.pop(0)
    return res


def main():
    dependencies = {'foo': ['bar', 'baz', 'qux'], 'bar': ['qux', 'qux2'], 'baz': ['bar'], 'ha': ['xa', 'pa', 'foo']}
    foo_deps = get_lib_dependencies('foo', dependencies)
    print foo_deps


if __name__ == '__main__':
    main()
