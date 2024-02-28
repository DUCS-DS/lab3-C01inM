from llist import LList, Node, append


import random


def length(lst):
    """return the length of a finite linked list"""
    counter = 0
    node = lst.head
    if lst.head:
        while node.next:
            node = node.next
            counter = counter + 1
        print("Fine, your list had something in it.")
    else:
        counter = 0
        print("The List is Empty Moron!")

    print(f"Number of Nodes: {counter}")


def llprint(lst):
    """print a finite linked list"""
    node = lst.head
    if lst.head:
        while node.next:
            print(node.val, end = " ")
            node = node.next
    else:
        print("EMPTY LIST! HOW MANY TIMES I GOTTA TELL YOU!")


if __name__ == "__main__":

    llist = LList()
    for i in range(10):
        append(llist, Node(random.randint(-100,100)))
    llprint(llist)
    from genfinite import lst 
    print(length(lst))