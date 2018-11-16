import queue as queue

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # initialize a list to use as a stack
    stack = [self]
    # while there are elements in the list, do this logic
    while len(stack) > 0:
      current = stack.pop()
      cb(current.value)
      # the right > left ordering is important here
      if current.right:
        stack.append(current.right)
      if current.left:
        stack.append(current.left)

  def breadth_first_for_each(self, cb):
    # base case for empty tree
    if self.value == None:
      return

    # initialize our storage queue
    storage = queue.Queue()
    # add the root node
    storage.put(self)

    # do this while there are nodes in queue
    while not storage.empty():
      # process the queued node (in first case, the root note)
      current = storage.get()
      # run the cb() on its value
      cb(current.value)
      if current.left:
        # if current has left child, add to queue
        storage.put(current.left)
      if current.right:
        # if current has right child, add to queue
        storage.put(current.right)
    
    # the while loop will traverse all nodes and run the cb() on each of their values until the queue is empty
    # pass

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
