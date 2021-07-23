# Given an integer array , every element is repeated TWICE , except one
# element , Find that element ?
# Input : - [1 , 2 , 1, 2 ,4 , 3 ,4]
# Output: - 3

def nonrepeated_elements(list1):
    res=dict()
    for i in list1:
        if (i not in res):
            res[i]=1
        else:
            res[i]+=1
    for key,value in res.items():
        if(value==1):
            print(key)
            return(key)
list1=[1,2,1,2,3,4,3]
nonrepeated_elements(list1)
