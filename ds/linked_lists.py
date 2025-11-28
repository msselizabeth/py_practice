
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            
        while cur.next:
            cur = cur.next
            
        cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Prev node is undefined.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def insert_before(self, next_node: Node, data):
        # check if next exists
        if next_node is None:
            print("Next node is undefined")
            return
        
        cur = self.head
        prev = None
        
        # find prev 
        while cur and cur != next_node:
            prev = cur
            cur = cur.next
        
        new_node = Node(data)
        new_node.next = next_node
        prev.next = new_node
        

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
            
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        res = []
        while current:
            # print(current.data)
            res.append(current.data)
            current = current.next
        
        print(res)
            

llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

print("Зв'язний список1:")
llist.print_list()

element = llist.search_element(5)
if element:
    print(element.data)
llist.insert_after(prev_node=element, data=1)

# Друк зв'язного списку
print("Зв'язний список2:")
llist.print_list()


element_next = llist.search_element(10)
llist.insert_before(element_next, 7)
print("Зв'язний список3:")
llist.print_list()


# # Видаляємо вузол
# llist.delete_node(10)

# print("\nЗв'язний список після видалення вузла з даними 10:")
# llist.print_list()

# # Пошук елемента у зв'язному списку
# print("\nШукаємо елемент 15:")
# element = llist.search_element(15)
# if element:
#     print(element.data)
