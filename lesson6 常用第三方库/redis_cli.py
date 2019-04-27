import redis

class Queue:
    def __init__(self, name):
        self._db = redis.Redis(host='localhost', port='6379')
        self.key = '%s:%s' % ('redis_demo', name)

    def qsize(self):
        return self._db.llen(self.key)

    def empty(self):
        return self.qsize() == 0

    def put(self, item):
        self._db.rpush(self.key, item)

    def get(self, block=True, timeout=None):
        if block: # 阻塞
            item = self._db.blpop(self.key, timeout=timeout)
            if item:
                item = item[1]
        else: # 非阻塞
            item = self._db.lpop(self.key)
        return item
        
queue = Queue('julyedu')
queue.put('v1')
queue.put('v2')
queue.put('v3')
v = queue.get()
print(v)
v = queue.get()
print(v)