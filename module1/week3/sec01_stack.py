# Implement class Stack

class Stack:
    def __init__(self, capacity=0):
        self.__capacity = capacity
        self.__storage = []

    def is_empty(self):
        return self.__storage == []

    def is_full(self):
        return len(self.__storage) == self.__capacity

    def pop(self):
        value = self.__storage.pop()

        return value
       
    def push(self, element):
        if len(self.__storage) <= self.__capacity:
            self.__storage.append(element)
        else:
            print('Stack is full!')

    def top(self):
        return self.__storage[-1]

if __name__ == '__main__':
    stack = Stack(3)

    stack.push(1)
    stack.push(2)
    stack.push(3)



    print(stack.is_empty())
    print(stack.is_full())
    val = stack.pop()
    print("pop value", val)


    top = stack.top()
    print("top value", top)
