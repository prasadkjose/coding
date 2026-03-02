""" Solution Module """
from utils.linked_list import LinkedList


class Solution:
    """ Solution Class """

    def run_solution(self, test_input):
        """ Solution Method """
        new_list = LinkedList()
        for i in test_input:
            new_list.append(i)

        # Brute force - Store nodes in an array and use two indexes from front and back
        # node_arr = []
        # curr = new_list.head
        # while curr:
        #     node_arr.append(curr)
        #     curr = curr.next_node

        # i = 0
        # j = len(node_arr) - 1

        # while i < j:
        #     node_arr[i].next_node = node_arr[j]
        #     i += 1
        #     node_arr[j].next_node = node_arr[i]
        #     j -= 1

        # node_arr[i].next_node = None
        # new_list.display()

        # Efficient Method - Reverse and Merge

        # Two Pointers fast and slow
        fast, slow = new_list.head.next_node, new_list.head

        # Move twice as fast, so slow is in the middle node
        while fast and fast.next_node:
            slow = slow.next_node
            fast = fast.next_node.next_node

        second = slow.next_node
        first = slow.next_node = None
        while second:
            tmp = second.next_node
            second.next_node = first
            first = second
            second = tmp

        first, second = new_list.head, first
        while second:
            tmp1, tmp2 = first.next_node, second.next_node
            first.next_node = second
            second.next_node = tmp1
            first, second = tmp1, tmp2

        # print(slow.data, fast.data)
        # new_list.display()
