import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def insert_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_middle(self, index, data):
        if index < 0:
            raise IndexError("Index cannot be negative")
        if index == 0:
            self.insert_beginning(data)
            return

        current = self.head
        for _ in range(index - 1):
            if current is None:
                raise IndexError("Index out of range")
            current = current.next

        if current is None:
            self.insert_end(data)
        else:
            new_node = Node(data)
            new_node.next = current.next
            new_node.prev = current
            current.next.prev = new_node
            current.next = new_node

    def pop_head(self):
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        if self.head is not None:
            self.head.prev = None
        else:
            self.tail = None
        return data

    def pop_tail(self):
        if self.tail is None:
            return None
        data = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        else:
            self.head = None
        return data

    def reverse(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        while current is not None:
            current.next, current.prev = current.prev, current.next
            current = current.prev  # Move to the now-previous node

        self.head, self.tail = self.tail, self.head

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_list_reverse(self):
        current = self.tail
        while current is not None:
            print(current.data, end=" ")
            current = current.prev
        print()

    def make_circular(self):
        if self.head is not None:
            self.tail.next = self.head
            self.head.prev = self.tail

    def move(self, steps):
        if self.head is None:
            return None

        current = self.head
        for _ in range(steps):
            current = current.next
            if current is None:  # Handle wrapping around in circular list
                current = self.head 

        return current.data
    
    def reverse_move(self, steps):
        if self.head is None:
            return None

        current = self.head
        for _ in range(steps):
            current = current.prev
            if current is None:  # Handle wrapping around in circular list
                current = self.tail

        return current.data
    

# Example usage
if __name__ == "__main__":
    linked_list = CircularLinkedList()

    # Create a list with 10 random values
    for _ in range(10):
        linked_list.insert_end(random.randint(1, 50))

    linked_list.print_list()  # Output will vary due to randomness

    linked_list.make_circular()

    # Example of move function
    move_value = 17
    value = linked_list.move(move_value)
    print(f"Value at {move_value} steps:", value)
    value = linked_list.reverse_move(6)
    print(f"Value at {move_value} steps in reverse:", value)