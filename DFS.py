graph = {'A': {'B', 'C'},
         'B': {'A', 'D', 'E'},
         'C': {'A', 'F'},
         'D': {'B'},
         'E': {'B', 'F'},
         'F': {'C', 'E'}
         }


def dfs(graph, start):
    visited, stack = [], [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.extend(vertex)
            stack.extend(graph[vertex] - set(visited))
    return visited


print(dfs(graph, 'A'))  # {'E', 'D', 'F', 'A', 'C', 'B'}


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
# l1 = list(dfs_paths(graph, 'A', 'E'))
# print(l1)
