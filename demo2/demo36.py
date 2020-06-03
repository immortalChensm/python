import collections
#列队

queue = collections.deque()

queue.append("a")
print(queue)
queue.append("b")
queue.append("c")

print(queue)

print(queue.popleft())