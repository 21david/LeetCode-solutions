class Node:
    def __init__(self, val):
        self.children = {}  # { "folderName (String)" : Node}
        self.val = val

class FileSystem:

    def __init__(self):
        self.root = Node(None)

    def createPath(self, path: str, value: int) -> bool:
        chain = path.split("/")[1:]
        print(chain)

        temp = self.root
        for folder in chain[:-1]:
            if folder in temp.children:
                temp = temp.children[folder]
            else:
                return False

        if chain[-1] in temp.children:
            return False

        temp.children[chain[-1]] = Node(value)
        return True


    def get(self, path: str) -> int:
        chain = path.split("/")[1:]

        temp = self.root
        for folder in chain:
            if folder in temp.children:
                temp = temp.children[folder]
            else:
                return -1

        return temp.val

        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)
