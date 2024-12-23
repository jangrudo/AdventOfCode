from aoc_shortcuts import *

f = open('input')

m = mread(f)

start = mfind(m, 'S')[0]
finish = mfind(m, 'E')[0]

q = {start}
visited = {start}
prev = {}

for iteration in urange(1):
    nq = set()

    for i, j in q:
        for ni, nj in deltas(m, i, j):
            if m[ni][nj] != '#' and (ni, nj) not in visited:
                visited.add((ni, nj))
                nq.add((ni, nj))
                prev[(ni, nj)] = (i, j)

    q = nq

    if finish in nq:
        break

path = [finish]
while path[-1] != start:
    path.append(prev[path[-1]])

path = list(reversed(path))

count = 0

# Ensure steady progress by pre-calculating the total pair count.
progress = tqdm(total = ((len(path)) * (len(path) - 1)) // 2)

for i in range(len(path) - 1):
    for j in range(i + 1, len(path)):
        shortcut = abs(path[i][0] - path[j][0]) + abs(path[i][1] - path[j][1])
        if shortcut <= 20:
            cheat_path = len(path) - (j - i) + shortcut

            if cheat_path <= len(path) - 100:
                count += 1

    # Updating the progress inside the inner loop is too slow even for tqdm.
    progress.update(len(path) - i - 1)
progress.close()

print(count)
