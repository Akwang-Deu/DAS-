#implementing using collections.deque
from collections import deque
q= deque()
#adding elements to a queue
q.append('Kenya')
q.append('Uganda')
q.append('Malawi')
q.append('South Sudan')
q.append('Tanzania')
print(q)
print(type(q))


#dequeued from queue

print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q.popleft())

print(q)
