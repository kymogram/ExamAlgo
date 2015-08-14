def AfficheChemins(tree, path=[]):
    if tree.RightChild != None or tree.LeftChild != None:
        path.append(tree.getRootVal())
        AfficheChemins(tree.LeftChild, path)
        AfficheChemins(tree.RightChild, path)
    else:
        print(path)
        path.pop()

def sommeChemin(tree, somme, valPath=0):
    if tree.RightChild != None or tree.LeftChild != None:
        valPath += tree.getRootVal()
        if sommeChemin(tree.LeftChild, somme, valPath):
            return True
        if sommeChemin(tree.RightChild, somme, valPath):
            return True
    else:
        if valPath == some:
            return True
        path -= tree.getRootVal()

def main():
    tree = BinaryTree(5, BinaryTree(4, BinaryTree(11, BinaryTree(7), BinaryTree(2))), BinaryTree(8, BinaryTree(13), BinaryTree(4, BinaryTree(1))))
    AfficheChemins(tree)