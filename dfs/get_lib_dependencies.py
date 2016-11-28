# Given a map of libraries and their immediate dependencies, 
# write a function that returns all dependencies of a given library.
# dependencies = {'foo': ['bar', 'baz'], 'bar': ['qux'], 'baz': ['bar']}
# foo_deps = get_lib_dependencies('foo', dependencies)
# foo_deps would contain the following 3 elements: bar, baz, qux


def get_lib_dependencies(root, graph):
    visited, res = set(), []
    dfs(root, graph, visited, res)
    res.pop(0)
    return res


def dfs(cur, graph, visited, res):
    res.append(cur)
    visited.add(cur)
    for nb in graph.get(cur, []):
        if nb not in visited:
            dfs(nb, graph, visited, res)


def main():
    dependencies = {'foo': ['bar', 'baz', 'qux'], 'bar': ['qux', 'qux2'], 'baz': ['bar'], 'ha': ['xa', 'pa', 'foo']}
    foo_deps = get_lib_dependencies('foo', dependencies)
    print foo_deps


if __name__ == '__main__':
    main()