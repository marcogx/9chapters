class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class TreeLinkNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None