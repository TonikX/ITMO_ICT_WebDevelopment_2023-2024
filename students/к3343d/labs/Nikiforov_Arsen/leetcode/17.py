# https://leetcode.com/problems/reverse-nodes-in-k-group/
class Solution(object):
    def reverseKGroup(self, head, k):
        # Функция для разворота связного списка
        def reverseLinkedList(head, k):
            new_head, ptr = None, head
            while k:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head

        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        if count == k:
            reversed_head = reverseLinkedList(head, k)
            head.next = self.reverseKGroup(ptr, k)
            return reversed_head
        return head