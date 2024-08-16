# Google question relatively frequent
class Logger:

    def __init__(self):
        self.timeAllowed = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message in self.timeAllowed: 
            if timestamp >= self.timeAllowed[message]: 
                self.timeAllowed[message] = timestamp + 10
                return True
            else: 
                return False
        else: 
            self.timeAllowed[message] = timestamp + 10 
            return True  