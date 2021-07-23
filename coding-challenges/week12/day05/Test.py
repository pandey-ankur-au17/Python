#  #Q1
 
# def sum_of_digit(N):
#     if N < 10 :
#         return N
#     else:
#         result=N%10 + sum_of_digit(N//10)

#     return sum_of_digit(result)

# N = int(input("Enter number: "))

# digit_sum = sum_of_digit(N)

# print(digit_sum)

# ------------------------------------------------------------------------------------------------#
# def sortSquare(arr, n):
    
#     for i in range(n):
#         arr[i]= arr[i] * arr[i]
#     arr.sort()
 

# input_string = input()
# user_list = input_string.split()
# for i in range(len(user_list)):
#     user_list[i] = int(user_list[i])

# arr=user_list

# # n = int(input())
# # for i in range(0, n):
# #     ele = int(input())
# #     arr.append(ele) 
# n = len(arr)
# sortSquare(arr, n)
# for i in range(n):
#     print(arr[i], end = " ")



# -------------------------------------------------------------------------------------#
#   ###### QQQQQ444444444444444444444444444444##############################

# # class Node:
     
# #     def __init__(self):
         
# #         self.data = 0
# #         self.next = None

# def countOfNodes(head):
 
#     count = 0
     
#     while (head != None):
#         head = head.next
#         count += 1
     
#     return count

# def deleteMid(head):

#     if (head == None):
#         return None
#     if (head.next == None):
#         del head
#         return None
 
#     copyHead = head

#     count = countOfNodes(head)
  

#     mid = count // 2

#     while (mid > 1):
#         mid -= 1
#         head = head.next

#     head.next = head.next.next
  
#     return copyHead
# def printList(ptr):
 
#     while (ptr != None):
#         print(ptr.data, end ="")
#         ptr = ptr.next
# def newNode(data):
 
#     temp = Node()
#     temp.data = data
#     temp.next = None
#     return temp

# # if __name__=='__main__':

# #     head = newNode(1)
# #     head.next = newNode(2)
# #     head.next.next = newNode(3)
# #     head.next.next.next = newNode(4)
  
# #     print("Gven Linked List")
# #     printList(head)
  
# #     head = deleteMid(head)
  
# #     print()

# #     printList(head)
   

# #################QQQQQQQQQQQQQQQQQQ444444444444444444444444444444  exact Solutions ###################


# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys

# '''
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# '''


# def deleteMid(head):
#     '''
#     head:  head of given linkedList
#     return: head of resultant llist
#     '''
    
# def countOfNodes(head):
 
#     count = 0
     
#     while (head != None):
#         head = head.next
#         count += 1
     
#     return count

# def deleteMid(head):

#     if (head == None):
#         return None
#     if (head.next == None):
#         del head
#         return None
 
#     copyHead = head

#     count = countOfNodes(head)
  

#     mid = count // 2

#     while (mid > 1):
#         mid -= 1
#         head = head.next

#     head.next = head.next.next
  
#     return copyHead
# def printList(ptr):
 
#     while (ptr != None):
#         print(ptr.data, end ="")
#         ptr = ptr.next
# def newNode(data):
 
#     temp = Node()
#     temp.data = data
#     temp.next = None
#     return temp





# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class Llist:
#     def __init__(self):
#     	self.head=None
#     def insert(self,data,tail):
#         node=Node(data)
#         if not self.head:
#             self.head=node
#             return node
#         tail.next=node
#         return node
# def printList(head):
#     while(head):
#         print(head.data,end=" ")
#         head=head.next
#     print()

# if __name__ == '__main__':
#     t=int(input())
#     for tcs in range(t):
#         n=int(input())
#         arr1=[int(x) for x in input().split()]
#         ll=Llist()
#         tail=None
#         for nodeData in arr1:
#             tail=ll.insert(nodeData,tail)
#         res=deleteMid(ll.head)
#         printList(res)





# ###################################QQQQQQQQQQQQQQQQQQQQQQQ333333333333333333333333333333333333333333#############################################

# def max_idx_pref():
#     sum = 0
#     idx = -1
#     for i in range(len(arr)):
#         sum = sum + arr[i]
#         if sum > k:
#             idx = i -1
#             break
#     if idx == -1:
#         print(-1)
#     else:
#         print(idx)

# n, k = input().split()
# arr = list(map(int, input().split()))
# n = int(n)
# k = int(k)        
# max_idx_pref()
