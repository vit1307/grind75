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
        ins = list2
        prev = None

        while curr:
            next = curr.next

            while curr.val > ins.val: 
                if ins.next == None:
                    ins.next = curr
                    return list2

                prev = ins    
                ins = ins.next

            if prev:
                prev.next = curr
            else:
                list2 = curr

            curr.next = ins
            
            prev = curr 
            curr = next

        return list2
        
