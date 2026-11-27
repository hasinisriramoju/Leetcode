class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        seen1={}

        for i in magazine:
            if i in seen1:
                seen1[i]+=1
            else:
                seen1[i]=1

        for i in ransomNote:
            if i not in seen1 or seen1[i]==0:
                return False
            else:
                seen1[i]-=1

        return True
        