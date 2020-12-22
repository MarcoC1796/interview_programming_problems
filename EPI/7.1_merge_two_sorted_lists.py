# Problem: The merge of two singly-linked lists is a list consisting of the nodes of the two lists in which numbers
#          appear in ascending order. Write a program that takes two singly-linked lists, assumed to be sorted, 
#          and returns their merge. The only field your program can change in a node is its next field.

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


# EPI Judge: sorted_lists_merge.py
def merge_two_sorted_lists(L1, L2):
    dummy_head = ListNode()
    prev_node = dummy_head

    while L1 and L2:
        if L1.data <= L2.data:
            prev_node.next = L1
            L1 = L1.next
        else:
            prev_node.next = L2
            L2 = L2.next
        prev_node = prev_node.next

    if L1:
        prev_node.next = L1
    if L2:
        prev_node.next = L2

    return  dummy_head.next

if __name__ == "__main__":
    L1 = ListNode()
    head1 = L1
    for i in range(50):
        head1.next = ListNode(i)
        head1 = head1.next

    L2 = ListNode()
    head2 = L2
    for i in range(25,69):
        head2.next = ListNode(i)
        head2 = head2.next

    print(merge_two_sorted_lists(L1.next, L2.next))

    
