def find_dup (nums):
    pt1 = 0
    pt2 = 0
    while True:
        pt1 = nums[pt1]
        pt2 = nums[nums[pt2]]
        if pt1 == pt2:
            break
        print ("round")
        print (pt1)
        print (pt2)
    print ("pt")
    print (pt1)

    pt1 = 0
    result = 0
    while True:
        print ("round 2")
        print (pt1)
        print (pt2)
        if nums[pt1] == nums[pt2]:
            result = nums[pt1]
            break

        pt1 +=1 
        pt2 = nums[pt2]

        
    print ("result")
    print (result)



nums = [1,3,4,2,2]
nums1 = [3,1,3,4,2]
nums1 = [1,3,4,2,5,7,6,1]
find_dup(nums1)
