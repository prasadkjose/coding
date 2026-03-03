""" Solution Module """
from utils.linked_list import LinkedList
class Solution:
    """ Solution Class """
    def run_solution(self, test_input):
        """ Solution Method """

        linked_list = LinkedList()
        for num in test_input:
            linked_list.append(num)

        # Go to the middle and reverse the end. Check start to end one by one. 
        head = linked_list.head

        slow, fast = head, head
        while fast.next_node and fast.next_node.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

        # reverse from the mid to the end.
        prev = None
        curr = slow.next_node
        while curr:
            temp = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = temp

        while head and prev:
            if head.data != prev.data:
                return False
            head = head.next_node
            prev = prev.next_node
        
        linked_list.display()
        return True
