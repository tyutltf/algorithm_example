from queue import Queue

q = Queue(maxsize=0)

q.put(1)
q.put(2)

# 输出队列
print(q.queue)
# 返回队列头
print(q.get())
# 返回队列长度
print(q.qsize())
# 判断队列是否为空
print(q.empty())
# 判断队列是否全满
print(q.full())
