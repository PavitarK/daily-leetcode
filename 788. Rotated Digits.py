# Leetcode 788
# Google Mock Assesment 
class Solution:
    def rotatedDigits(self, n: int) -> int:
        mapping = {
            "0" : "0",
            "1" : "1",
            "2": "5",
            "3" : "-1",
            "4" : "-1",
            "5" : "2",
            "6" : "9",
            "7" : "-1",
            "8" : "8",
            "9" : "6"
        }
        count = 0
 
        for i in range(1,n+1):
            digits = list(str(i))
            if "3" in digits or "4" in digits or "7" in digits: 
                continue
            else: 
                newDigits = digits.copy()
                for j in range(len(digits)): 
                    newDigits[j] = mapping[digits[j]]
                newNum = 0
                oldNum = i
                for num in newDigits:
                    newNum = newNum*10 + int(num)
                #print(f"NEW NUM IS: {newNum}")
                #print(f"OLD NUM IS: {oldNum}")
                if oldNum != newNum: 
                    #print("INCREASING COUNT")
                    count +=1
            
            
        return count
        
        