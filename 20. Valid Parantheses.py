def isValid(s: str) -> bool:
    if len(s)%2 == 1: 
        return False

    stack = []
    opening = ["{", "[", "("]
    pairs = ["{}", "[]", "()"]
    
    for bracket in s: 
        if bracket in opening: 
            stack.append(bracket)
        else:
            try: 
                pair = stack[-1]+bracket
            except(IndexError): 
                return False
            if pair in pairs: 
                stack.pop()
            else: 
                return False
    if not stack: 
        return True
    return False