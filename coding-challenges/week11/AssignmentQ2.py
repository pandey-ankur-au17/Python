# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
	def isPalindrome(self, head):
		temp = []
		while head != None:
			temp.append(head.val)
			head = head.next			
		if temp == temp[::-1]:
			return True
		else:
			return False


if __name__ == "__main__":

    Solution()