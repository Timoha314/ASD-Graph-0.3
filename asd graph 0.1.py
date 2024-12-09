with open('input.txt', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    adjacency_list = [[] for _ in range(n)]
    for _ in range(m):
        u, v = map(int, file.readline().strip().split())
        adjacency_list[u - 1].append(v)
        adjacency_list[v - 1].append(u)

with open('output.txt', 'w') as file:
    for neighbors in adjacency_list:
        file.write(f"{len(neighbors)} " + " ".join(map(str, neighbors)) + "\n")