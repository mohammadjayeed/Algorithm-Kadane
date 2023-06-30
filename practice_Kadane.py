def maxSubArray(nums):
    
    l = []
    prev = 0
    for i in range(0,len(nums)):
        
        if i == 0:
            
            prev = nums[i]
            l.append(prev)
        else:
            current_total = prev + nums[i]
            current_value = nums[i]
            
            if current_total > current_value :
                prev = current_total
                l.append(prev)
                continue
            prev = current_value
            l.append(prev)
            
       
           
    return max(l)