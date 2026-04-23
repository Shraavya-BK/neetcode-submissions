# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None #previous value will be none
        current = head #pointer will start at the head

        while current: #loops until it reaches the last value in the array i.e it has assigned NONE to all the values
        
            next_node=current.next #once reached the nth value we are going to lock it
            current.next=prev #once locked the pointer eill be at the nth value and will move backward
            prev=current #previous value of the nth node will become the current value
            current=next_node #current value will become the nect node and this continues until we have fetched all the values

        return prev
