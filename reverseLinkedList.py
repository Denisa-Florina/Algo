class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None  # Nu avem un nod anterior pentru primul element
    current = head
    
    while current:
        next_node = current.next  # Salvăm următorul nod
        current.next = prev       # Inversăm legătura
        prev = current            # Mergem mai departe
        current = next_node       # Avansăm la următorul nod
        
    return prev  # La final, prev va fi noul head al listei

# Funcție pentru a crea o listă legată dintr-o listă de valori
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# Funcție pentru a tipări lista legată
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

# Test
values = [1, 2, 3, 4, 5]
head = create_linked_list(values)
print("Original list:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("Reversed list:")
print_linked_list(reversed_head)
