# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fp= head
        sp = head
        if not head.next:
            return None
        while fp.next and fp.next.next and fp.next.next.next:
            sp = sp.next
            fp = fp.next.next
        else:
            print(sp.val,  " " , fp.val)
            sp.next = sp.next.next
        return head
        