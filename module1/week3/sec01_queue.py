class Queue:
    def __init__(self, capacity):
        self.__capacity = capacity
        self.__storage = []

    def is_empty(self):
        return self.__storage == []

    def is_full(self):
        return len(self.__storage) == self.__capacity

    def enqueue(self, value):
        self.__storage.append(value)

    def dequeue(self):
        value = self.__storage.pop(0)

        return value

    def front(self):

        return self.storage[0]


if __name__ == '__main__':
    queue1 = Queue(capacity=5)
    queue1.enqueue(1)
    queue1.enqueue(2)


    print(queue1.is_empty())
    print(queue1.is_full())
   

    value = queue1.dequeue()
    print(value)
    

    front_value = queue1.front()
    print(front_value)