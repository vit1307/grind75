# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        elif not list2:
            return list1

        curr = list1

        while curr:
            ins = list2
            prev = None
            next = curr.next

            while ins:
                if curr.val <= ins.val:
                    if prev:
                        prev.next = curr
                    else:
                        list2 = curr

                    curr.next = ins

                    break

                if ins.next == None:
                    ins.next = curr
                    curr.next = None
                    break
                else:
                    prev = ins
                    ins = ins.next

            curr = next


        return list2
