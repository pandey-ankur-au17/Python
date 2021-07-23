#2nd mathod
def TrappingWater(height):

    if len(height) == 0:
        return 0;

    else:
        res = 0
        for i in range(0, len(height)):
            lMax = 0
            rMax = 0

            for j in range(0, i):
                lMax = max(lMax, height[j])
 
            for j in range(i + 1, len(height)):
                rMax = max(rMax, height[j])
            
            water = min(lMax, rMax) - height[i]
            if (water > 0): 
                res += water
        
        return res;