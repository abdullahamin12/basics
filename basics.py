class Solution:
    def isValidself(self,x):
        bool=False
        for i in range(len(x)-1):
            if x[i]==x[::-1]:
                bool=True
            elif x[i]==x[i+1]:
                bool=True
            else:
                bool=False
                break
        return bool

s=Solution()
a=s.isValidself("()[]{}")
        
 