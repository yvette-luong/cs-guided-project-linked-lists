class ListNode:
    """
    Each ListNode holds a reference to its previous node as well as its next node in the List. 
    That two-directional reference is what allow for our DoublyLinkedList to be doubly-linked ! 
    """

    def __init__(self, value, prev=None, next=None):
        """
        Constructor a node that stores the specified value.
        Prev and Next references are optional on construction and default to None if nothing is specified
        """
        self.prev = prev # the node before this one -defaults to None
        self.value = value # the value to the store
        self.next = next # the Node after this one - defaults to None

    def __repr__(self):
        return f"ListNode({self.value})"

class DoublyLinkedList:
    """
    This is our doubly-linked list class. 
    It holds references to the list's head and tail nodes as well as the list's size
    """ 

    def __init__(self, node=None):
        self.head = node # the first item in list
        self.tail = node # the last item in list
        self.size = 1 if node is not None else 0 # number of items stored in DLL

    def __len__(self):
        """
        Return a string representation of this DoublyLinkedList
        """
        if self.size == 0:
            return "DLL=[]"
        
        str_repr = "DLL=["
        current_node = self.head

        while current_node is not None:
            str_repr += f"{current_node} -> "
            current_node = current_node.next

        str_repr = f"{str_repr[:4]}]"
        return str_repr

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it as the new head of the list.
        Don't forget to handle the old head node's previous pointer accordingly.
        """

        new_node = ListNode(value)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
        
        # Increments the size attribute after adding node to list
        self.size+=1    

    def remove_from_head(self):
        """
        Removes the List's current head node, making the current head's next node the new head of the List.
        Return the value of the removed Node.
        """

        if self.size == 0: # no elements in list
            return None # nothing to return 
        
        removed_value = self.head.value # make a copy of the node to be deleted 

        if self.size == 1: # if only one element in the list (node is head and tail)

            self.head = self.tail = None # list will be empty
        
        else: # more than one element in the list
            self.head = self.head.next # shift head right (reassign head to head.next)
            self.head.prev = None # reassign head.prev to point at None (it used to point at old_head)

        self.size -= 1 
        return removed_value
    
    def add_to_tail(self, value):
        '''
        Wraps the given value in a ListNode and inserts it as the new tail of the list.
        Don't forget to handle the old tail node's next pointer accordingly.
        '''

        new_node = ListNode(value)

        if self.size == 0: # if list is empty 
            self.head = self.tail = new_node # make a new node both head and tail 
        
        else:
            self.tail.next = new_node # place new_node after tail
            new_node.prev = self.tail # place current tail before new_node
            self.tail = new_node # replace self.tail
        
        self.size += 1 # increase size of the list

    def remove_from_tail(self):
        '''
        Removes the List's current tail node, making the current tail's previous node the tail of the List.
        Returns the value of the removed Node.
        '''
        if self.size == 0: # if list is empty
            return None # Nothing to remove, return out 
        
        tail_to_remove = self.tail # copy value of current tail before deletion (for return)
        tail_to_remove.prev = tail_to_remove.next = None # remove any ties to list 

        if self.size == 1: # if only one item in the list 
            self.head = self.tail = None # list will now be empty 
        
        else:
            self.tail.prev.next = None # reassign new tail's prev to None(last item)
            self.tail = self.tail.prev # shift tail left 
        
        self.size -= 1 # decrease size (deleting el)
        return tail_to_remove.value # return value of removed tail

    def move_to_front(self, node):
        '''
        Removes the input node from its current spot in the List 
        and Insert it as the new head node of the List.
        '''

        if self.size == 0: # no items in the list 
            return # nothing to move; return out

        if self.head is node: # if node is head already 
            return # nothing to move, node is at beginning; return out

        if self.tail is node: # if node is tail 
            self.tail = node.prev #shift tail left 
        
        else: #else node must be not tail
            # if node is not tail, then node.next is not None 
            node.next.prev = node.prev # sew node.next to node.prev

        node.prev.next = node.next # if node = tail next is None; else; next is a node. Workds either way! 
        self.head.prev = node.next # assign current head's prev to point at node instead of None 
        node.next = self.head # place node before head 
        self.head = node # reassign head (shifting left) head is now node 
        self.head.prev = None # reassign head.prev to point at None (no nodes before head )



    