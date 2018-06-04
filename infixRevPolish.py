def preExp(expression):
    posExp = posRead(parser(expression))
    inExp = inRead(parser(expression))
    return "Reverse Polish: " + posExp + "\n" + "Infix: " + inExp


def parser(expression):
    tree = []
    if len(expression) == 1:
        return expression
    if expression[0] in "+-/*":
        nexp = expression[1:len(expression)-1]
        tree += [expression[0]] + [parser(nexp)] + [expression[len(expression)-1]]
        return tree

            
def posRead(tree):
    if len(tree[1]) == 1:
        leftChild = tree[1]
        rightChild = tree[2]
        root = tree[0]
        return leftChild + rightChild + root
    else:
        root = tree[0]
        leftChild = posRead(tree[1])
        rightChild = tree[2]
        return leftChild + rightChild + root


def inRead(tree):
    if len(tree[1]) == 1:
        leftChild = tree[1]
        rightChild = tree[2]
        root = tree[0]
        return leftChild + root + rightChild
    else:
        root = tree[0]
        leftChild = inRead(tree[1])
        rightChild = tree[2]
        return leftChild + root + rightChild


                
