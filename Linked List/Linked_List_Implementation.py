class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        return

    def insert_list_of_values(self, list_of_values):
        for vals in list_of_values:
            self.insert_at_end(vals)

    def insert_at_index(self, index, value):
        if 0 > index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_beginning(value)
            return
        if index == self.get_length() - 1:
            self.insert_at_end(value)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(value,itr.next)
                itr.next = node
                break
            itr = itr.next
            count+=1

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at_index(self,index):
        if 0 > index >= self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def print(self):
        if self.head is None:
            print("Linked List Is Empty")
            return
        ll_str = str()
        itr = self.head
        while itr:
            ll_str += str(itr.data) + " -> "
            itr = itr.next
        print(ll_str + "None")


L = LinkedList()

L.insert_at_beginning(10)
L.insert_at_end(80)
L.insert_at_beginning(20)
L.insert_at_end(30)
L.insert_at_beginning(70)
list_of_values = ["Apple", "Samsung", "OnePlus"]
L.insert_list_of_values(list_of_values)
# L.remove_at_index(1)
L.insert_at_index(4,99)
L.print()
print("Length of my Linked List is -> ", L.get_length())