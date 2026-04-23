# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy

        while list1 and list2: #loops until one of them becomes empty
            if list1.val<=list2.val: #it picks the smaller node as lists are sorted if value of l1 is <= l2 then
                tail.next = list1 #the tail will move to l1
                list1 = list1.next #l1 will be next

            else:
                tail.next = list2 #if not the tail will move to l2
                list2 = list2.next

            tail = tail.next #tail always points to the last node in merged list
        
        if list1:
            tail.next = list1 #if l1 has still nodes left it will attach the remaining to the merged list
        else:
            tail.next = list2 #if l2 has still nodes left it will attach the remaining to the merged list
        
        return dummy.next

