from Deque_Generator import get_deque

class Queue:

  def __init__(self):
    # TODO replace pass with your implementation.
    self.__dq = get_deque()

  def __str__(self):
    return self.__dq.__str__()

  def __len__(self):
    return self.__dq.__len__()

  def enqueue(self, val):
    self.__dq.push_back(val)
  def dequeue(self):
    return self.__dq.pop_front()

  def peek(self):
    return self.__dq.peek_front()
