from collections import deque


class Queue:
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
        :param name: Describes the comapny name
        :type name: str max_length = 40
        :param country: Depicts the manufacturer's country of origin
        :type country: str max_length = 20
        :param year: depicts the foundation year year of a company
        :type date: 

        .. note::
    '''

    abstract_queue = ['apple', 'banana', 'cherry', 'orange']

    def implement_deque(self):
        q = deque()
        return print(q)


if __name__ == '__main__':
    instance = Queue()
    print(instance.implement_deque())