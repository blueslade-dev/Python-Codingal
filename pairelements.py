class Pair_elements:
    def twosums(self,nums,target):
        lookup = {}
        for i,num in enumerate(nums):
            if target - num in lookup:
                return lookup[target-num],i
            lookup[num] = 1

ob = Pair_elements()
print("Index1-%d, Index2-%d" % ob.twosums((10,20,30,40,50,60,70),50))                        