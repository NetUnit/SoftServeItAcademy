from collections import deque
from queue import Queue


class Queue1(Queue):
    '''
    ==================================================================
    This class describes basic queues like a linear data structures
    ==================================================================

    Operations associated with queue are:

        Enqueue: Adds an item to the queue. If the queue is full, then it
        is said to be an Overflow condition – Time Complexity : O(1)
        Dequeue: Removes an item from the queue. The items are popped in
        the same order in which they are pushed. If the queue is empty,
        then it is said to be an Underflow condition – Time Complexity : O(1)
        Front: Get the front item from queue – Time Complexity : O(1)
        Rear: Get the last item from queue – Time Complexity : O(1)

    Attrs:
        :param maxsize: number of items allowed in the queue
        :type maxsize: int


    .. note::
        queues could not be modified during iteration

        Queues useful for the reason:
        put() - place the item into a queue last
        get_item() - takes first item from the queue,
        so the least recently added item is removed first

        https://www.geeksforgeeks.org/queue-in-python/
        https://i.imgur.com/tJoe7AH.png
    '''
    list_ = ['apple', 'banana', 'cherry', 'orange']
    maxsize = 3
    
    def create_deque(self):
        from collections import deque
        self.deque = deque()
        for fruit in self.list_:
            self.deque.append(fruit)
        return self.deque

    def implement_deque(self):
        deque = self.create_deque()
        print(deque)

        deque.append('fruit1')
        deque.append('fruit2')

        deque.popleft()
        print(deque)
        # deque.popleft()
        # print(deque)
        # deque.popleft()
        # print(deque)
        # deque.popleft()
        # print(deque)
        return deque

    def get_size(self):
        '''
        :returns: number of items in the queue
        '''
        return self.qsize()

    def get_empty(self):
        '''
        :returns: True if the queue is empty, False otherwise
        '''
        return self.empty()
    
    def get_item(self):
        item = self.get()
        return item

    def fulfill_queue(self):
        self.put('orange')
        self.put('banana')
        self.put('lichi')
        # will raise Full exception
        # self.put_nowait('lemon')
        
        # appple is excessive
        # as the queue size is 3
        # self.put('apple')
        return self

if __name__ == '__main__':
    deque = Queue1()
    print(deque.implement_deque())
    # returns True as it was dequeued
    print(deque.get_empty())
    # returns False as it' empty not full
    print(deque.full())
    

    queue = Queue1(maxsize=3)
    print(queue.get_size())
    queue.fulfill_queue()
    print(queue.get_size())
    # print(queue.__dict__)
    print(queue.empty())
    print(queue.full())
    
    # will return firts item - orange
    # queue will remove this item from queue
    print(queue.get_item())
    print(queue.__dict__)
    queue.put_nowait('lemon')
    print(queue.__dict__)
    # Return an item if one is immediately
    # available, else raise QueueEmpty
    print(queue.get_nowait())
    print(queue.get_nowait())
