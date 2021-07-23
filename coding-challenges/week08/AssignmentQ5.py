def findAppear(nums1, nums2):
    repeetNum = []
    for i in nums1:
        if i in nums2:
            repeetNum.append(i)
            nums2.remove(i)

    return repeetNum


if __name__=="__main__":

    nums1 = [1,2]
    nums2 = [1,1]

    # nums1 = [4,9,5]
    # nums2 = [9,4,9,8,4]

    result = findAppear(nums1, nums2)
    print(result)