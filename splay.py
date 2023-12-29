def NewNode(key = None, value = None, left = None, right = None):
  node = [key, value, left, right]

  return node

class Splay_tree:
  def __init__(self):
    self.len = 0
    self.root = None
  def rightrotate(self, node):
    left_node = node[2]
    node[2] = left_node[3]
    left_node[3] = node
    return left_node
  def leftrotate(self, node):
    right_node = node[3]
    node[3] = right_node[2]
    right_node[2] = node
    return right_node
  def splay(self, root, key):
    if root == None or root[0] == key: return root
    if root[0] > key:
      if root[2] == None: return root
      if root[2][0] > key:
        root[2][2] = self.splay(root[2][2], key)
        root = self.rightrotate(root)
      elif root[2][0] < key:
        root[2][3] = self.splay(root[2][3], key)

        if root[2][3] != None:
          root[2] = self.leftrotate(root[2])
      if root[2] == None: return root
      else: return self.rightrotate(root)
    else:
      if root[3] == None: return root

      if root[3][0] > key:
        root[3][2] = self.splay(root[3][2], key)

        if root[3][2] != None:
          root[3] = self.rightrotate(root[3])
      elif root[3][0] < key:
        root[3][3] = self.splay(root[3][3], key)
        root = self.leftrotate(root)
      if root[3] == None: return root
      else: return self.leftrotate(root)

  def __getitem__(self, key):
    result = self.root
    self.root = self.splay(result, key)
    if self.root[0] == key: return self.root[1]
    else: raise KeyError(key)

  def insert(self, root, key, value):
    if root == None: 
      self.len += 1
      return NewNode(key, value)

    root = self.splay(root, key)
    if root[0] == key:
      root[1] = value
      return root

    newnode = NewNode(key, value)
    if root[0] > key:
      newnode[3] = root
      newnode[2] = root[2]
      root[2] = None
    else:
      newnode[2] = root
      newnode[3] = root[3]
      root[3] = None
    self.len += 1
    return newnode

  def __setitem__(self, key, value):
    self.root = self.insert(self.root, key, value)

  def delete(self, root, key):
    temp = NewNode()
    if root == None: return None

    root = self.splay(root, key)

    if key != root[0]: return root

    if root[2] == None:
      temp = root
      root = root[3]

    else:
      temp = root

      root = self.splay(root[2], key)

      root[3] = temp[3]

    return root

  def __delitem__(self, key):
    result = self.delete(self.root, key)
    if result == None or result == self.root:
      raise KeyError(key)
    else:
      self.root = result
      self.len -= 1

  def __contains__(self, key):
    result = self.root
    self.root = self.splay(result, key)
    if self.root == None: return False
    if self.root[0] == key: return True
    else: return False

  def __len__(self):
    return self.len
