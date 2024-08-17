# Leetcode 681: Next Closest Time
# Google Problem 

class Solution:
    def nextClosestTime(self, time: str) -> str:
        # make two lists
        # hours possible
        # minutes possible
        # sort both lists 
        # starting from closest hour check every possible minute
            # if valid minute is found return that combo
        # if no vaild minute is found increase hour
        # if reached end of hour list loop back to 0th index and check again from there
        
        hours = []
        minutes = []        
        digits = list(time)
        digits.remove(":")
        
        iHour = int(digits[0] + digits[1])
        iMin = int(digits[2] + digits[3])
                          
        def findPossibleTimes(digits, digitLimit): 
            possibleTimes = set() # prevents duplicates
            for i in digits: 
                for j in digits: 
                    if int(i+j) <= digitLimit: 
                        possibleTimes.add(int(i+j))
            return possibleTimes
        
        hours = list(findPossibleTimes(digits, 23))
        minutes = list(findPossibleTimes(digits, 59))
        hours.sort()
        minutes.sort()
        
        startHour = hours.index(iHour)
        startMin = minutes.index(iMin)
        # need to reorder list such that we start at closest hour
        # and then increase until loops to the next day
        hoursSearch = hours[startHour:]
        for hour in hours[:startHour]:
            hoursSearch.append(hour)
        
        for hour in hoursSearch:  
            if int(hour) == iHour: 
                for mins in minutes[startMin+1:]:
                    timeNext = str(hour).zfill(2) + ":" + str(mins).zfill(2)
                    return timeNext
            else:
                timeNext = str(hour).zfill(2) + ":" + str(minutes[0]).zfill(2)
                return timeNext
        
        # will only reach if time given has only one unique digit            
        return time