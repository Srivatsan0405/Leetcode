class Solution:
    def defangIPaddr(self, address: str) -> str:
        a=""
        for i in address:
            if i==".":
                a=a+'[.]'
            else: 
                a=a+i
            
        return a