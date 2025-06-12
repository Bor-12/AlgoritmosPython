from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    ultimo = dummy
    while list1 and list2:
        if list1.val < list2.val:
            ultimo.next = list1
            list1 = list1.next
        else:
            ultimo.next = list2
            list2 = list2.next
        ultimo = ultimo.next
    if list1:
        ultimo.next = list1
    else:
        ultimo.next = list2
    return dummy.next