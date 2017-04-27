# Long Yu
# Date: April 18th 2017
# Description: Linked List 



class StackLinkedList:
    """ Using Linked List to implement Stack"""

    class _Node:
        """ Internal node class for a LL """
        __slots__ = '_element', '_next'

        def __init__(self, e, next):
            """ _element : value of the node 
            _next : act like a pointer to next node
            """
            self._element = e
            self._next = next 

    def __init__(self):
        """ 
        _head : pointer to Node
        _size : size of elements in Stack
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """ return number of elements in Stack """
        return self._size

    def push(self, element):
        """ add a node """
        temp = self._Node(element, self._head)
        self._head = temp  
        self._size += 1 

    def top(self):
        """ display the top element """
        if self._size == 0:
            return "Stack is Empty"
        else:
            return self._head._element

    def pop(self):
        """ return the top element """
        if self._size == 0:
            print("Stack is empty no more elements to pop ")
        else:
            temp = self._head._element
            self._head = self._head._next
            self._size -= 1
            return temp

""" Testing """ 
if __name__ == '__main__':
    list = StackLinkedList()
    len(list)
    list.push(12)
    list.push(10)
    print(len(list))
    print(list.top())
    list.pop()
    print(list.top())
    list.pop()
    print(list.top())
    len(list)
    


