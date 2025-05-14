
from collections import deque

class binaryNode:
    def __init__(self, nodeVal):
        self.nodeVal = nodeVal
        self.left = None
        self.right = None

    def addLeftNode(self, nodeVal):
        if self:
            node = binaryNode(nodeVal)
            self.left = node
        else:
            print("Parent is None")

    def addRightNode(self, nodeVal):
        if self:
            node = binaryNode(nodeVal)
            self.right = node
        else:
            print("Parent is None")

    # preorder
    def printPreorder(self):
        stack = []
        if not self:
            return

        stack.append(self)

        print("Preorder traversal: [ ", end="")
        while stack:
            node = stack.pop()
            print(node.nodeVal, end=" ")

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        print("]")

    def printInorder(self):
        stack = []
        current = self

        print("Inorder traversal: [ ", end="")
        while current or stack:
            # Reach the leftmost node of the current subtree
            while current:
                stack.append(current)
                current = current.left

            # current is none, so pop from stack
            current = stack.pop()
            print(current.nodeVal, end=" ")

            # Move to the right child
            current = current.right

        print("]")

    def printLevelOrder(self):
        if not self:
            return

        queue = deque()
        queue.append(self)
        print("Level order traversal: [ ", end="")
        while queue:
            n = len(queue)
            while n:
                node = queue.popleft()

                print(node.nodeVal, end=" ")
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                n-=1

        print("]")

    def printPostOrder(self):
        if not self:
            return

        stack = []
        current = self
        lastVisited = None
        print("Postorder traversal: [ ", end="")
        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            # current is now none, peak its parent and goto right
            parent = stack[-1]
            # if right child exists and hasn't been visited yet, go right
            if parent.right and lastVisited != parent.right:
                current = parent.right
            else:
                print(parent.nodeVal, end=" ")
                lastVisited = stack.pop()
                current = None # don't go left again

        print("]")

def createTreeWrapper():
    nodeQueue = deque()

    print("Enter root node value: ", end="")
    nodeVal = int(input())

    if nodeVal != -1:
        root = binaryNode(nodeVal)
        nodeQueue.append(root)
    else:
        print("No root. Tree not created.")
        return None

    while nodeQueue:
        parentNode = nodeQueue.popleft()

        leftNodeVal, rightNodeVal = map(int, input(f"Left and right for {parentNode.nodeVal}: ").split())

        if leftNodeVal != -1:
            parentNode.addLeftNode(leftNodeVal)
            nodeQueue.append(parentNode.left)

        if rightNodeVal != -1:
            parentNode.addRightNode(rightNodeVal)
            nodeQueue.append(parentNode.right)

    print("Binary Tree building finished!")
    return root

def searchInorder(inorder, inStart, inEnd, nodeVal):
    for i in range(inStart, inEnd+1):
        if inorder[i] == nodeVal:
            return i

    return -1


def generateTree(preorder, inorder, preIndex, inStart, inEnd):
    print(f"preIndex {preIndex}")
    if inStart > inEnd:
        return None

    root = binaryNode(preorder[preIndex[0]])
    preIndex[0]+=1
    if inStart == inEnd:
        return root

    splitIndex = searchInorder(inorder, inStart, inEnd, root.nodeVal)
    root.left = generateTree(preorder, inorder, preIndex, inStart, splitIndex-1)
    root.right = generateTree(preorder, inorder, preIndex, splitIndex+1, inEnd)

    return root

if(__name__ == "__main__"):
    print("code is being run from cmd line.")
    root = createTreeWrapper()
    root.printPreorder()
    root.printInorder()
    root.printLevelOrder()
    root.printPostOrder()

    # generate tree from preorder and inorder
    preorder = [1,2,4,5,3,6,7]
    inorder = [4,2,5,1,6,3,7]
    preIndex = [0]

    root = generateTree(preorder, inorder, preIndex, 0, len(inorder)-1)
    root.printPreorder()
    root.printInorder()
