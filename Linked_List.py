class Linked_List:

  class __Node:

    def __init__(self, val):
        self.element = val
        self.next = None #will be filled when we add more things to this list..
        self.prev = None  # for now referencing sentinel None

  def __init__(self):
    self.__header = self.__Node(None)
    self.__trailer = self.__Node(None)
    self.__trailer.prev = self.__header
    self.__header.next = self.__trailer
    self.__size = 0


  def __len__(self):
    return self.__size

  def append_element(self, val):
    new_node = self.__Node(val)
    new_node.prev = self.__trailer.prev
    new_node.next = self.__trailer
    self.__trailer.prev.next = new_node
    self.__trailer.prev = new_node

    self.__size += 1

  def insert_element_at(self, val, index):

    if index >= self.__size or index <= -1: #if index is greater than number of items or if index is negative.
        raise IndexError

    new_node = self.__Node(val)
    self.half= self.__size // 2
    if index == 0:
        new_node.next = self.__header.next
        new_node.prev = self.__header
        self.__header.next.prev = new_node
        self.__header.next = new_node

        self.__size += 1
    elif index == 1 or index <= self.half: #execute if index is less than half of the size
        cur= self.__header
        for i in range(0, index):
            cur = cur.next
        new_node.next = cur.next
        new_node.prev = cur
        cur.next.prev = new_node
        cur.next = new_node

        self.__size += 1
    else: #execute if the index is more than half of the size... so it only traverses through half of the list
        cur = self.__trailer
        for i in range(self.__size-index):
            cur= cur.prev
        new_node.prev = cur.prev
        new_node.next = cur
        cur.prev.next = new_node
        cur.prev = new_node
        self.__size += 1

  def remove_element_at(self, index):
    if index >= self.__size or index <= -1: #raise error if index is out of bounds
        raise IndexError
    self.half = self.__size // 2
    if (index == 1) or (index <= self.half): #if index is in the first half, execute
        cur= self.__header
        for i in range(index): #start a walk from header to index
            cur = cur.next
        returned = cur.next.element
        cur.next.next.prev = cur
        cur.next = cur.next.next
        self.__size -= 1
        return returned
    else:   # if index is in the second half, execute
        cur= self.__trailer
        for i in range((self.__size - 1) - index): # last index- index of number we want to remove
            cur = cur.prev
        returned = cur.prev.element
        cur.prev.prev.next= cur
        cur.prev = cur.prev.prev
        self.__size -= 1
        return returned

  def get_element_at(self, index):
    if index >= self.__size or index <= -1: #raise error if index is out of bounds
        raise IndexError
    self.half = self.__size // 2
    if (index == 1) or (index <= self.half):
        cur = self.__header
        for i in range(index + 1):
            cur = cur.next
        return cur.element
    else:
        cur= self.__trailer
        for i in range(self.__size-index):
            cur = cur.prev
        return cur.element

  def rotate_left(self):
    head = self.__header.next.element #stores element
    cur = self.__header.next #current node
    if self.__size > 1:
        for i in range(0,self.__size):
            if i >= 1:
                cur = cur.next
                cur.prev.element = cur.element
            if i==self.__size-1:
                self.__trailer.prev.element= head

  def __str__(self):
    if self.__size == 0:
        return "[ ]"
    else:
        cur= self.__header.next
        final_ans= "[ " + str(cur.element)
        while cur.next is not self.__trailer:
            cur= cur.next
            final_ans += ", " + str(cur.element)
        final_ans += " ]"
        return final_ans


  def __iter__(self):
    self.__iter__index = self.__header.next
    return self

  def __next__(self):
    if self.__iter__index == self.__trailer:
        raise StopIteration
    element = self.__iter__index.element
    self.__iter__index = self.__iter__index.next
    return element
