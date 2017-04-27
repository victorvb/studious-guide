"""
Author: Long Yu
Date: April 18th 2017
Descriptions: Using Linked List to implement Queue 
"""

class QueueLinkedList:
    """ build a Queue using Linked List """

    class _Node:
        """ simple Node class """
        __slots__ = '_element', '_next'

        def __init__(self, e, next):
            """ constructor """
            self._element = e
            self._next = next 
        
    def __init__(self):
        """ constructor 
        _head : head pointer to first element 
        _tail : pointer to last element 
        _size : size of the Queue
        """

        self._head = None
        self._tail = self._head
        self._size = 0

    def __len__(self):
        """ 
        """

        return self._size

    def enqueue(self, e):
        """ add an element to the queue 
        e : element need to add
        """
        if self.is_empty():
            temp = self._Node(e, None)
            self._head = temp
        else:
            temp = self._Node(e, None)
            self._tail._next = temp

        self._tail = temp
        self._size += 1

    def dequeue(self):
        """ 
            remove an element from queue
            return the element
        """
        if self.is_empty():
            print("Queue is empty")
        else:
            temp = self._head 
            self._head = self._head._next
            self._size -= 1
            if self.is_empty():
                self._tail = None
        return temp._element
                   
            

    def first(self):
        """ 
        return first element in Queue 
        and without removing it 
        """
        if self.is_empty():
            return "Queue is empty"
        else:
            return self._head._element

    def is_empty(self):
        """ 
           check if queue is empty
        """

        return self._size == 0

if __name__ == '__main__':

    queueList = QueueLinkedList()
    queueList.enqueue(12)
    queueList.enqueue(10)
    print(queueList.first())
    queueList.dequeue()
    print(queueList.first())
    queueList.dequeue()
    print(queueList.first())
    queueList.enqueue(13)
    print(queueList.first())


   
   

        

