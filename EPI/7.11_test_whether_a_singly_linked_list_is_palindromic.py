# Problem: write a program that tests whether a sinlgy linked list is palindromic.

class ListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        result = []
        head = self
        while head:
            result.append(str(head.data)+" -> ")
            head = head.next
        return ''.join(result)

    def __eq__(self, L):
        iter1 = self
        iter2 = L
        while iter1 and iter2:
            if iter1.data != iter2.data:
                return False
            iter1 = iter1.next
            iter2 = iter2.next

        return (not iter1) and (not iter2)

# EPI Judge: is_list_palindromic.py
def is_linked_list_a_palindrome(L):

    def reverse_list(start):
        if not start.next:
            return
        prev_head = start.next
        while prev_head.next:
            temp = prev_head.next
            prev_head.next = temp.next
            temp.next = start.next
            start.next = temp

    dummy_head = ListNode(next=L)
    iterator_slow, iterator_fast = dummy_head, dummy_head
    while iterator_fast.next and iterator_fast.next.next:
        iterator_fast = iterator_fast.next.next
        iterator_slow = iterator_slow.next

    reverse_list(iterator_slow)

    second_half_iter = iterator_slow.next
    first_half_iter = dummy_head.next
    while second_half_iter:
        if second_half_iter.data != first_half_iter.data:
            reverse_list(iterator_slow)
            return False
        second_half_iter = second_half_iter.next
        first_half_iter = first_half_iter.next

    reverse_list(iterator_slow)
    return True

def array_to_list(L):
    dummy_head = ListNode()
    previous = dummy_head
    for e in L:
        current = ListNode(data=e)
        previous.next = current
        previous = current

    return dummy_head.next

if __name__ == "__main__":
    L = [2, 5, 3, 1, 3, 5, 3, 4, 2, 5, 5, 6, 3, 2, 2, 4, 3, 4, 5, 6, 
         6, 5, 4, 3, 4, 2, 2, 3, 6, 5, 5, 2, 4, 3, 5, 3, 1, 3, 5, 2]
    L1 = array_to_list(L)
    L2 = array_to_list(L)
    assert L1 == L2
    result = is_linked_list_a_palindrome(L2)
    assert L1 == L2
    assert  result == True
