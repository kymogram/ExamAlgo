def AfficheChemins(tree, path=[]):
    if tree.RightChild != None and tree.LeftChild != None:
        path.append(tree.getRootVal())
        AfficheChemins(tree.LeftChild, path)
        AfficheChemins(tree.RightChild, path)
    else:
        printPath()
        path.pop()

def printPath(path):
    print(path)

def sommeChemin(arbre, somme, valPath=0):
    if tree.RightChild != None and tree.LeftChild != None:
        valPath += tree.getRootVal()
        AfficheChemins(tree.LeftChild, path)
        AfficheChemins(tree.RightChild, path)
    else:
        if valPath == some:
            # Ici je fais un return True, mais ça n'arrête pas la fonction
            # pour autant.. je dois mettre où l'autre return True ?
            return True
        path -= tree.getRootVal()

def main():
    tree = BinaryTree(5, BinaryTree(4, BinaryTree(11, BinaryTree(7), BinaryTree(2))), BinaryTree(8, BinaryTree(13), BinaryTree(4, BinaryTree(1))))
    AfficheChemins(tree)