### All you need
- init queue or stack or use recursive stack
- init visited set
- mark start u as visited and append to queue or stack
- start traversing from u
- proccess u first
- for each v (neighbour of u)
- if not in visited
- pop and mark as visited
- if not visited add to visited and append to queue or stack
- continue while queue or stack is not empty

### BFS vs DFS
BFS uses queue first in first out (FIFO) in python we can use collections dequeue, or pop(0) with lists, but it's better to use dequeue
DFS uses stack last in first out (LIFO) we just use it with list and pop


### Important note on DFS recursive vs DFS stack
Recursive DFS inspects neighbors in list order and always “dives” into the first available neighbor—so it’s left-first.

Iterative DFS with a plain stack inspects neighbors in list order but then visits them in reverse (because of LIFO), making it right-first.