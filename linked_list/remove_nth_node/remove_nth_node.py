""" Solution Module """
from utils.linked_list import LinkedList, ListNode


class Solution:
    """ Solution Class """

    def run_solution(self, test_input):
        """ Solution Method """
        [nums, n] = test_input

        linked_list = LinkedList()

        for num in nums:
            linked_list.append(num)

        dummy = ListNode(0, linked_list.head)
        left = dummy
        right = linked_list.head

        for _ in range(0, n):
            right = right.next_node

        # Move the window till right is in the end of the list.
        while right:
            left = left.next_node
            right = right.next_node

        # Now left.next is the node to delete. So connect the next one
        left.next_node = left.next_node.next_node

        curr = dummy.next_node
        while curr:
            print(curr.data)
            curr = curr.next_node
        linked_list.display()
