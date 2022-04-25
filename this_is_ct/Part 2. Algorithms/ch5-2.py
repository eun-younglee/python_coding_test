# queue

from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.popleft()
print(queue)  # [4, 3]
